import pandas as pd
import streamlit as st
import plotly.express as px
import mysql.connector
import requests
import json
from streamlit_option_menu import option_menu

# Set page config
st.set_page_config(page_title="PhonePe Data Analysis and Visualization", layout="wide")

# Title
st.title("📊 PhonePe Data Analysis and Visualization Dynamics Dashboard")

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",  # replace with your password
    database="phonepe_data"
)

cursor = conn.cursor()

def load_data():
    query = """
        SELECT *
        FROM agg_ins_table;
    """
    return pd.read_sql(query, conn)

def load_data1():
    query = """
        SELECT *
        FROM agg_trans_table;
    """
    return pd.read_sql(query, conn)

def load_data2():
    query = """
        SELECT *
        FROM agg_user_table;
    """
    return pd.read_sql(query, conn)

def load_data3():
    query = """
        SELECT *
        FROM map_ins_table;
    """
    return pd.read_sql(query, conn)

def load_data4():
    query = """
        SELECT *
        FROM map_user_table;
    """
    return pd.read_sql(query, conn)

def load_data5():
    query = """
        SELECT *
        FROM map_trans_table;
    """
    return pd.read_sql(query, conn)

def load_data6():
    query = """
        SELECT *
        FROM top_ins_table;
    """
    return pd.read_sql(query, conn)

def load_data7():
    query = """
        SELECT *
        FROM top_user_table;
    """
    return pd.read_sql(query, conn)

def load_data8():
    query = """
        SELECT *
        FROM top_trans_table;
    """
    return pd.read_sql(query, conn)

def load_data9():
    query = """
        SELECT *
        FROM top_ins_dist_table;
    """
    return pd.read_sql(query, conn)

def load_data10():
    query = """
        SELECT *
        FROM top_user_dist_table;
    """
    return pd.read_sql(query, conn)

def load_data11():
    query = """
        SELECT *
        FROM top_trans_dist_table;
    """
    return pd.read_sql(query, conn)

# Load the data
df = load_data()
df1 = load_data1()
df2 = load_data2()
df3 = load_data3()
df4 = load_data4()
df5 = load_data5()
df6 = load_data6()
df7 = load_data7()
df8 = load_data8()
df9 = load_data9()
df10 = load_data10()
df11 = load_data11()

# Sidebar filters
with st.sidebar:
     selected = option_menu("Main Menu", ["Home", "Analytics", "Insights", "About"],
                           icons=['house', 'bar-chart', 'lightbulb', 'info-circle'],
     menu_icon="cast", default_index=0, 
     styles={
            "container": {"padding": "5!important", "background-color": "#FF7A30", "width": "250px"},
            "icon": {"color": "black", "font-size": "18px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#FF7A30", "color": "white"},
        }
     )

if selected == "Home":
    st.title("🏠 Home Page")
elif selected == "Analytics":
    st.title("📊 Analytics Page")
elif selected == "Insights":
    st.title("💡 Insights Page")
elif selected == "About":
    st.title("ℹ️ About This App")
    st.markdown("""
    ### PhonePe Pulse Data Analysis and Visualization

    An interactive exploration of PhonePe’s transactions, users, and insurance data across India.  
    Built with **Streamlit & Plotly**, this dashboard highlights key trends and insights from official **PhonePe Pulse** datasets.

    **Highlights:**
    - Transaction value & volume trends across years, states, and quarters  
    - User growth patterns & mobile brand preferences  
    - Insurance adoption and regional penetration  

    **Tech Stack:** Python (Pandas, Plotly, Streamlit), MySQL, GeoJSON 
    
    **Developed By:** Senthilkumar.K
    """)

