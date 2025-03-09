import altair as alt

def engagement_chart(df):
    """
    Generate an Altair bubble chart showing reviews vs. installs.

    Parameters:
        df (pd.DataFrame): The filtered DataFrame.

    Returns:
        dict: Vega JSON object of the Altair chart.
    """
    if df.empty:
        return {"data": [], "mark": "circle", "encoding": {}}

    # Select top 50 apps for better visibility
    top_apps = df.sort_values(by="Installs", ascending=False).head(50)

    top_apps["Installs"] = top_apps["Installs"] / 1_000  
    top_apps["Reviews"] = top_apps["Reviews"] / 1_000  

    selection = alt.selection_point(fields=["Category"], bind="legend")

    chart = alt.Chart(top_apps).mark_circle().encode(
        x=alt.X("Reviews:Q", title="Number of Reviews"),
        y=alt.Y("Installs:Q", title="Total Installs"),
        size=alt.Size("Installs:Q", title="Relative Bubble Size", scale=alt.Scale(range=[10, 500])),  
        color=alt.Color("Category:N", title="Category", legend=alt.Legend(title="App Category")),  
        opacity=alt.condition(selection, alt.value(0.8), alt.value(0.2)), 
        tooltip=["App", "Category", alt.Tooltip("Installs:Q", title="Total Installs"),
                 alt.Tooltip("Reviews:Q", title="Total Reviews"), "Rating"]
    ).properties(
        title="Reviews vs. Installs for Top Apps",
        height=300
    ).add_params(
        selection  
    )

    return chart