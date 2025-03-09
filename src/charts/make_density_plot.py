import altair as alt

def make_density_plot(df, categories):
    """
    Creates a density plot for the 'Rating' column in the dataset.

    Parameters:
    df (pandas.DataFrame): The input dataframe containing app data with a 'Rating' column.
    categories (list): A list of selected categories for filtering the data. 
                       If 'All' is included, the data will not be filtered by category.

    Returns:
    alt.Chart: An Altair chart object representing the density plot for the 'Rating' column.
    
    The function filters the dataframe based on the selected categories, and then generates
    a density plot that visualizes the distribution of 'Rating' in the dataset. If four or fewer
    categories are selected, the density plot will be grouped by category and each category will 
    have its own color. If more than four categories are selected, the plot will display the density 
    for all categories together, with the density area colored in steelblue.
    """
    # if "All" not in categories:
    #     df = df[df["Category"].isin(categories)]

    # density_chart = alt.Chart(df).transform_density(
    #     'Rating',
    #     as_=['Rating', 'Density'],
    #     groupby=['Category'] if len(categories) <= 4 else []
    # ).mark_area(opacity=0.5).encode(
    #     x='Rating:Q',
    #     y='Density:Q',
    #     #color='Category:N' if len(categories) <= 4 else alt.value('steelblue'),
    #     color=alt.Color('Category:N' if len(categories) <= 4 else alt.value('steelblue'), legend=None)
    # )
    
    if "All" not in categories:
        df = df[df["Category"].isin(categories)]

    boxplot_chart = alt.Chart(df).mark_boxplot().encode(
        y='Category:N',  
        x='Rating:Q',   
        color=alt.Color('Category:N' if len(categories) <= 4 else alt.value('steelblue'), legend=None)
    ).properties(
        width=400, height=290,
        title = "Ratings for each Category"
    )

    return boxplot_chart

    #return density_chart