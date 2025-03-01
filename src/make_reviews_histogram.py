import altair as alt

def make_reviews_histogram(df, categories):
    """
    Creates a histogram for the 'Reviews' column in the dataset.

    Parameters:
    df (pandas.DataFrame): The input dataframe containing app data with a 'Reviews' column.
    categories (list): A list of selected categories for filtering the data. 
                       If 'All' is included, the data will not be filtered by category.

    Returns:
    alt.Chart: An Altair chart object representing the histogram for the 'Reviews' column.
    
    The function filters the dataframe based on the selected categories, and then generates
    a histogram that visualizes the distribution of 'Reviews' in the dataset. If more than
    four categories are selected, the color of the bars is set to orange. Otherwise, the bars
    are colored by category.
    """
    if "All" not in categories:
        df = df[df["Category"].isin(categories)]

    reviews_histogram = alt.Chart(df).mark_bar(opacity = 0.5).encode(
        alt.X('Reviews:Q', bin=alt.Bin(maxbins=25), title='Number of Reviews'),
        alt.Y('count():Q', title='Count'),
        color='Category:N' if len(categories) <= 4 else alt.value('orange')
    ).properties(
        title="Histogram for Number of Reviews",
        width=450,
        height=400
    )

    return reviews_histogram