if selected == "Home":
    st.title("Dashboard Overview")

    tab1, tab2 = st.tabs(["Summary", "Updates"])

    with tab1:
        st.write("""

        The **PhonePe Transaction Dynamics Dashboard** is an interactive data visualization tool designed to monitor, analyze, and interpret digital payment trends on the PhonePe platform.  
        It empowers stakeholders to make data-driven decisions by presenting real-time and historical transaction insights in an intuitive format.

        ### 🔑 Key Features:
        - ✅ **Transaction Volume & Value Tracking** — Monitor total transactions over time by day, week, month, or quarter.
        - ✅ **Geographical Insights** — Visualize top-performing states, districts, and pin codes for granular analysis.
        - ✅ **Device & Category Breakdown** — Explore usage trends by device brands and transaction categories.
        - ✅ **User Registration Metrics** — Analyze new user sign-ups across different regions and timeframes.
        - ✅ **Filter by Time & Location** — Slice the data using dynamic filters for year, quarter, state, and more.
        - ✅ **Visual Dashboards** — Line charts, bar graphs, heatmaps, and choropleths for powerful storytelling.

        """)

    with tab2:
        st.write("PhonePe has acquired the GSPay platform from GupShup to enable UPI payments on feature phones, allowing users without internet to transact using QR codes, receive and send money through NFC-based UPI services, reaching over 240 million feature‑phone users in India.This marks a key step toward broadening digital payment adoption in underserved user segments.")

    st.markdown("""
    This is the **Home** tab of your interactive dashboard. Use the sidebar to navigate between sections like:
    - 📊 Analytics
    - ℹ️ About
    """)
    st.image("data:image/svg+xml;base64,PHN2ZyBpZD0iTGF5ZXJfMSIgZGF0YS1uYW1lPSJMYXllciAxIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzMzAgOTAiPjxkZWZzPjxzdHlsZT4uY2xzLTF7ZmlsbDojZmZmO30uY2xzLTJ7ZmlsbDojNWYyNDlmO308L3N0eWxlPjwvZGVmcz48Y2lyY2xlIGNsYXNzPSJjbHMtMSIgY3g9IjUwLjM0IiBjeT0iNDQuOTIiIHI9IjQyLjQyIi8+PHBhdGggY2xhc3M9ImNscy0yIiBkPSJNNTQuNSw1NC4xNmExMy4xNCwxMy4xNCwwLDAsMS00LjcxLjk0Yy0zLjg4LDAtNS42Mi0xLjk0LTUuNjItNi4yOVYzNy4zNkg1NC41Wm0xNS0yMC4zOGEzLDMsMCwwLDAtMy0zSDYwLjlsLTEzLTE1QTQuNzEsNC43MSwwLDAsMCw0MywxNC4zNmwtNC41LDEuMzNhLjk0Ljk0LDAsMCwwLS4zNywxLjU4TDUyLjI3LDMwLjgySDMwLjU3YTEuMTEsMS4xMSwwLDAsMC0xLjEzLDEuMTFWMzQuNGEzLDMsMCwwLDAsMywzaDMuMzFWNDguODNjMCw4LjU0LDQuNTUsMTMuNjUsMTIuMTksMTMuNjVhMTYuOTMsMTYuOTMsMCwwLDAsNi41Ni0xLjE3djcuNjNhMy43NSwzLjc1LDAsMCwwLDMuNzQsMy43NmgzLjNBMS40MSwxLjQxLDAsMCwwLDYzLDcxLjI5aDBWMzcuMzZoNS40NGExLjEyLDEuMTIsMCwwLDAsMS4xMS0xLjEzWiIvPjxwYXRoIGNsYXNzPSJjbHMtMSIgZD0iTTI4NCw0Mi42NWMwLTMuNzQtMi41MS01LjYzLTYuMjItNS42M2ExMS4yNywxMS4yNywwLDAsMC0zLjY4LjY1VjUzLjNhNi44Myw2LjgzLDAsMCwwLDMuNzQsMWMzLjY2LDAsNi4xNi0yLDYuMTYtNS42MVptOC41LDZjMCw3LjY4LTUuNzQsMTIuODQtMTMuMjcsMTIuODRhMTMuODMsMTMuODMsMCwwLDEtNS4xMy0uODlWNzEuMjZhMS40LDEuNCwwLDAsMS0xLjM5LDEuNDFoLTUuNTdhMS40MSwxLjQxLDAsMCwxLTEuNDEtMS40MWgwVjMzLjU0YTIuMTUsMi4xNSwwLDAsMSwxLjQzLTIsMzMuOSwzMy45LDAsMCwxLDEwLjg4LTEuOTJjOC41MSwwLDE0LjQ5LDUuMTcsMTQuNDksMTMuMlptLTE2MS43OC02YzAtMy43NC0yLjUyLTUuNjMtNi4yMy01LjYzYTExLjIxLDExLjIxLDAsMCwwLTMuNjcuNjVWNTMuM2E2Ljc0LDYuNzQsMCwwLDAsMy43NCwxYzMuNjYsMCw2LjE2LTIsNi4xNi01LjYxWm04LjQ5LDZjMCw3LjY4LTUuNzQsMTIuODQtMTMuMjYsMTIuODRhMTMuODMsMTMuODMsMCwwLDEtNS4xMy0uODlWNzEuMjZhMS40MSwxLjQxLDAsMCwxLTEuMzYsMS40MWgtNS42YTEuNDIsMS40MiwwLDAsMS0xLjQtMS40MVYzMy41NGEyLjEyLDIuMTIsMCwwLDEsMS40Mi0yLDM0LDM0LDAsMCwxLDEwLjg5LTEuOTJjOC41MSwwLDE0LjQ5LDUuMTcsMTQuNDksMTMuMlptNTIuOTEsNC4wOWMwLTMtMS43NS00LjY0LTQuODItNC42NHMtNC44NCwxLjczLTQuODQsNC42OHY4Ljg2YzAsMi45MiwxLjcxLDQuNTMsNC44Miw0LjUzczQuODItMS42MSw0LjgyLTQuNTNabTguMzcsMFY2MS42YzAsNy4yNi01LjA2LDExLjc4LTEzLjE5LDExLjc4cy0xMy4yMy00LjUxLTEzLjIzLTExLjc4VjUyLjc4YzAtNy4zNiw1LjA2LTEyLDEzLjIzLTEyczEzLjE2LDQuNjQsMTMuMTYsMTJabS0zNS44MSwxOS45aDMuMzZhMS40LDEuNCwwLDAsMCwxLjQyLTEuMzdWNTMuNjhjMC04LTQuMy0xMi44NS0xMS41LTEyLjg1YTE2LjQsMTYuNCwwLDAsMC01Ljg5LDFWMzMuMTRhMy41MywzLjUzLDAsMCwwLTMuNTItMy41NGgtMy4zMmExLjQxLDEuNDEsMCwwLDAtMS40MiwxLjRoMFY3MS4yNmExLjQxLDEuNDEsMCwwLDAsMS40MSwxLjQxaDUuNDNhMS40MSwxLjQxLDAsMCwwLDEuNDEtMS40MWgwVjQ4Ljg3YTExLDExLDAsMCwxLDQuMDgtLjc5YzMuNDQsMCw1LDEuNzMsNSw1LjYxVjY5LjE1YTMuNTYsMy41NiwwLDAsMCwzLjU0LDMuNTNabTEzOS41Ny0xOGg5LjA3VjUyLjI3YzAtMy0xLjY2LTQuNjUtNC41NC00LjY1cy00LjUzLDEuNjYtNC41Myw0LjY1djIuMzhabS4xOCw1LjJoLS4xOFY2MmMwLDIuODgsMS44Myw0LjUzLDUsNC41M2ExMy44OCwxMy44OCwwLDAsMCw2Ljg5LTEuODQsMS40LDEuNCwwLDAsMSwuNzUtLjE3LDEuMzksMS4zOSwwLDAsMSwxLC41bC44MywxYTMuNTksMy41OSwwLDAsMSwuOTMsMi40NkEzLjMxLDMuMzEsMCwwLDEsMzE4LDcxLjMxLDE4LjU5LDE4LjU5LDAsMCwxLDMwOSw3My40MmExNC41MywxNC41MywwLDAsMS05LjI2LTIuODgsMTAuNzMsMTAuNzMsMCwwLDEtMy44LTguNjZ2LTkuMmMwLTcuNDIsNC44Mi0xMS44MywxMi45MS0xMS44Myw3Ljg4LDAsMTIuMzgsNC4zMiwxMi4zOCwxMS44M3Y1Ljc3YTEuNCwxLjQsMCwwLDEtMS4zOSwxLjQxSDMwNC41Wm0tNjAuNTctNS4ySDI1M1Y1Mi4yN2MwLTMtMS42Ni00LjY1LTQuNTQtNC42NXMtNC41NCwxLjY2LTQuNTQsNC42NXYyLjM4Wm0uMTksNS4yaC0uMTlWNjJjMCwyLjg4LDEuODQsNC41Myw1LDQuNTNhMTMuODUsMTMuODUsMCwwLDAsNi44OC0xLjg0LDEuNTQsMS41NCwwLDAsMSwuNzYtLjE3LDEuMzksMS4zOSwwLDAsMSwxLC41bC44MywxYTMuNTQsMy41NCwwLDAsMSwuOTIsMi40NiwzLjI4LDMuMjgsMCwwLDEtMS43MywyLjgzLDE4LjU5LDE4LjU5LDAsMCwxLTguOTUsMi4xMSwxNC40NiwxNC40NiwwLDAsMS05LjI2LTIuODgsMTAuNzMsMTAuNzMsMCwwLDEtMy44LTguNjZ2LTkuMmMwLTcuNDIsNC44Mi0xMS44MywxMi45LTExLjgzLDcuODksMCwxMi4zOSw0LjMyLDEyLjM5LDExLjgzdjUuNzdhMS40LDEuNCwwLDAsMS0xLjM5LDEuNDFIMjQ0Wm0tMjEuNDEsOS4zVjUzLjc0YzAtMy44OC0xLjUyLTUuNi00LjkzLTUuNmExNC4yMywxNC4yMywwLDAsMC00LjE1LjU2VjcxLjI3YTEuMzksMS4zOSwwLDAsMS0xLjM3LDEuNDFoLTUuNDZhMS40LDEuNCwwLDAsMS0xLjQxLTEuMzlWNDQuODRhMi4xOCwyLjE4LDAsMCwxLDEuMzYtMiwzMi44MiwzMi44MiwwLDAsMSwxMS0yYzguNTQsMCwxMy4yMyw0LjU4LDEzLjIzLDEyLjlWNzEuMjdhMS4zOSwxLjM5LDAsMCwxLTEuMzcsMS40MWgtMy40YTMuNTMsMy41MywwLDAsMS0zLjUtMy41M1oiLz48L3N2Zz4=", width=300)

    st.subheader("Get Started")
    st.write("Select a tab on the left to begin exploring the data.")

    st.markdown(
    "<style> .big-font { font-size:24px; font-weight: bold; } </style>",
    unsafe_allow_html=True,
)

