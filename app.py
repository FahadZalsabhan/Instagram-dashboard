import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Social Accounts Dashboard",
    layout="wide"
)

st.title("Social Accounts Dashboard")
st.write("Explore followers, countries, and account categories.")

st.sidebar.header("About the data")
st.sidebar.write("Account followers, countries, categories, and ranks.")

uploaded_file = st.sidebar.file_uploader(
    "Upload cleaned_daily.csv",
    type=["csv"]
)

if uploaded_file is None:
    st.info("Upload your cleaned CSV file to start.")
    st.stop()


df = pd.read_csv(uploaded_file)
df["date"] = pd.to_datetime(df["date"])


st.success("File uploaded successfully")


st.sidebar.header("Filters")

country_options = ["All"] + sorted(df["country"].dropna().unique())
category_options = ["All"] + sorted(df["category"].dropna().unique())

selected_country = st.sidebar.selectbox(
    "Country",
    country_options
)

selected_category = st.sidebar.selectbox(
    "Category",
    category_options
)

filtered_df = df.copy()

if selected_country != "All":
    filtered_df = filtered_df[
        filtered_df["country"] == selected_country
    ]

if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["category"] == selected_category
    ]

if filtered_df.empty:
    st.warning("No records match these filters. Try another selection.")
    st.stop()


st.subheader("Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Records", f"{len(filtered_df):,}")

col2.metric(
    "Unique Accounts",
    f"{filtered_df['username'].nunique():,}"
)

col3.metric(
    "Average Followers per Record",
    f"{filtered_df['followers'].mean():,.0f}"
)

st.caption(
    "Statistics reflect the selected records. "
    "Accounts appearing on multiple dates may be counted more than once "
    "in the follower average."
)


st.subheader("Top 10 Countries by Record Count")

country_counts = (
    filtered_df["country"]
    .value_counts()
    .head(10)
    .rename_axis("country")
    .reset_index(name="records")
)

country_chart = px.bar(
    country_counts,
    x="country",
    y="records",
    labels={
        "country": "Country",
        "records": "Number of Records"
    }
)

st.plotly_chart(country_chart)


st.subheader("Followers Distribution")

followers_chart = px.histogram(
    filtered_df,
    x="followers",
    nbins=20,
    labels={"followers": "Followers"}
)

followers_chart.update_layout(
    yaxis_title="Number of Records"
)

st.plotly_chart(followers_chart)

st.subheader("Data Preview")
st.write("First 100 matching records")
st.dataframe(filtered_df.head(100), hide_index=True)
