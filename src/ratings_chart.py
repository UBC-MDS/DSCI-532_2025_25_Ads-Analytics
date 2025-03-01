import altair as alt
import pandas as pd

def ratings_chart(df):
    """
    Generate an interactive Altair histogram chart for the ratings vs App categories.

    Parameters:
        df (pd.DataFrame): The DataFrame containing app data.
        min_rating (float): Minimum rating to filter apps.
        max_rating (float): Maximum rating to filter apps.

    Returns:
        object of the Altair chart
    """

    #df = df.query("Rating >= @min_rating and Rating <= @max_rating")
    average_ratings = df.groupby('Category')['Rating'].mean().reset_index()
    

    chart = alt.Chart(average_ratings).mark_bar().encode(
        y=alt.Y("Category:N", sort="-x", title="App Category"),  
        x=alt.X("Rating:Q", title="Average Ratings", axis=alt.Axis(format=",.0f")), 
        color=alt.Color("Category:N", legend=None),
        tooltip=['Category', 'Rating']
    ).properties(
        title="Average Ratings vs Categories",
        width=500,
        height=400
    )

    return chart