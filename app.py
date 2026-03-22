import pandas as pd
import streamlit as st
from helper import * 

summer_df , winter_df = data_preprocessor()

#st.dataframe(summer_df)
#st.dataframe(winter_df)
#st.write("Before")
#st.write(summer_df.shape)
#st.write(winter_df.shape)

summer_df,winter_df = duplicate_rows_remover(summer_df,winter_df)
summer_df.dropna(subset = ["region"],inplace = True)
winter_df.dropna(subset = ["region"],inplace = True)

#st.write("After")
#st.write(summer_df.shape)
#st.write(winter_df.shape)

st.sidebar.title("MENU")
season = st.sidebar.radio("Choose Season " , ("Summer", "Winter"))
options = st.sidebar.radio("Options",("Medal-Tally","County-wise","Year-wise","Year-wise-progress"))

###MEDAL TALLY FOR SUMMER OLYMPICS
if season =="Summer" and options == "Medal-Tally":
    st.subheader("Summer Olympics Medal Tally:")
    medal_pivot_summer = medal_tally_calculator(summer_df)
    medal_pivot_summer = medal_pivot_summer.sort_values(by=["Bronze","Gold","Silver"],ascending = False)
    st.dataframe(medal_pivot_summer)
### MEDAL TALLY FOR WINTER OLYMPICS
if season =="Winter" and options == "Medal-Tally":
    st.subheader("Winter Olympics Medal Tally:")
    medal_pivot_Winter = medal_tally_calculator(winter_df)
    medal_pivot_Winter = medal_pivot_Winter.sort_values(by=["Bronze","Gold","Silver"],ascending = False)
    st.dataframe(medal_pivot_Winter)
###COUNTRY WISE
elif season =="Summer" and options == "County-wise":
    st.subheader("Summer Olympics Country-Wise:")
    medal_pivot_summer = medal_tally_calculator(summer_df)
    noc = st.selectbox("Choose the Country",medal_pivot_summer.index.to_list())
    details = country_wise_search(noc ,medal_pivot_summer)
    table = pd.DataFrame().from_dict(details,orient = "index",columns =["values"])
    st.dataframe(table)
    
elif season =="Winter" and options == "County-wise":
    st.subheader("Winter Olympics Country-Wise:")
    medal_pivot_winter = medal_tally_calculator(winter_df)
    noc = st.selectbox("Choose the Country",medal_pivot_winter.index.to_list())
    details = country_wise_search(noc ,medal_pivot_winter)
    table = pd.DataFrame().from_dict(details,orient = "index",columns =["values"])
    st.dataframe(table)    
###  YEAR WISE
elif season =="Summer" and options == "Year-wise":
    st.subheader("Summer Olympics Year Wise:")
    years = sorted(summer_df["Year"].unique())
    selected_year = st.selectbox("Select Year" , years)
    countries = sorted(summer_df[summer_df["Year"]==selected_year]["region"].unique())
    selected_country = st.selectbox("Select Country :" , countries)
    plot_medals(selected_year,selected_country,summer_df)
elif season =="Winter" and options == "Year-wise":
    st.subheader("Winter Olympics Year Wise:")
    years = sorted(winter_df["Year"].unique())
    selected_year = st.selectbox("Select Year" , years)
    countries = sorted(winter_df[winter_df["Year"]==selected_year]["region"].unique())
    selected_country = st.selectbox("Select Country :" , countries)
    plot_medals(selected_year,selected_country,winter_df)
    
### YEAR WISE PROGRESS
elif season =="Summer" and options == "Year-wise-progress":
    st.subheader("Summer Olympics Year Wise Progress:")
    countries = sorted(summer_df["region"].unique())
    selected_country = st.selectbox("Select Country :" , countries)
    year_analysis(selected_country,summer_df)
elif season =="Winter" and options == "Year-wise-progress":
    st.subheader("Winter Olympics Year Wise Progress:")
    countries = sorted(winter_df["region"].unique())
    selected_country = st.selectbox("Select Country :" , countries)
    year_analysis(selected_country,winter_df)