# callbacks/charts_callbacks.py

from dash import Input, Output
import pandas as pd

from src.charts.engagement_chart import engagement_chart
from src.components.get_summary_stats import get_summary_stats
from src.charts.make_density_plot import make_density_plot
from src.charts.ranking_chart import create_wordcloud
from src.charts.make_popularity_score import make_popularity_score

from src.utils.cache import cache

def register_charts_callbacks(app, df):
    """
    Register callbacks related to updating charts and visualizations.

    Parameters:
    app (Dash): The Dash app instance.
    df (pd.DataFrame): The DataFrame containing the data.
    """


    def filter_dataframe(selected_types, rating_range, selected_ratings, selected_categories):
        """
        Filter the DataFrame based on the selected filters.
        """
        if "All" in selected_types:
            selected_types = df["Type"].unique()
        if "All" in selected_ratings:
            selected_ratings = df["Content Rating"].unique()
        if "All" in selected_categories:
            selected_categories = df["Category"].unique()

        min_rating, max_rating = rating_range
        filtered_df = df[
            (df["Type"].isin(selected_types)) &
            (df["Rating"] >= min_rating) & (df["Rating"] <= max_rating) &
            (df["Content Rating"].isin(selected_ratings)) &
            (df["Category"].isin(selected_categories))
        ]
        return filtered_df

    @app.callback(
        [Output("popularity-histogram", "spec"),
         Output("engagement-chart", "spec"),
         Output("density-plot", "spec"),
         Output("wordcloud", "figure")],
        [Input("app-type-filter", "value"),
         Input("rating-slider", "value"),
         Input("content-rating-filter", "value"),
         Input("category-filter", "value")]
    )
    def update_charts(selected_types, rating_range, selected_ratings, selected_categories):
        """
        Update charts based on the selected filters.
        """
        if not selected_types or not rating_range or not selected_ratings or not selected_categories:
            no_data_msg = {"mark": "text", "encoding": {"text": {"value": "No data selected"}}}
            return no_data_msg, no_data_msg, no_data_msg, {}

        filtered_df = filter_dataframe(selected_types, rating_range, selected_ratings, selected_categories)
        if filtered_df.empty:
            no_data_msg = {"mark": "text", "encoding": {"text": {"value": "No data selected"}}}
            return no_data_msg, no_data_msg, no_data_msg, {}

        return (
            make_popularity_score(filtered_df, selected_categories).to_dict(format="vega"),
            engagement_chart(filtered_df, selected_categories).to_dict(format="vega"),
            make_density_plot(filtered_df, selected_categories).to_dict(format="vega"),
            create_wordcloud(filtered_df, selected_categories)
        )

    @app.callback(
        [Output("mean-rating", "children"),
         Output("mean-reviews", "children"),
         Output("mean-installs", "children")],
        [Input("app-type-filter", "value"),
         Input("rating-slider", "value"),
         Input("content-rating-filter", "value"),
         Input("category-filter", "value")]
    )
    def update_summary_stats(selected_types, rating_range, selected_ratings, selected_categories):
        """
        Update summary statistics based on the selected filters.
        """
        if not selected_types or not rating_range or not selected_ratings or not selected_categories:
            return "No data", "No data", "No data"

        filtered_df = filter_dataframe(selected_types, rating_range, selected_ratings, selected_categories)
        if filtered_df.empty:
            return "No data", "No data", "No data"

        stats = get_summary_stats(filtered_df)
        return (
            f"{stats['mean_rating']:.2f}",
            f"{stats['mean_reviews']:,.0f}",
            f"{stats['mean_installs']:,.0f}"
        )