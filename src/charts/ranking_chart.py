import altair as alt
import pandas as pd

def ranking_chart(df, selected_type="Free", min_rating=4):
    """
    Generate an interactive Altair bar chart for the Top 10 Apps by Installs.

    Parameters:
        df (pd.DataFrame): The DataFrame containing app data.
        selected_type (str): "Free" or "Paid" to filter by app type.
        min_rating (float): Minimum rating to filter apps.

    Returns:
        object of the Altair chart
    """
    alt.data_transformers.enable("vegafusion")
    filtered_df = df[(df["Type"] == selected_type) & (df["Rating"] >= min_rating)]

    top_apps = filtered_df.groupby("App")["Installs"].sum().reset_index()

    top_apps["Installs"] = pd.to_numeric(top_apps["Installs"], errors='coerce')

    top_apps = top_apps.dropna(subset=["Installs"])

    top_apps = top_apps.sort_values(by="Installs", ascending=False).head(10)

    chart = alt.Chart(top_apps).mark_bar().encode(
        y=alt.Y("App:N", sort="-x", title="App"),
        x=alt.X("Installs:Q", title="Total Installs"), 
        color=alt.Color("App:N", legend=None),
        tooltip=[alt.Tooltip("App:N", title="App Name"),
                 alt.Tooltip("Installs:Q", title="Total Installs")]
    ).properties(
        title="Top 10 Apps by Installs",
        width=900,
        height=800
    )

    return chart