import altair as alt

def make_density_plot(df, categories):
    if "All" not in categories:
        df = df[df["Category"].isin(categories)]

    density_chart = alt.Chart(df).transform_density(
        'Rating',
        as_=['Rating', 'Density'],
        groupby=['Category'] if len(categories) <= 4 else []
    ).mark_area(opacity=0.5).encode(
        x='Rating:Q',
        y='Density:Q',
        color='Category:N' if len(categories) <= 4 else alt.value('steelblue')
    ).properties(
        title="Density Plot for Ratings",
        width=450,
        height=400
    )

    return density_chart