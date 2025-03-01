import altair as alt

def make_reviews_histogram(df, categories):
    
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