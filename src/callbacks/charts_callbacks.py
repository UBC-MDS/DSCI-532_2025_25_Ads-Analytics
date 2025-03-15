# callbacks/charts_callbacks.py

from dash import Input, Output
import pandas as pd
from src.charts.engagement_chart import engagement_chart
from src.components.get_summary_stats import get_summary_stats
from src.charts.make_density_plot import make_density_plot
from src.charts.ranking_chart import create_wordcloud
from src.charts.make_popularity_score import make_popularity_score

def register_charts_callbacks(app, df):
    """
    Register callbacks related to updating charts and visualizations.

    Parameters:
    app (Dash): The Dash app instance.
    df (pd.DataFrame): The DataFrame containing the data.
    """

    @app.callback(
        [Output("popularity-histogram", "spec"),
         Output("engagement-chart", "spec"),
         Output("mean-rating", "children"),
         Output("mean-reviews", "children"),
         Output("mean-installs", "children"),
         Output("category-filter", "value"),
         Output("density-plot", "spec"),
         Output("wordcloud", "figure")],
        [Input("app-type-filter", "value"),
         Input("rating-slider", "value"),
         Input("content-rating-filter", "value"),
         Input("category-filter", "value")]
    )
    def update_charts(selected_types, rating_range, selected_ratings, selected_categories):
        """
        Update all charts and summary statistics based on the selected filters.

        Parameters:
        selected_types (list): Selected app types.
        rating_range (list): Selected rating range.
        selected_ratings (list): Selected content ratings.
        selected_categories (list): Selected categories.

        Returns:
        tuple: Updated chart specifications and summary statistics.
        """
        # If any required filter is empty, return a message indicating no data
        if not selected_types or not rating_range or not selected_ratings or not selected_categories:
            no_data_msg = {"mark": "text", "encoding": {"text": {"value": "No data selected"}}}
            return (
                no_data_msg, no_data_msg, "No data", "No data", "No data", [], no_data_msg, {}
            )

        # Handle "All" selection for filters
        if "All" in selected_types:
            selected_types = df["Type"].unique()
        if "All" in selected_ratings:
            selected_ratings = df["Content Rating"].unique()
        if "All" in selected_categories:
            selected_categories = df["Category"].unique()

        # Limit to 4 categories for better visualization
        elif len(selected_categories) > 4:
            selected_categories = selected_categories[:4]

        # Apply filters to the DataFrame
        min_rating, max_rating = rating_range
        filtered_df = df[
            (df["Type"].isin(selected_types)) &
            (df["Rating"] >= min_rating) & (df["Rating"] <= max_rating) &
            (df["Content Rating"].isin(selected_ratings)) &
            (df["Category"].isin(selected_categories))
        ]

        # If no data after filtering, return a message
        if filtered_df.empty:
            return (
                no_data_msg, no_data_msg, "No data", "No data", "No data", selected_categories, no_data_msg, {}
            )

        # Calculate mean statistics
        stats = get_summary_stats(filtered_df)

        # Determine if "All" should remain selected
        updated_categories = (
            ["All"] if len(selected_categories) == len(df["Category"].unique()) else selected_categories
        )

        # Return updated components
        return (
            make_popularity_score(filtered_df, updated_categories).to_dict(format="vega"),
            engagement_chart(filtered_df, updated_categories).to_dict(format="vega"),
            f"{stats['mean_rating']:.2f}",
            f"{stats['mean_reviews']:,.0f}",
            f"{stats['mean_installs']:,.0f}",
            updated_categories,
            make_density_plot(filtered_df, updated_categories).to_dict(format="vega"),
            create_wordcloud(filtered_df, updated_categories)
        )