if selected == "Analytics":

    tab1, tab2, tab3= st.tabs(["Aggregated Analysis", "Map Analysis", "Top Analysis"])

    st.sidebar.header("🔍 Filter Options")
    years_list = [2018, 2019, 2020, 2021, 2022, 2023 ,2024]
    states = st.sidebar.multiselect("Select States", options=sorted(df['State'].unique()), default=None)
    years = st.sidebar.multiselect("Select Years", options=years_list, default=None)
    quarter = st.sidebar.multiselect("Select Quarter", options=sorted(df['Quarter'].unique()), default=None)


    # # Apply filters
    filtered_df = df.copy()
    filtered_df1 = df1.copy()
    filtered_df2= df2.copy()
    filtered_df3= df3.copy()
    filtered_df4= df4.copy()
    filtered_df5= df5.copy()
    filtered_df6= df6.copy()
    filtered_df7= df7.copy()
    filtered_df8= df8.copy()
    filtered_df9= df9.copy()
    filtered_df10= df10.copy()
    filtered_df11= df11.copy()
    if states:
        filtered_df = filtered_df[filtered_df['State'].isin(states)]
    if years:
        filtered_df = filtered_df[filtered_df['Year'].isin(years)]
    if quarter:
        filtered_df = filtered_df[filtered_df['Quarter'].isin(quarter)]

    if states:
        filtered_df1 = filtered_df1[filtered_df1['State'].isin(states)]
    if years:
        filtered_df1 = filtered_df1[filtered_df1['Year'].isin(years)]
    if quarter:
        filtered_df1 = filtered_df1[filtered_df1['Quarter'].isin(quarter)]

    if states:
        filtered_df2 = filtered_df2[filtered_df2['State'].isin(states)]
    if years:
        filtered_df2 = filtered_df2[filtered_df2['Year'].isin(years)]
    if quarter:
        filtered_df2 = filtered_df2[filtered_df2['Quarter'].isin(quarter)]

    if states:
        filtered_df3 = filtered_df3[filtered_df3['State'].isin(states)]
    if years:
        filtered_df3 = filtered_df3[filtered_df3['Year'].isin(years)]
    if quarter:
        filtered_df3 = filtered_df3[filtered_df3['Quarter'].isin(quarter)]

    if states:
        filtered_df4 = filtered_df4[filtered_df4['State'].isin(states)]
    if years:
        filtered_df4 = filtered_df4[filtered_df4['Year'].isin(years)]
    if quarter:
        filtered_df4 = filtered_df4[filtered_df4['Quarter'].isin(quarter)]

    if states:
        filtered_df5 = filtered_df5[filtered_df5['State'].isin(states)]
    if years:
        filtered_df5 = filtered_df5[filtered_df5['Year'].isin(years)]
    if quarter:
        filtered_df5 = filtered_df5[filtered_df5['Quarter'].isin(quarter)]

    if states:
        filtered_df6 = filtered_df6[filtered_df6['State'].isin(states)]
    if years:
        filtered_df6 = filtered_df6[filtered_df6['Year'].isin(years)]
    if quarter:
        filtered_df6 = filtered_df6[filtered_df6['Quarter'].isin(quarter)]


    if states:
        filtered_df7 = filtered_df7[filtered_df7['State'].isin(states)]

    if years:
        filtered_df7 = filtered_df7[filtered_df7['Year'].isin(years)]
    if quarter:
        filtered_df7 = filtered_df7[filtered_df7['Quarter'].isin(quarter)]

    if states:
        filtered_df8 = filtered_df8[filtered_df8['State'].isin(states)]
    if years:
        filtered_df8 = filtered_df8[filtered_df8['Year'].isin(years)]
    if quarter:
        filtered_df8 = filtered_df8[filtered_df8['Quarter'].isin(quarter)]

    if states:
        filtered_df9 = filtered_df9[filtered_df9['State'].isin(states)]
    if years:
        filtered_df9 = filtered_df9[filtered_df9['Year'].isin(years)]
    if quarter:
        filtered_df9 = filtered_df9[filtered_df9['Quarter'].isin(quarter)]

    if states:
        filtered_df10 = filtered_df10[filtered_df10['State'].isin(states)]
    if years:
        filtered_df10 = filtered_df10[filtered_df10['Year'].isin(years)]
    if quarter:
        filtered_df10 = filtered_df10[filtered_df10['Quarter'].isin(quarter)]

    if states:
        filtered_df11 = filtered_df11[filtered_df11['State'].isin(states)]
    if years:
        filtered_df11 = filtered_df11[filtered_df11['Year'].isin(years)]
    if quarter:
        filtered_df11 = filtered_df11[filtered_df11['Quarter'].isin(quarter)]

    # Aggregate
    summary = (
        filtered_df.groupby(['State', 'Year', 'Quarter'])
        .agg(Total_Transactions=('Transaction_count', 'sum'),
            Total_Amount=('Transaction_amount', 'sum'))
        .reset_index()
    )

    # Aggregate
    summary1 = (
        filtered_df1.groupby(['State', 'Year', 'Quarter'])
        .agg(Total_Transactions=('Transaction_count', 'sum'),
            Total_Amount=('Transaction_amount', 'sum'))
        .reset_index()
    )

    # Aggregate
    summary2 = (
        filtered_df2.groupby(['State', 'Year', 'Quarter'])
        .agg(User_brand=('User_brand_type','count'),
            Users_Count=('Users_count', 'sum'))
        .reset_index()
    )

    # Map_ins
    summary3 = (
        filtered_df3.groupby(['State', 'Year', 'Quarter'])
        .agg(Total_Transactions=('Transaction_count', 'sum'),
            Total_Amount=('Transaction_amount', 'sum'))
        .reset_index()
    )

    # Map_user
    summary4 = (
        filtered_df4.groupby(['State', 'Year', 'Quarter'])
        .agg(Regd_User=('RegisteredUser', 'sum'),
            App_opens=('AppOpens', 'sum'))
        .reset_index()
    )

    # Map_trans
    summary5 = (
        filtered_df5.groupby(['State', 'Year', 'Quarter'])
        .agg(Total_Transactions=('Transaction_count', 'sum'),
            Total_Amount=('Transaction_amount', 'sum'))
        .reset_index()
    )


    # Top_ins
    summary6 = (
        filtered_df6.groupby(['State', 'Year', 'Quarter'])
        .agg(Total_Transactions=('Transaction_count', 'sum'),
            Total_Amount=('Transaction_amount', 'sum'))
        .reset_index()
    )

    # Top_user
    summary7 = (
        filtered_df7.groupby(['State', 'Year', 'Quarter'])
        .agg(Regd_User=('RegisteredUser', 'sum'))
        .reset_index()
    )

    # Top_Trans
    summary8 = (
        filtered_df8.groupby(['State', 'Year', 'Quarter'])
        .agg(Total_Transactions=('Transaction_count', 'sum'),
            Total_Amount=('Transaction_amount', 'sum'))
        .reset_index()
    )

    # Top_Dist_ins
    summary9 = (
        filtered_df9.groupby(['State', 'Year', 'Quarter', 'Dist_Name'])
        .agg(Total_Transactions=('Transaction_count', 'sum'),
            Total_Amount=('Transaction_amount', 'sum'))
        .reset_index()
    )

    # Top_Dist_user
    summary10 = (
        filtered_df10.groupby(['State', 'Year', 'Quarter','Dist_Name'])
        .agg(Regd_User=('RegisteredUser', 'sum'))
        .reset_index()
    )


    with tab1:
        method = st.radio("**Select the Analysis Method**",["Insurance Analysis", "Transaction Analysis", "User Analysis"])
        if method == "Insurance Analysis":   
            
            # KPI Metrics
            st.subheader("📌 Key Metrics")
            col1, col2 = st.columns(2)
            col1.metric("Total Transactions", f"{filtered_df['Transaction_count'].sum():}")
            col2.metric("Total Amount", f"₹{filtered_df['Transaction_amount'].sum():,.2f}")


            # Time-series chart
            st.subheader("📈 Transaction Trends Over Time")
            time_series = (
                filtered_df.groupby(['State','Year', 'Quarter'])
                .agg(Total_Transactions=('Transaction_count', 'sum'),
                    Total_Amount=('Transaction_amount', 'sum'))
                .reset_index()
            )

            col1, col2 = st.columns(2)
            with col1:

                time_series['Quarter_Label'] = time_series['Year'].astype(str) + ' Q' + time_series['Quarter'].astype(str)
                fig1 = px.bar(time_series, x='State', y='Total_Amount',
                        title="Total Transaction Value Over Time", color='Year',text='Total_Amount', width=400, height=600)
                st.plotly_chart(fig1, use_container_width=True, key="chart1")

            with col2:
                fig2 = px.bar(time_series, x='State', y='Total_Transactions',
                        title="Total Transaction Count Over Time", color='Year',text='Total_Transactions', width=400, height=600)
                st.plotly_chart(fig2, use_container_width=True, key="chart2")


            st.subheader("📈 Transaction Maps Over Time")


            col1, = st.columns(1)
            with col1:
                url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
                response= requests.get(url)
                data1= json.loads(response.content)
                states_name_tra= [feature["properties"]["ST_NM"] for feature in data1["features"]]
                states_name_tra.sort()
                years_label = ", ".join(map(str, sorted(summary["Year"].unique())))
                fig_india_1= px.choropleth(summary, geojson= data1, locations= "State", featureidkey= "properties.ST_NM",
                                            color= "Total_Transactions", color_continuous_scale= "Sunsetdark",
                                            range_color= (summary["Total_Transactions"].min(),summary["Total_Transactions"].max()),
                                            hover_name= "State",title = f"{years_label} TRANSACTION COUNT",
                                            fitbounds= "locations",width =400, height= 600)
                fig_india_1.update_geos(visible =False)
                    
                st.plotly_chart(fig_india_1, use_container_width=True, key="chart3")


                fig_india_2= px.choropleth(summary, geojson= data1, locations= "State", featureidkey= "properties.ST_NM",
                                            color= "Total_Amount", color_continuous_scale= "Sunsetdark",
                                            range_color= (summary["Total_Amount"].min(),summary["Total_Amount"].max()),
                                            hover_name= "State",title = f"{years_label} TRANSACTION AMOUNT",
                                            fitbounds= "locations",width =400, height= 600)
                fig_india_2.update_geos(visible =False)
                    
                st.plotly_chart(fig_india_2, use_container_width=True, key="chart4")
            
        if method == "Transaction Analysis":   
            
                st.subheader("📌 Key Metrics")
                col1, col2 = st.columns(2)
                col1.metric("Total Transactions", f"{filtered_df1['Transaction_count'].sum():}")
                col2.metric("Total Amount", f"₹{filtered_df1['Transaction_amount'].sum():,.2f}")

                st.subheader("📈 Transaction Trends Over Time")
                time_series = (
                    filtered_df1.groupby(['State','Year', 'Quarter'])
                    .agg(Total_Transactions=('Transaction_count', 'sum'),
                        Total_Amount=('Transaction_amount', 'sum'))
                    .reset_index()
                )

                col1, col2 = st.columns(2)
                with col1:

                    time_series['Quarter_Label'] = time_series['Year'].astype(str) + ' Q' + time_series['Quarter'].astype(str)
                    fig1 = px.bar(time_series, x='State', y='Total_Amount',
                            title="Total Transaction Value Over Time", color='Year',text='Total_Amount', width=400, height=600)
                    st.plotly_chart(fig1, use_container_width=True, key="chart5")

                with col2:
                    fig2 = px.bar(time_series, x='State', y='Total_Transactions',
                            title="Total Transaction Count Over Time", color='Year',text='Total_Transactions', width=400, height=600)
                    st.plotly_chart(fig2, use_container_width=True, key="chart6")


                st.subheader("📈 Transaction Maps Over Time")


                col1, = st.columns(1)
                with col1:
                    url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
                    response= requests.get(url)
                    data1= json.loads(response.content)
                    states_name_tra= [feature["properties"]["ST_NM"] for feature in data1["features"]]
                    states_name_tra.sort()
                    years_label = ", ".join(map(str, sorted(summary["Year"].unique())))
                    fig_india_1= px.choropleth(summary1, geojson= data1, locations= "State", featureidkey= "properties.ST_NM",
                                                color= "Total_Transactions", color_continuous_scale= "Sunsetdark",
                                                range_color= (summary1["Total_Transactions"].min(),summary1["Total_Transactions"].max()),
                                                hover_name= "State",title = f"{years_label} TRANSACTION COUNT",
                                                fitbounds= "locations",width =400, height= 600)
                    fig_india_1.update_geos(visible =False)
                        
                    st.plotly_chart(fig_india_1, use_container_width=True, key="chart7")


                    fig_india_2= px.choropleth(summary1, geojson= data1, locations= "State", featureidkey= "properties.ST_NM",
                                                color= "Total_Amount", color_continuous_scale= "Sunsetdark",
                                                range_color= (summary1["Total_Amount"].min(),summary1["Total_Amount"].max()),
                                                hover_name= "State",title = f"{years_label} TRANSACTION AMOUNT",
                                                fitbounds= "locations",width =400, height= 600)
                    fig_india_2.update_geos(visible =False)
                        
                    st.plotly_chart(fig_india_2, use_container_width=True, key="chart8")
        if method == "User Analysis":   
            
            st.subheader("📌 Key Metrics")
            col1, col2 = st.columns(2)
            with col1:
                st.write("### 📱 User Brands ")
                for brand in filtered_df2['User_brand_type'].unique():
                    st.write(brand)
            col2.metric("User_Count", f"{filtered_df2['Users_count'].sum():}")

            st.subheader("📈 User Trends Over Time")
            time_series = (
                filtered_df2.groupby(['State','Year', 'Quarter'])
                .agg(User_Brands=('User_brand_type', 'sum'),
                    User_Count=('Users_count', 'sum'))
                .reset_index()
            )

            col1, = st.columns(1)

            with col1:
                fig2 = px.bar(time_series, x='State', y='User_Count',
                        title="Total User Count Over Time", color='Year',text='User_Count', width=400, height=600)
                st.plotly_chart(fig2, use_container_width=True, key="chart9")


            st.subheader("📈 User Maps Over Time")


            col1, = st.columns(1)
            with col1:
                url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
                response= requests.get(url)
                data1= json.loads(response.content)
                states_name_tra= [feature["properties"]["ST_NM"] for feature in data1["features"]]
                states_name_tra.sort()
                years_label = ", ".join(map(str, sorted(summary["Year"].unique())))
                fig_india_2= px.choropleth(summary2, geojson= data1, locations= "State", featureidkey= "properties.ST_NM",
                                            color= "Users_Count", color_continuous_scale= "Sunsetdark",
                                            range_color= (summary2["Users_Count"].min(),summary2["Users_Count"].max()),
                                            hover_name= "State",title = f"{years_label} Users Count",
                                            fitbounds= "locations",width =400, height= 600)
                fig_india_2.update_geos(visible =False)
                    
                st.plotly_chart(fig_india_2, use_container_width=True, key="chart10")

    with tab2:
        method1 = st.radio("**Select the Analysis Method**",["Map Insurance Analysis", "Map Transaction Analysis", "Map User Analysis"],key="analysis_method_radio")
        if method1 == "Map Insurance Analysis":

            st.subheader("📌 Key Metrics")
            col1, col2 = st.columns(2)
            col1.metric("Total Transactions", f"{filtered_df3['Transaction_count'].sum():}")
            col2.metric("Total Amount", f"₹{filtered_df3['Transaction_amount'].sum():,.2f}")

            st.subheader("📈 Insurance Transaction Trends Over Time")
            time_series = (
                filtered_df3.groupby(['State','Year', 'Quarter'])
                .agg(Total_Transactions=('Transaction_count', 'sum'),
                    Total_Amount=('Transaction_amount', 'sum'))
                .reset_index()
            )

            col1, col2 = st.columns(2)
            with col1:

                time_series['Quarter_Label'] = time_series['Year'].astype(str) + ' Q' + time_series['Quarter'].astype(str)
                fig1 = px.bar(time_series, x='State', y='Total_Amount',
                        title="Total Insurance Transaction Value Over Time", color='Year',text='Total_Amount', width=400, height=600)
                st.plotly_chart(fig1, use_container_width=True, key="chart11")

            with col2:
                fig2 = px.bar(time_series, x='State', y='Total_Transactions',
                        title="Total Insurance Transaction Count Over Time", color='Year',text='Total_Transactions', width=400, height=600)
                st.plotly_chart(fig2, use_container_width=True, key="chart12")


            st.subheader("📈 Insurance Transaction Maps Over Time")


            col1, = st.columns(1)
            with col1:
                url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
                response= requests.get(url)
                data1= json.loads(response.content)
                states_name_tra= [feature["properties"]["ST_NM"] for feature in data1["features"]]
                states_name_tra.sort()
                years_label = ", ".join(map(str, sorted(summary["Year"].unique())))
                fig_india_1= px.choropleth(summary3, geojson= data1, locations= "State", featureidkey= "properties.ST_NM",
                                            color= "Total_Transactions", color_continuous_scale= "Sunsetdark",
                                            range_color= (summary3["Total_Transactions"].min(),summary3["Total_Transactions"].max()),
                                            hover_name= "State",title = f"{years_label} TRANSACTION COUNT",
                                            fitbounds= "locations",width =400, height= 600)
                fig_india_1.update_geos(visible =False)
                    
                st.plotly_chart(fig_india_1, use_container_width=True, key="chart13")


                fig_india_2= px.choropleth(summary3, geojson= data1, locations= "State", featureidkey= "properties.ST_NM",
                                            color= "Total_Amount", color_continuous_scale= "Sunsetdark",
                                            range_color= (summary3["Total_Amount"].min(),summary3["Total_Amount"].max()),
                                            hover_name= "State",title = f"{years_label} TRANSACTION AMOUNT",
                                            fitbounds= "locations",width =400, height= 600)
                fig_india_2.update_geos(visible =False)
                    
                st.plotly_chart(fig_india_2, use_container_width=True, key="chart14")

        if method1 == "Map User Analysis":

            st.subheader("📌 Key Metrics")
            col1, col2 = st.columns(2)
            col1.metric("Registered Users", f"{filtered_df4['RegisteredUser'].sum():}")
            col2.metric("App Opens Count", f"{filtered_df4['AppOpens'].sum():}")

            st.subheader("📈 User Trends Over Time")
            time_series = (
                filtered_df4.groupby(['State','Year', 'Quarter'])
                .agg(Regd_User=('RegisteredUser', 'sum'),
                    App_opens=('AppOpens', 'sum'))
                .reset_index()
            )

            col1,col2 = st.columns(2)

            with col1:
                fig2 = px.bar(time_series, x='State', y='Regd_User',
                        title="Total Registered Users Over Time", color='Year',text='Regd_User', width=400, height=600)
                st.plotly_chart(fig2, use_container_width=True, key="chart15")

            with col2:
                fig2 = px.bar(time_series, x='State', y='App_opens',
                        title="Total App Opens Count Over Time", color='Year',text='App_opens', width=400, height=600)
                st.plotly_chart(fig2, use_container_width=True, key="chart16")


            st.subheader("📈 Register User Maps Over Time")


            col1, = st.columns(1)
            with col1:
                url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
                response= requests.get(url)
                data1= json.loads(response.content)
                states_name_tra= [feature["properties"]["ST_NM"] for feature in data1["features"]]
                states_name_tra.sort()
                years_label = ", ".join(map(str, sorted(summary["Year"].unique())))
                fig_india_2= px.choropleth(summary4, geojson= data1, locations= "State", featureidkey= "properties.ST_NM",
                                            color= "Regd_User", color_continuous_scale= "Sunsetdark",
                                            range_color= (summary4["Regd_User"].min(),summary4["Regd_User"].max()),
                                            hover_name= "State",title = f"{years_label} Rigister Users Count",
                                            fitbounds= "locations",width =400, height= 600)
                fig_india_2.update_geos(visible =False)
                    
                st.plotly_chart(fig_india_2, use_container_width=True, key="chart17")

                fig_india_1= px.choropleth(summary4, geojson= data1, locations= "State", featureidkey= "properties.ST_NM",
                                            color= "App_opens", color_continuous_scale= "Sunsetdark",
                                            range_color= (summary4["App_opens"].min(),summary4["App_opens"].max()),
                                            hover_name= "State",title = f"{years_label} APP OPENS COUNT",
                                            fitbounds= "locations",width =400, height= 600)
                fig_india_1.update_geos(visible =False)
                    
                st.plotly_chart(fig_india_1, use_container_width=True, key="chart18")
        
        if method1 == "Map Transaction Analysis":

            st.subheader("📌 Key Metrics")
            col1, col2 = st.columns(2)
            col1.metric("Total Transactions", f"{filtered_df5['Transaction_count'].sum():}")
            col2.metric("Total Amount", f"₹{filtered_df5['Transaction_amount'].sum():,.2f}")

            st.subheader("📈 Transaction Trends Over Time")
            time_series = (
                filtered_df5.groupby(['State','Year', 'Quarter'])
                .agg(Total_Transactions=('Transaction_count', 'sum'),
                    Total_Amount=('Transaction_amount', 'sum'))
                .reset_index()
            )

            col1, col2 = st.columns(2)
            with col1:

                time_series['Quarter_Label'] = time_series['Year'].astype(str) + ' Q' + time_series['Quarter'].astype(str)
                fig1 = px.bar(time_series, x='State', y='Total_Amount',
                        title="Total Transaction Value Over Time", color='Year',text='Total_Amount', width=400, height=600)
                st.plotly_chart(fig1, use_container_width=True, key="chart19")

            with col2:
                fig2 = px.bar(time_series, x='State', y='Total_Transactions',
                        title="Total Transaction Count Over Time", color='Year',text='Total_Transactions', width=400, height=600)
                st.plotly_chart(fig2, use_container_width=True, key="chart20")


            st.subheader("📈 Transaction Maps Over Time")


            col1, = st.columns(1)
            with col1:
                url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
                response= requests.get(url)
                data1= json.loads(response.content)
                states_name_tra= [feature["properties"]["ST_NM"] for feature in data1["features"]]
                states_name_tra.sort()
                years_label = ", ".join(map(str, sorted(summary["Year"].unique())))
                fig_india_1= px.choropleth(summary5, geojson= data1, locations= "State", featureidkey= "properties.ST_NM",
                                            color= "Total_Transactions", color_continuous_scale= "Sunsetdark",
                                            range_color= (summary5["Total_Transactions"].min(),summary5["Total_Transactions"].max()),
                                            hover_name= "State",title = f"{years_label} TRANSACTION COUNT",
                                            fitbounds= "locations",width =400, height= 600)
                fig_india_1.update_geos(visible =False)
                    
                st.plotly_chart(fig_india_1, use_container_width=True, key="chart21")


                fig_india_2= px.choropleth(summary5, geojson= data1, locations= "State", featureidkey= "properties.ST_NM",
                                            color= "Total_Amount", color_continuous_scale= "Sunsetdark",
                                            range_color= (summary5["Total_Amount"].min(),summary5["Total_Amount"].max()),
                                            hover_name= "State",title = f"{years_label} TRANSACTION AMOUNT",
                                            fitbounds= "locations",width =400, height= 600)
                fig_india_2.update_geos(visible =False)
                    
                st.plotly_chart(fig_india_2, use_container_width=True, key="chart22")
    
    with tab3:
        method2 = st.radio("**Select the Analysis Method**",["Top Insurance Analysis", "Top Transaction Analysis", "Top User Analysis"],key="top_analysis_method_radio")
        if method2 == "Top Insurance Analysis":

            st.subheader("📌 Key Metrics")
            col1, col2 = st.columns(2)
            col1.metric("Total Transactions", f"{filtered_df6['Transaction_count'].sum():}")
            col2.metric("Total Amount", f"₹{filtered_df6['Transaction_amount'].sum():,.2f}")

            st.subheader("📈 Top Insurance Transaction Trends Over Time")
            time_series = (
                filtered_df6.groupby(['State','Year', 'Quarter'])
                .agg(Total_Transactions=('Transaction_count', 'sum'),
                    Total_Amount=('Transaction_amount', 'sum'))
                .reset_index()
            )

            col1, col2 = st.columns(2)
            with col1:

                time_series['Quarter_Label'] = time_series['Year'].astype(str) + ' Q' + time_series['Quarter'].astype(str)
                fig1 = px.bar(time_series, x='State', y='Total_Amount',
                        title="Total Insurance Transaction Value Over Time", color='Year',text='Total_Amount', width=400, height=600)
                st.plotly_chart(fig1, use_container_width=True, key="chart23")

            with col2:
                fig2 = px.bar(time_series, x='State', y='Total_Transactions',
                        title="Total Insurance Transaction Count Over Time", color='Year',text='Total_Transactions', width=400, height=600)
                st.plotly_chart(fig2, use_container_width=True, key="chart24")


            st.subheader("📈 Top Insurance Transaction Maps Over Time")


            col1, = st.columns(1)
            with col1:
                url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
                response= requests.get(url)
                data1= json.loads(response.content)
                states_name_tra= [feature["properties"]["ST_NM"] for feature in data1["features"]]
                states_name_tra.sort()
                years_label = ", ".join(map(str, sorted(summary["Year"].unique())))
                fig_india_1= px.choropleth(summary6, geojson= data1, locations= "State", featureidkey= "properties.ST_NM",
                                            color= "Total_Transactions", color_continuous_scale= "Sunsetdark",
                                            range_color= (summary6["Total_Transactions"].min(),summary6["Total_Transactions"].max()),
                                            hover_name= "State",title = f"{years_label} TRANSACTION COUNT",
                                            fitbounds= "locations",width =400, height= 600)
                fig_india_1.update_geos(visible =False)
                    
                st.plotly_chart(fig_india_1, use_container_width=True, key="chart25")


                fig_india_2= px.choropleth(summary6, geojson= data1, locations= "State", featureidkey= "properties.ST_NM",
                                            color= "Total_Amount", color_continuous_scale= "Sunsetdark",
                                            range_color= (summary6["Total_Amount"].min(),summary6["Total_Amount"].max()),
                                            hover_name= "State",title = f"{years_label} TRANSACTION AMOUNT",
                                            fitbounds= "locations",width =400, height= 600)
                fig_india_2.update_geos(visible =False)
                    
                st.plotly_chart(fig_india_2, use_container_width=True, key="chart26")

   
        if method2 == "Top User Analysis":

            st.subheader("📌 Key Metrics")
            col1, = st.columns(1)
            col1.metric("Registered Users", f"{filtered_df7['RegisteredUser'].sum():}")

            st.subheader("📈 Top Users Trends Over Time")
            time_series = (
                filtered_df7.groupby(['State','Year', 'Quarter'])
                .agg(Regd_User=('RegisteredUser', 'sum'))
                .reset_index()
            )

            col1,  = st.columns(1)
            with col1:

                time_series['Quarter_Label'] = time_series['Year'].astype(str) + ' Q' + time_series['Quarter'].astype(str)
                fig1 = px.bar(time_series, x='State', y='Regd_User',
                        title="Total Users Over Time", color='Year',text='Regd_User', width=400, height=600)
                st.plotly_chart(fig1, use_container_width=True, key="chart27")

            
            st.subheader("📈 Top Users Maps Over Time")


            col1, = st.columns(1)
            with col1:
                url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
                response= requests.get(url)
                data1= json.loads(response.content)
                states_name_tra= [feature["properties"]["ST_NM"] for feature in data1["features"]]
                states_name_tra.sort()
                years_label = ", ".join(map(str, sorted(summary["Year"].unique())))
                fig_india_1= px.choropleth(summary7, geojson= data1, locations= "State", featureidkey= "properties.ST_NM",
                                            color= "Regd_User", color_continuous_scale= "Sunsetdark",
                                            range_color= (summary7["Regd_User"].min(),summary7["Regd_User"].max()),
                                            hover_name= "State",title = f"{years_label} USERS COUNT",
                                            fitbounds= "locations",width =400, height= 600)
                fig_india_1.update_geos(visible =False)
                    
                st.plotly_chart(fig_india_1, use_container_width=True, key="chart28")


        if method2 == "Top Transaction Analysis":

            st.subheader("📌 Key Metrics")
            col1, col2 = st.columns(2)
            col1.metric("Total Transactions", f"{filtered_df8['Transaction_count'].sum():}")
            col2.metric("Total Amount", f"₹{filtered_df8['Transaction_amount'].sum():,.2f}")

            st.subheader("📈 Top Transaction Trends Over Time")
            time_series = (
                filtered_df8.groupby(['State','Year', 'Quarter'])
                .agg(Total_Transactions=('Transaction_count', 'sum'),
                    Total_Amount=('Transaction_amount', 'sum'))
                .reset_index()
            )

            col1, col2 = st.columns(2)
            with col1:

                time_series['Quarter_Label'] = time_series['Year'].astype(str) + ' Q' + time_series['Quarter'].astype(str)
                fig1 = px.bar(time_series, x='State', y='Total_Amount',
                        title="Total Transaction Value Over Time", color='Year',text='Total_Amount', width=400, height=600)
                st.plotly_chart(fig1, use_container_width=True, key="chart29")

            with col2:
                fig2 = px.bar(time_series, x='State', y='Total_Transactions',
                        title="Total Transaction Count Over Time", color='Year',text='Total_Transactions', width=400, height=600)
                st.plotly_chart(fig2, use_container_width=True, key="chart30")


            st.subheader("📈 Top Transaction Maps Over Time")


            col1, = st.columns(1)
            with col1:
                url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
                response= requests.get(url)
                data1= json.loads(response.content)
                states_name_tra= [feature["properties"]["ST_NM"] for feature in data1["features"]]
                states_name_tra.sort()
                years_label = ", ".join(map(str, sorted(summary["Year"].unique())))
                fig_india_1= px.choropleth(summary8, geojson= data1, locations= "State", featureidkey= "properties.ST_NM",
                                            color= "Total_Transactions", color_continuous_scale= "Sunsetdark",
                                            range_color= (summary8["Total_Transactions"].min(),summary8["Total_Transactions"].max()),
                                            hover_name= "State",title = f"{years_label} TRANSACTION COUNT",
                                            fitbounds= "locations",width =400, height= 600)
                fig_india_1.update_geos(visible =False)
                    
                st.plotly_chart(fig_india_1, use_container_width=True, key="chart31")


                fig_india_2= px.choropleth(summary8, geojson= data1, locations= "State", featureidkey= "properties.ST_NM",
                                            color= "Total_Amount", color_continuous_scale= "Sunsetdark",
                                            range_color= (summary8["Total_Amount"].min(),summary8["Total_Amount"].max()),
                                            hover_name= "State",title = f"{years_label} TRANSACTION AMOUNT",
                                            fitbounds= "locations",width =400, height= 600)
                fig_india_2.update_geos(visible =False)
                    
                st.plotly_chart(fig_india_2, use_container_width=True, key="chart32")

