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
    category_to_color = {
    'GAME': "#1f77b4",
    'ENTERTAINMENT': "#ff7f0e",
    'PHOTOGRAPHY': "#2ca02c",
    'VIDEO_PLAYERS': "#d62728",
    'SHOPPING': "#9467bd",
    'SOCIAL': "#8c564b",
    'COMMUNICATION': "#e377c2",
    'HOUSE_AND_HOME': "#7f7f7f",
    'WEATHER': "#bcbd22",
    'EDUCATION': "#17becf"
    }
    
    top_categories = df.groupby("Category")["Installs"].sum().reset_index()
    top_categories["Installs"] = top_categories["Installs"] / 1000  
    top_categories = top_categories.sort_values(by="Installs", ascending=False).head(10)

    chart = alt.Chart(top_categories).mark_bar().encode(
        y=alt.Y("Category:N", sort="-x", title="App Category"),  
        x=alt.X("Installs:Q", title="Total Installs"), 
        color=alt.Color("Category:N", scale=alt.Scale(domain=list(category_to_color.keys()), range=list(category_to_color.values())), legend=None),
        tooltip=[alt.Tooltip("Category:N", title="App Category"),
                 alt.Tooltip("Installs:Q", title="Total Installs")]
    ).properties(
        #title="Top 10 App Categories by Installs",
        height=300,
        width=400
    )

    return chart