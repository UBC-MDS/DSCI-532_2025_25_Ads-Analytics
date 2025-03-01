import altair as alt
import pandas as pd

def total_reviews_chart(df):
    """
    Generate an interactive Altair histogram chart for the total reviews.

    Parameters:
        df (pd.DataFrame): The DataFrame containing app data.

    Returns:
        object of the Altair chart
    """

    #df = df.query("Rating >= @min_rating")
    average_reviews = df.groupby('Category')['Reviews'].mean().reset_index()
    

    chart = alt.Chart(average_reviews).mark_bar().encode(
        y=alt.Y("Category:N", sort="-x", title="App Category"),  
        x=alt.X("Reviews:Q", title="Average Reviews", axis=alt.Axis(format=",.0f")), 
        color=alt.Color("Category:N", legend=None),
        tooltip=['Category', 'Reviews']
    ).properties(
        title="Average Reviews vs Categories",
        width=500,
        height=400
    ).interactive()

    return chart