def q1():
    st.sidebar.header("🔍 Filter Options")
    years = st.sidebar.multiselect("Select Years", options=sorted(df8['Year'].unique()), default=None)
    quarter = st.sidebar.multiselect("Select Quarter", options=sorted(df8['Quarter'].unique()), default=None)
    a=df8[["State","Year","Quarter","Transaction_count","Transaction_amount"]]
    if years:
        a = a[a['Year'].isin(years)]
    if quarter:
        a = a[a['Quarter'].isin(quarter)]
    a1=a.groupby("State")[["Transaction_amount", "Transaction_count"]].sum().sort_values(by="Transaction_amount", ascending=False)
    a2= pd.DataFrame(a1).reset_index().head(10)
    # Format years 
    year_label = ", ".join(str(int(y)) for y in years) if years else "All Years"
    # Format years 
    qt_label ="Quarter " + ", ".join(str(int(z)) for z in quarter) if quarter else " "

    a2_melt = a2.melt( id_vars="State", value_vars=["Transaction_amount", "Transaction_count"], 
    var_name="Metric", value_name="Value")

    fig_top_state= px.bar(a2_melt, x="State", y="Value", color="Metric", barmode="group", 
    title=f"HIGHEST TRANSACTION AMOUNT & STATES {year_label} : {qt_label}",
    color_discrete_map={"Transaction_amount": "lightblue","Transaction_count": "white"})  
    return st.plotly_chart(fig_top_state)

