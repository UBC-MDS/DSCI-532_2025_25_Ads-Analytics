import altair as alt
import pandas as pd

def total_reviews_chart(df, min_rating=0):
    """
    Generate an interactive Altair histogram chart for the total reviews.

    Parameters:
        df (pd.DataFrame): The DataFrame containing app data.
        min_rating (float): Minimum rating to filter apps.

    Returns:
        object of the Altair chart
    """

    df = df.query("Rating >= @min_rating and Rating <= @max_rating")
    average_ratings = df.groupby('Category')['Rating'].mean().reset_index()
    

    chart = alt.Chart(average_ratings).mark_point().encode(
        y=alt.Y("Category:N", sort="-x", title="App Category"),  
        x=alt.X("Rating:Q", title="Total Installs (Thousands)", axis=alt.Axis(format=",.0f")), 
        color=alt.Color("Category:N", legend=None),
        tooltip=['Category', 'Rating']
    ).properties(
        title="Ratings vs Categories",
        width=500,
        height=400
    ).interactive()

    return chart