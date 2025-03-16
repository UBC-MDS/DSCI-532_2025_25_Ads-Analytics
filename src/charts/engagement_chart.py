import altair as alt

def engagement_chart(df, categories):
    """
    Generate an Altair bubble chart showing reviews vs. installs with zoom functionality.

    Parameters:
        df (pd.DataFrame): The filtered DataFrame.
        categories (list): The categories to filter on.

    Returns:
        alt.Chart: Altair chart with zoom functionality.
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

    # Select top 50 apps for better visibility
    top_apps = df.sort_values(by="popularity_score", ascending=False).head(50)

    top_apps["Installs"] = top_apps["Installs"] / 1_000  
    top_apps["Reviews"] = top_apps["Reviews"] / 1_000  

    selection = alt.selection_point(fields=["Category"], bind="legend")

    # Create a zoom selection
    zoom = alt.selection_interval(bind='scales')

    chart = alt.Chart(top_apps).mark_circle(size=75).encode(
        x=alt.X("Reviews:Q", title="Number of Reviews",
                scale=alt.Scale(domain=[top_apps["Reviews"].min(), top_apps["Reviews"].max()])),
        y=alt.Y("Installs:Q", title="Total Installs",
                scale=alt.Scale(domain=[top_apps["Installs"].min(), top_apps["Installs"].max()])),  
        color=alt.Color("Category:N", title="Category",
                        scale=alt.Scale(domain=list(category_to_color.keys()), 
                                        range=list(category_to_color.values()))),  
        opacity=alt.condition(selection, alt.value(0.8), alt.value(0.2)),
        size=alt.Size("Rating:Q", title="Rating",
                  scale=alt.Scale(domain=[top_apps["Rating"].min(), top_apps["Rating"].max()], range=[50, 500])),  
        tooltip=["App", "Category", alt.Tooltip("Installs:Q", title="Total Installs"),
                 alt.Tooltip("Reviews:Q", title="Total Reviews"), "Rating"]
    ).properties(
        height=290
    ).add_params(
        selection,
        zoom
    )

    return chart