def q2():
    st.sidebar.header("🔍 Filter Options")
    years = st.sidebar.multiselect("Select Years", options=sorted(df2['Year'].unique()), default=None)
    quarter = st.sidebar.multiselect("Select Quarter", options=sorted(df2['Quarter'].unique()), default=None)
    b=df2[["Year","Quarter","User_brand_type","Users_count"]]
    if years:
        b = b[b['Year'].isin(years)]
    if quarter:
        b = b[b['Quarter'].isin(quarter)]
    b1=b.groupby("User_brand_type")["Users_count"].sum().sort_values(ascending=False)
    b2= pd.DataFrame(b1).reset_index().head(10)

    year_label = ", ".join(str(int(y)) for y in years) if years else "All Years"
    qt_label ="Quarter " + ", ".join(str(int(a)) for a in quarter) if quarter else " "

    fig_brands= px.pie(b2, values="Users_count", names = "User_brand_type" , color_discrete_sequence=px.colors.sequential.Rainbow_r,
                       title= f"Top 10 device brands are dominant in {year_label} : {qt_label}")
    return st.plotly_chart(fig_brands)

def q3():
    st.sidebar.header("🔍 Filter Options")
    years = st.sidebar.multiselect("Select Years", options=sorted(df6['Year'].unique()), default=None)
    quarter = st.sidebar.multiselect("Select Quarter", options=sorted(df6['Quarter'].unique()), default=None)
    c=df6[["State","Year","Quarter","Transaction_count","Transaction_amount"]]
    if years:
        c = c[c['Year'].isin(years)]
    if quarter:
        c = c[c['Quarter'].isin(quarter)]
    c1=c.groupby("State")[["Transaction_amount", "Transaction_count"]].sum().sort_values(by="Transaction_amount", ascending=False)
    c2= pd.DataFrame(c1).reset_index().head(10)

    year_label = ", ".join(str(int(y)) for y in years) if years else "All Years"
    qt_label ="Quarter " + ", ".join(str(int(z)) for z in quarter) if quarter else " "

    c2_melt = c2.melt( id_vars="State", value_vars=["Transaction_amount", "Transaction_count"], 
    var_name="Metric", value_name="Value")

    fig_ins_state= px.bar(c2_melt, x="State", y="Value", color="Metric", barmode="group", 
    title=f"Top 10 State-level insurance insights for PhonePe’s strategic growth {year_label} : {qt_label}",
    color_discrete_map={"Transaction_amount": "lightyellow","Transaction_count": "white"})  
    return st.plotly_chart(fig_ins_state)

