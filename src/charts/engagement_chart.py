import altair as alt

def engagement_chart(df, categories):
    """
    Generate an Altair bubble chart showing reviews vs. installs.

    Parameters:
        df (pd.DataFrame): The filtered DataFrame.

    Returns:
        dict: Vega JSON object of the Altair chart.
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

    chart = alt.Chart(top_apps).mark_circle(size=10).encode(
    x=alt.X("Reviews:Q", title="Number of Reviews",
            scale=alt.Scale(domain=[top_apps["Reviews"].min(), top_apps["Reviews"].max()])),
    y=alt.Y("Installs:Q", title="Total Installs",
            scale=alt.Scale(domain=[top_apps["Installs"].min(), top_apps["Installs"].max()])),
    size=alt.Size("Installs:Q", title="Bubble Size by Installs", scale=alt.Scale(range=[10, 500])),  
    color=alt.Color("Category:N", title="Category",
                    scale=alt.Scale(domain=list(category_to_color.keys()), 
                                    range=list(category_to_color.values()))),  
    opacity=alt.condition(selection, alt.value(0.8), alt.value(0.2)), 
    tooltip=["App", "Category", alt.Tooltip("Installs:Q", title="Total Installs"),
             alt.Tooltip("Reviews:Q", title="Total Reviews"), "Rating"]
).properties(
    height=290
).add_params(
    selection  
)

    return chart