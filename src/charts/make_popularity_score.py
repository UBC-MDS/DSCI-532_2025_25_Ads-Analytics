import altair as alt

def make_popularity_score(df, categories):
    """
    Creates a histogram for the average of popularity score for each category selected in the dataset.

    Parameters:
    df (pandas.DataFrame): The input dataframe containing app data with a 'Reviews' column.
    categories (list): A list of selected categories for filtering the data. 
                       If 'All' is included, the data will not be filtered by category.

    Returns:
    alt.Chart: An Altair chart object representing the popularity score for each category selected in the dataset
    
    The function filters the dataframe based on the selected categories, and then generates
    a bar plot that visualizes the distribution of average popularity score over selected categories in the dataset. If more than
    four categories are selected, the color of the bars is set to orange. Otherwise, the bars
    are colored by category.
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
    
    if "All" not in categories:
        df = df[df["Category"].isin(categories)]

    # Aggregate the data to calculate the average popularity_score by Category
    category_avg_popularity = df.groupby('Category')['popularity_score'].mean().reset_index(name='avg_popularity_score')

    # Create an Altair bar chart to visualize the average popularity_score by category
    avg_popularity_chart = alt.Chart(category_avg_popularity).mark_bar().encode(
        alt.Y('Category:N', title='Category', sort='-x'),  
        alt.X('avg_popularity_score:Q', title='Average Popularity Score'),  
        #color='Category:N' if len(categories) <= 4 else alt.value('orange'),  
        color=alt.Color('Category:N' if len(categories) <= 4 else alt.value('orange'), scale=alt.Scale(domain=list(category_to_color.keys()), range=list(category_to_color.values())),legend=None),
        tooltip=["Category",  alt.Tooltip("avg_popularity_score:Q", title="Average Popularity Score")]
    ).properties(
        width=400, height=290,
        title="Average Popularity Score by Category"
    )

    return avg_popularity_chart