def q4():
    st.sidebar.header("🔍 Filter Options")
    years = st.sidebar.multiselect("Select Years", options=sorted(df8['Year'].unique()), default=None)
    quarter = st.sidebar.multiselect("Select Quarter", options=sorted(df8['Quarter'].unique()), default=None)
    d=df8[["State","Year","Quarter","Transaction_count","Transaction_amount"]]
    if years:
        d = d[d['Year'].isin(years)]
    if quarter:
        d = d[d['Quarter'].isin(quarter)]
    d1=d.groupby("State")[["Transaction_amount", "Transaction_count"]].sum().sort_values(by="Transaction_amount", ascending=False)
    d2= pd.DataFrame(d1).reset_index().head(10)

    year_label = ", ".join(str(int(y)) for y in years) if years else "All Years"
    qt_label ="Quarter " + ", ".join(str(int(z)) for z in quarter) if quarter else " "

    d2_melt = d2.melt( id_vars="State", value_vars=["Transaction_amount", "Transaction_count"], 
    var_name="Metric", value_name="Value")

    fig_top_trans_state= px.bar(d2_melt, x="State", y="Value", color="Metric", barmode="group", 
    title=f"States With Highest Trasaction Amount {year_label} : {qt_label}",
    color_discrete_map={"Transaction_amount": "lightblue","Transaction_count": "white"})  
    return st.plotly_chart(fig_top_trans_state)

