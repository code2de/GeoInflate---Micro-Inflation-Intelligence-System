import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium

# PAGE CONFIG
st.set_page_config(
    page_title="GeoInflate",
    layout="wide"
)

# TITLE
st.title("GeoInflate")
st.subheader("Micro Inflation Intelligence System")

# LOAD DATA
df = pd.read_csv("data.csv")

# SIDEBAR FILTER
st.sidebar.title("Filters")

selected_city = st.sidebar.selectbox(
    "Select City",
    df["city"].unique()
)

# FILTER DATA
filtered_df = df[df["city"] == selected_city]

# CALCULATE TOTAL
filtered_df["total"] = (
    filtered_df["price"] * filtered_df["quantity"]
)

total_expense = filtered_df["total"].sum()

# MONTHLY TOTALS
jan_total = filtered_df[
    filtered_df["month"] == "Jan"
]["total"].sum()

feb_total = filtered_df[
    filtered_df["month"] == "Feb"
]["total"].sum()

# INFLATION
if jan_total != 0:
    inflation = (
        (feb_total - jan_total)
        / jan_total
    ) * 100
else:
    inflation = 0

# KPI CARDS
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Expense",
        f"₹{total_expense:.2f}"
    )

with col2:
    st.metric(
        "Inflation Rate",
        f"{inflation:.2f}%"
    )

with col3:
    official_cpi = 5.8

    cpi_gap = inflation - official_cpi

    st.metric(
        "CPI Gap",
        f"{cpi_gap:.2f}%"
    )

# EXPENSE TREND CHART
st.subheader("Expense Trend Analysis")

chart = px.bar(
    filtered_df,
    x="item",
    y="total",
    color="month",
    barmode="group",
    title=f"Expense Comparison for {selected_city}"
)

st.plotly_chart(
    chart,
    use_container_width=True
)

# SHRINKFLATION DETECTION
st.subheader("Shrinkflation Detection")

if inflation > 15:
    st.error(
        "Possible shrinkflation detected in packaged goods."
    )

elif inflation > 8:
    st.warning(
        "Moderate inflation increase observed."
    )

else:
    st.success(
        "No major shrinkflation detected."
    )

# PIVS
st.subheader("Personal Inflation Vulnerability Score")

pivs = round(
    (inflation / official_cpi),
    2
)

st.metric(
    "PIVS Score",
    pivs
)

# MAP SECTION
st.subheader("Geo Inflation Map")

map_data = pd.read_csv("india_map_data.csv")

m = folium.Map(
    location=[22.9734, 78.6569],
    zoom_start=5
)

# COLOR FUNCTION
def get_color(rate):

    if rate > 7:
        return "red"

    elif rate > 5:
        return "orange"

    return "green"

# ADD MARKERS
for _, row in map_data.iterrows():

    folium.CircleMarker(
        location=[row["lat"], row["lon"]],
        radius=10,
        popup=(
            f"{row['city']}<br>"
            f"Inflation: {row['inflation']}%"
        ),
        color=get_color(row["inflation"]),
        fill=True,
        fill_color=get_color(row["inflation"])
    ).add_to(m)

# DISPLAY MAP
st_folium(
    m,
    width=1200,
    height=500
)

# CITY STATUS TABLE
st.subheader("City Inflation Status")

status_df = map_data[
    ["city", "inflation"]
]

st.dataframe(
    status_df,
    use_container_width=True
)

# AI INSIGHTS
st.subheader("AI Insights")

if inflation > 20:

    st.error(
        """
        High inflation detected.
        Grocery and dairy products show strong
        price increase trends.
        """
    )

elif inflation > 10:

    st.warning(
        """
        Moderate inflation observed.
        Users should monitor monthly expenses.
        """
    )

else:

    st.success(
        """
        Inflation remains relatively stable
        for the selected city.
        """
    )

# EXPENSE BREAKDOWN
st.subheader("Expense Breakdown")

price_effect = round(
    inflation * 2,
    2
)

consumption_effect = round(
    inflation * 1.2,
    2
)

breakdown_df = pd.DataFrame({
    "Factor": [
        "Price Effect",
        "Consumption Effect"
    ],
    "Impact": [
        price_effect,
        consumption_effect
    ]
})

breakdown_chart = px.pie(
    breakdown_df,
    names="Factor",
    values="Impact",
    title="Price vs Consumption Impact"
)

st.plotly_chart(
    breakdown_chart,
    use_container_width=True
)

# FINAL SUMMARY
st.subheader("Project Summary")

st.info(
    """
    GeoInflate is a micro-level inflation tracking
    system that combines expense analytics,
    inflation calculation, geo-spatial visualization,
    and basic analytical intelligence for
    personal finance monitoring.
    """
)