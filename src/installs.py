import altair as alt
import pandas as pd

def installs_chart(df, selected_type="Free", min_rating=4):
    """
    Generate an interactive Altair bar chart for the Top 10 App Categories by Installs.

    Parameters:
        df (pd.DataFrame): The DataFrame containing app data.
        selected_type (str): "Free" or "Paid".
        min_rating (float): Minimum rating to filter apps.

    Returns:
        str: Interactive Altair chart in HTML format.
    """
    filtered_df = df[(df["Type"] == selected_type) & (df["Rating"] >= min_rating)]

    top_categories = filtered_df.groupby("Category")["Installs"].sum().reset_index()
    top_categories = top_categories.sort_values(by="Installs", ascending=False).head(10)

    selection = alt.selection_interval(encodings=['x'])

    chart = alt.Chart(top_categories).mark_bar().encode(
        x=alt.X("Category:N", sort="-y", title="App Category"),
        y=alt.Y("Installs:Q", title="Total Installs"),
        color=alt.condition(selection, alt.Color("Category:N", legend=None), alt.value("lightgray")),
        tooltip=[alt.Tooltip("Category:N", title="App Category"),
                 alt.Tooltip("Installs:Q", title="Total Installs")]
    ).properties(
        title="Top 10 App Categories by Installs",
        width=600,
        height=400
    ).add_params(
        selection
    )

    return chart.to_html()