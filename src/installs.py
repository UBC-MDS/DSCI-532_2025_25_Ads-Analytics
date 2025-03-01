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
        object of the Altair chart
    """
    top_categories = df.groupby("Category")["Installs"].sum().reset_index()
    top_categories["Installs"] = top_categories["Installs"] / 1000  
    top_categories = top_categories.sort_values(by="Installs", ascending=False).head(10)

    chart = alt.Chart(top_categories).mark_bar().encode(
        y=alt.Y("Category:N", sort="-x", title="App Category"),  
        x=alt.X("Installs:Q", title="Total Installs (Thousands)", axis=alt.Axis(format=",.0f")), 
        color=alt.Color("Category:N", legend=None),
        tooltip=[alt.Tooltip("Category:N", title="App Category"),
                 alt.Tooltip("Installs:Q", title="Total Installs (K)", format=",.0f")]
    ).properties(
        title="Top 10 App Categories by Installs",
        width=600,
        height=400
    ).interactive()  

    return chart