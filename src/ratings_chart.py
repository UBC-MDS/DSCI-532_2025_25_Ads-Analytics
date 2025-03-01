import altair as alt
import pandas as pd

def ratings_chart(df):
    """
    Generate an interactive Altair histogram chart for the ratings vs App categories.

    Parameters:
        df (pd.DataFrame): The DataFrame containing app data.

    Returns:
        object of the Altair chart
    """

    #df = df.query("Rating >= @min_rating and Rating <= @max_rating")
    average_ratings = df.groupby('Category')['Rating'].mean().reset_index()
    #average_ratings['Rating'] = pd.to_numeric(average_ratings['Rating'], errors='coerce')
    min_rating = average_ratings['Rating'].min()
    max_rating = average_ratings['Rating'].max()

    chart = alt.Chart(average_ratings).mark_bar().encode(
        y=alt.Y("Category:N", sort="-x", title="App Category"),  
        x=alt.X("Rating:Q", title="Average Ratings", axis=alt.Axis(format=",.1f", tickCount=6)),
         
        color=alt.Color("Category:N", legend=None),
        tooltip=['Category', 'Rating']
    ).properties(
        title="Average Ratings vs Categories",
        width=300,
        height=400
    )

    return chart