def q5():
    st.sidebar.header("🔍 Filter Options")
    years = st.sidebar.multiselect("Select Years", options=sorted(df7['Year'].unique()), default=None)
    quarter = st.sidebar.multiselect("Select Quarter", options=sorted(df7['Quarter'].unique()), default=None)
    e=df7[["State","Year","Quarter","RegisteredUser"]]
    if years:
        e = e[e['Year'].isin(years)]
    if quarter:
        e = e[e['Quarter'].isin(quarter)]
    e1=e.groupby("State")["RegisteredUser"].sum().sort_values(ascending=False)
    e2= pd.DataFrame(e1).reset_index().head(10)

    year_label = ", ".join(str(int(y)) for y in years) if years else "All Years" 
    qt_label ="Quarter " + ", ".join(str(int(z)) for z in quarter) if quarter else " "

    fig_top_user_state= px.bar(e2, x= "State", y= "RegisteredUser",title= f"Top 10 States With Phonepe users in {year_label} : {qt_label}", color_discrete_sequence= px.colors.sequential.Purples) 
    return st.plotly_chart(fig_top_user_state) 

def q6():
    st.sidebar.header("🔍 Filter Options")
    years = st.sidebar.multiselect("Select Years", options=sorted(df['Year'].unique()), default=None)
    quarter = st.sidebar.multiselect("Select Quarter", options=sorted(df['Quarter'].unique()), default=None)
    ins_f=df[["State","Year","Quarter","Transaction_count","Transaction_amount"]]
    if years:
        ins_f = ins_f[ins_f['Year'].isin(years)]   
    if quarter:
        ins_f = ins_f[ins_f['Quarter'].isin(quarter)]   
    
    ins_f=pd.DataFrame(ins_f)

    f1=ins_f.groupby("State")[["Transaction_amount", "Transaction_count"]].sum().sort_values(by="Transaction_amount", ascending=True)
    f2= pd.DataFrame(f1).reset_index().head(10)

    f3=ins_f.groupby("State")[["Transaction_amount", "Transaction_count"]].sum().sort_values(by="Transaction_amount", ascending=False)
    f4= pd.DataFrame(f3).reset_index().head(10)

    year_label = ", ".join(str(int(y)) for y in years) if years else "All Years"
    qt_label ="Quarter " + ", ".join(str(int(z)) for z in quarter) if quarter else " "

    f2_melt = f2.melt( id_vars="State", value_vars=["Transaction_amount", "Transaction_count"], 
    var_name="Metric", value_name="Value")

    f4_melt = f4.melt( id_vars="State", value_vars=["Transaction_amount", "Transaction_count"], 
    var_name="Metric", value_name="Value")

    fig_low_ins_state= px.bar(f2_melt, x="State", y="Value", color="Metric", barmode="group", 
    title=f"10 States Low insurance adoption {year_label} : {qt_label}",
    color_discrete_map={"Transaction_amount": "lightblue","Transaction_count": "white"}) 

    fig_high_ins_state= px.bar(f4_melt, x="State", y="Value", color="Metric", barmode="group", 
    title=f"10 States High insurance adoption {year_label} : {qt_label}",
    color_discrete_map={"Transaction_amount": "lightblue","Transaction_count": "white"})  
    
    col1, = st.columns(1)

    with col1:
        st.plotly_chart(fig_low_ins_state, use_container_width=True)

    col2, = st.columns(1)

    with col2:
        st.plotly_chart(fig_high_ins_state, use_container_width=True)


