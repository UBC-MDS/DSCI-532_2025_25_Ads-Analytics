import altair as alt

def reviews_vs_installs_chart(df):
    """
    Generate an Altair bubble chart showing reviews vs. installs.

    Parameters:
        df (pd.DataFrame): The filtered DataFrame.

    Returns:
        dict: Vega JSON object.
    """
    top_apps = df.sort_values(by="Installs", ascending=False).head(50)

    chart = alt.Chart(top_apps).mark_circle().encode(
        x=alt.X("Reviews:Q", title="Number of Reviews", axis=alt.Axis(format=",.0f")),
        y=alt.Y("Installs:Q", title="Total Installs", axis=alt.Axis(format=",.0f")),
        size=alt.Size("Rating:Q", title="App Rating", scale=alt.Scale(domain=[1, 5])),
        color=alt.Color("Category:N", title="Category"),
        tooltip=["App", "Category", alt.Tooltip("Installs:Q", format=",.0f"), alt.Tooltip("Reviews:Q", format=",.0f"), "Rating"]
    ).properties(
        title="Reviews vs. Installs for Top Apps",
        width=500,
        height=400
    ).interactive()

    return chart.to_dict(format="vega")