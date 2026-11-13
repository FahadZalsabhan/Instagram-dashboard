
# Instagram accounts dashboard

Our first-week project at Tuwaiq Academy. We used Python to explore Instagram account data and built a dashboard with Streamlit.

## Data

[Instagram Top Accounts on Kaggle](https://www.kaggle.com/datasets/arkhiplisitsa/instagram-top-accounts)

The cleaned data has 38071 records and 11998 unique usernames. Some accounts appear on multiple dates.

## What we did

- Checked missing values and data types.
- Calculated basic statistics.
- Removed extra spaces and converted dates.
- Filled missing text values with "Unknown" or "Not specified".
- Built country and category filters.
- Added summary statistics and interactive charts.
- Displayed a preview of the data.

The US has the most records in this dataset. Most follower counts are at the lower end with a few very large values. Averages include repeated accounts.

## Files

- app.py contains the dashboard code.
- analysis.ipynb contains the analysis and cleaning steps.
- cleaned_daily.csv contains the cleaned data.
- pyproject.toml and uv.lock store the project dependencies.

## Tools

We used Python with pandas and Streamlit. We created charts using Plotly and Matplotlib with Seaborn. We also used uv and Git and worked in Google Colab.

## How to run

Install uv and run these commands inside the project folder.

```bash
uv sync
uv run streamlit run app.py
```

Open the link shown in the terminal and upload cleaned_daily.csv from the sidebar.

To run the analysis in Colab, open analysis.ipynb and upload the original daily.csv when prompted. Run the cells in order.