def q7():
    st.sidebar.header("🔍 Filter Options")
    years = st.sidebar.multiselect("Select Years", options=sorted(df11['Year'].unique()), default=None)
    quarter = st.sidebar.multiselect("Select Quarter", options=sorted(df11['Quarter'].unique()), default=None)
    g=df11[["State","Year","Quarter","Dist_Name","Transaction_count","Transaction_amount"]]
    if years:
        g = g[g['Year'].isin(years)]
    if quarter:
        g = g[g['Quarter'].isin(quarter)]
    g1=g.groupby(["State", "Dist_Name"])[["Transaction_amount", "Transaction_count"]].sum().sort_values(by="Transaction_amount", ascending=False)
    g2= pd.DataFrame(g1).reset_index().head(10)

    year_label = ", ".join(str(int(y)) for y in years) if years else "All Years"
    qt_label ="Quarter " + ", ".join(str(int(z)) for z in quarter) if quarter else " "

    g2_melt = g2.melt( id_vars="State", value_vars=["Transaction_amount", "Transaction_count"], 
    var_name="Metric", value_name="Value")

    g3_melt = g2.melt( id_vars="Dist_Name", value_vars=["Transaction_amount", "Transaction_count"], 
    var_name="Metric", value_name="Value")

    fig_trans_state= px.bar(g2_melt, x="State", y="Value", color="Metric", barmode="group", 
    title=f"Which States contribute the highest to overall transaction volume and value on PhonePe {year_label} : {qt_label}",
    color_discrete_map={"Transaction_amount": "lightblue","Transaction_count": "white"})  

    fig_trans_dist= px.bar(g3_melt, x="Dist_Name", y="Value", color="Metric", barmode="group", 
    title=f"Which Districts contribute the highest to overall transaction volume and value on PhonePe {year_label} : {qt_label}",
    color_discrete_map={"Transaction_amount": "lightblue","Transaction_count": "white"})

    col1, = st.columns(1)

    with col1:
        st.plotly_chart(fig_trans_state, use_container_width=True)

    col2, = st.columns(1)

    with col2:
        st.plotly_chart(fig_trans_dist, use_container_width=True)

def q8():
    st.sidebar.header("🔍 Filter Options")
    years = st.sidebar.multiselect("Select Years", options=sorted(df10['Year'].unique()), default=None)
    quarter = st.sidebar.multiselect("Select Quarter", options=sorted(df10['Quarter'].unique()), default=None)
    h=df10[["State","Year","Quarter","Dist_Name","RegisteredUser"]]
    i=df7[["State","Year","Quarter","Pincodes","RegisteredUser"]]
    if years:
        h = h[h['Year'].isin(years)]
    if quarter:
        h = h[h['Quarter'].isin(quarter)]

    if years:
        i = i[i['Year'].isin(years)]
    if quarter:
        i = i[i['Quarter'].isin(quarter)]


    h1=h.groupby(["State", "Dist_Name"])["RegisteredUser"].sum().sort_values(ascending=False)
    h2= pd.DataFrame(h1).reset_index().head(10)

    i1=i.groupby(["State", "Pincodes"])["RegisteredUser"].sum().sort_values(ascending=False)
    i2= pd.DataFrame(i1).reset_index().head(10)
    
    year_label = ", ".join(str(int(y)) for y in years) if years else "All Years"
    qt_label ="Quarter " + ", ".join(str(int(z)) for z in quarter) if quarter else " "

    fig_user_state= px.bar(h2, x= "State", y= "RegisteredUser",title= f"Top 10 States With Phonepe users in {year_label} : {qt_label}", 
                               color_discrete_sequence= px.colors.sequential.Purples)
    
    fig_user_dist= px.bar(h2, x= "Dist_Name", y= "RegisteredUser",title= f"Top 10 Districts With Phonepe users in {year_label} : {qt_label}", 
                               color_discrete_sequence= px.colors.sequential.Purples)
    
    
    fig_user_pincode= px.pie(i2, values="RegisteredUser", names="Pincodes",hole=0.4,title=f"Top 10 Pincodes With PhonePe Users in {year_label} : {qt_label}",
    color_discrete_sequence=px.colors.sequential.Purples)

    col1, = st.columns(1)

    with col1:
        st.plotly_chart(fig_user_state, use_container_width=True)

    col2, = st.columns(1)

    with col2:
        st.plotly_chart(fig_user_dist, use_container_width=True)


    col3, = st.columns(1)

    with col3:
        st.plotly_chart(fig_user_pincode, use_container_width=True)

def q9():
    st.sidebar.header("🔍 Filter Options")
    years = st.sidebar.multiselect("Select Years", options=sorted(df9['Year'].unique()), default=None)
    quarter = st.sidebar.multiselect("Select Quarter", options=sorted(df9['Quarter'].unique()), default=None)
    j=df9[["State","Year","Quarter","Dist_Name","Transaction_count","Transaction_amount"]]
    k=df6[["State","Year","Quarter","Pincodes","Transaction_count","Transaction_amount"]]
    if years:
        j = j[j['Year'].isin(years)]
    if quarter:
        j = j[j['Quarter'].isin(quarter)]

    if years:
        k = k[k['Year'].isin(years)]
    if quarter:
        k = k[k['Quarter'].isin(quarter)]
    j1=j.groupby(["State", "Dist_Name"])[["Transaction_amount", "Transaction_count"]].sum().sort_values(by="Transaction_amount", ascending=False)
    j2= pd.DataFrame(j1).reset_index().head(10)

    k1=k.groupby(["State", "Pincodes"])[["Transaction_amount", "Transaction_count"]].sum().sort_values(by="Transaction_amount", ascending=False)
    k2= pd.DataFrame(k1).reset_index().head(10)
 
    year_label = ", ".join(str(int(y)) for y in years) if years else "All Years"
    qt_label ="Quarter " + ", ".join(str(int(z)) for z in quarter) if quarter else " "

    j2_melt = j2.melt( id_vars="Dist_Name", value_vars=["Transaction_amount", "Transaction_count"], 
    var_name="Metric", value_name="Value")

    fig_ins_dist= px.bar(j2_melt, x="Dist_Name", y="Value", color="Metric", barmode="group", 
    title=f"Top 10 Districts by Insurance Transactions (Amount & Count) in {year_label} : {qt_label}",
    color_discrete_map={"Transaction_amount": "lightblue","Transaction_count": "white"})  

    fig_ins_pincode_tx= px.pie(k2, values="Transaction_amount", names="Pincodes", hole=0.4,
    title=f"Top 10 Pincodes by Insurance Transaction Amount in {year_label} : {qt_label}", color_discrete_sequence=px.colors.sequential.Purples)

    fig_ins_pincode_cx= px.pie(k2, values="Transaction_count", names="Pincodes", hole=0.4,
    title=f"Top 10 Pincodes by Insurance Transaction Count in {year_label} : {qt_label}", color_discrete_sequence=px.colors.sequential.Purples)
    
    col1, = st.columns(1)

    with col1:
        st.plotly_chart(fig_ins_dist, use_container_width=True)

    col2, = st.columns(1)

    with col2:
        st.plotly_chart(fig_ins_pincode_tx, use_container_width=True)

    col3, = st.columns(1)

    with col3:
        st.plotly_chart(fig_ins_pincode_cx, use_container_width=True)


if selected == "Insights":


    q= st.selectbox("**Select the Question**",('Which states are growing in transaction volumes?','Top 10 device brands are dominant?','Top 10 State-level insurance insights',
                                  'States With Highest Trasaction Amount?','Top 10 States With Phonepe users?',
                                  '10 States High and low insurance adoption—indicating untapped potential for expanding insurance services?','Which states, districts contribute the highest to overall transaction volume and value on PhonePe?',
                                  'Which states, districts, and pin codes recorded the highest number of user registrations on year and quarter?',
                                 'What are the top 10 regions (by district or pin code) contributing to overall insurance transaction volume?'))

    if q=="Which states are growing in transaction volumes?":
        q1()

    elif q=="Top 10 device brands are dominant?":
        q2()

    elif q=="Top 10 State-level insurance insights":
        q3()

    elif q=="States With Highest Trasaction Amount?":
        q4()

    elif q=="Top 10 States With Phonepe users?":
        q5()

    elif q=="10 States High and low insurance adoption—indicating untapped potential for expanding insurance services?":
        q6()

    elif q=="Which states, districts contribute the highest to overall transaction volume and value on PhonePe?":
        q7()

    elif q=="Which states, districts, and pin codes recorded the highest number of user registrations on year and quarter?":
        q8()

    elif q=="What are the top 10 regions (by district or pin code) contributing to overall insurance transaction volume?":
        q9()

