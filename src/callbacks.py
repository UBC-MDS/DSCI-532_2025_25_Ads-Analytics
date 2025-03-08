from dash import Input, Output, ctx
import pandas as pd

from src.charts.engagement_chart import engagement_chart
from src.get_summary_stats import get_summary_stats
from src.charts.make_density_plot import make_density_plot
from src.charts.make_reviews_histogram import make_reviews_histogram
from src.charts.ranking_chart import create_wordcloud 
from src.charts.make_popularity_score import make_popularity_score

def register_callbacks(app, df):
    """
    Register all callbacks for the Dash app.

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
        # If any required filter is empty, return blank outputs
        if not selected_types or not rating_range or not selected_ratings or not selected_categories:
            return (
                {}, {}, "-", "-", "-", [], {}, {}
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

        # If no data after filtering, return blank outputs
        if filtered_df.empty:
            return (
                {}, {}, "-", "-", "-", selected_categories, {}, {}
            )

        # Calculate mean statistics
        stats = get_summary_stats(filtered_df)
        mean_rating = f"{stats['mean_rating']:.2f}"
        mean_reviews = f"{stats['mean_reviews']:,.0f}"
        mean_installs = f"{stats['mean_installs']:,.0f}"

        # Determine if "All" should remain selected
        updated_categories = (
            ["All"] if len(selected_categories) == len(df["Category"].unique()) else selected_categories
        )

        # Return updated components
        return (
            make_popularity_score(filtered_df, updated_categories).to_dict(format="vega"),
            engagement_chart(filtered_df, updated_categories).to_dict(format="vega"),
            mean_rating,
            mean_reviews,
            mean_installs,
            updated_categories,
            make_density_plot(filtered_df, updated_categories).to_dict(format="vega"),
            create_wordcloud(filtered_df, updated_categories)
        )

    @app.callback(
        Output("app-type-filter", "value"),
        Input("app-type-filter", "value"),
        prevent_initial_call=True
    )
    def update_app_type_selection(selected_types):
        """
        Ensures that selecting 'All' in App Type filter disables other selections and vice versa.
        """
        if "All" in selected_types and len(selected_types) > 1:
            return ["All"]  # Reset to "All" only
        return selected_types  # Allow other selections if "All" is not selected

    @app.callback(
        Output("content-rating-filter", "value"),
        Input("content-rating-filter", "value"),
        prevent_initial_call=True
    )
    def update_content_rating_selection(selected_ratings):
        """
        Ensures that selecting 'All' in Content Rating filter disables other selections and vice versa.
        """
        if "All" in selected_ratings and len(selected_ratings) > 1:
            return ["All"]  # Reset to "All" only
        return selected_ratings  # Allow other selections if "All" is not selected
