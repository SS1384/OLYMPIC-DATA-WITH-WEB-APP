import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

athletes =pd.read_csv(r"athlete_events.csv") 
regions =pd.read_csv(r"noc_regions.csv") 

def data_preprocessor():
    global athletes,regions
    df = pd.merge(athletes , regions , on= "NOC")
    df.drop_duplicates(inplace = True)
    df["Medal"].fillna("No Medal",inplace = True)
    summer_df = df[df["Season"] =="Summer"]
    winter_df = df[df["Season"] =="Winter" ]
    return summer_df,winter_df

def duplicate_rows_remover(df1,df2):
    df1 = df1.drop_duplicates(subset = ["Team","NOC","Games","Year","Season","City","Sport","Event"])
    df2 = df2.drop_duplicates(subset = ["Team","NOC","Games","Year","Season","City","Sport","Event"])
    return df1,df2
def medal_tally_calculator(df):
    medal_count = df.groupby(["NOC","Medal"]).size().reset_index(name = "count")
    medal_pivot = medal_count.pivot(index = "NOC" , columns = "Medal" , values = "count").fillna(0)
    medal_pivot =medal_pivot.astype(int)
    if "No Medal" in medal_pivot.columns:
        medal_pivot.drop(columns = "No Medal",inplace =True)
    medal_pivot["Total_Medal"] = medal_pivot[["Bronze","Gold","Silver"]].sum(axis = 1)
    return medal_pivot
def country_wise_search(noc,pivot_table):
    if noc in pivot_table.index:
        details={
            "Gold":pivot_table.loc[noc,"Gold"],
            "Bronze":pivot_table.loc[noc,"Bronze"],
            "Silver":pivot_table.loc[noc,"Silver"],
            "Total_Medal":pivot_table.loc[noc,"Total_Medal"]
        }
        return details
    else:
        print("NO NOC exists")

def plot_medals(year,country,df):
    medals_count = df.groupby(["Year","region","Medal"]).size().unstack(fill_value = 0)
    medals_count = medals_count.reset_index() 
    medals_count["Total_Medals"] = medals_count["Gold"] + medals_count["Bronze"] + medals_count["Silver"]
    
    filtered_df = medals_count[(medals_count["Year"] == year) & (medals_count["region"] == country)]
    if filtered_df.empty:
        print(f"No Olympic data found for {country} in {year}.")
        return
    gold = filtered_df["Gold"].values[0]
    bronze = filtered_df["Bronze"].values[0]
    silver = filtered_df["Silver"].values[0]
    total_medals = filtered_df["Total_Medals"].values[0]

    fig,ax = plt.subplots(figsize=(4,3))
    medals = ["Bronze","Gold","Silver","Total_Medals"]
    counts = [bronze,gold,silver,total_medals]
    ax.bar(medals,counts,color = ["green","blue","brown" , "yellow"])
    st.pyplot(fig)


def year_analysis(country,df):
    medals_count = df.groupby(["Year","region","Medal"]).size().unstack(fill_value = 0)
    medals_count = medals_count.reset_index() 
    medals_count["Total_Medals"] = medals_count["Gold"] + medals_count["Bronze"] + medals_count["Silver"]
    filtered_df = medals_count[medals_count["region"]==country]
    fig,ax = plt.subplots(figsize=(4,3))
    ax.plot(filtered_df["Year"],filtered_df["Gold"],color="gold",label = "GOLD",marker="o",linestyle = "-")
    ax.plot(filtered_df["Year"],filtered_df["Bronze"],color="brown",label = "BRONZE",marker="o",linestyle = "-")
    ax.plot(filtered_df["Year"],filtered_df["Silver"],color="silver",label = "SILVER",marker="o",linestyle = "-")
    ax.plot(filtered_df["Year"],filtered_df["Total_Medals"],color="black",label = "TOTAL MEDALS",marker="o",linestyle = "-")
    ax.legend()
    st.pyplot(fig)