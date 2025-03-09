from dash import Input, Output
import pandas as pd

from src.charts.install_chart import installs_chart
from src.charts.engagement_chart import engagement_chart
from src.get_summary_stats import get_summary_stats
from src.charts.make_density_plot import make_density_plot
from src.charts.make_reviews_histogram import make_reviews_histogram
from src.charts.ranking_chart import create_wordcloud 

def register_callbacks(app, df):
    """
    Register all callbacks for the Dash app.
    
    Parameters:
    app (Dash): The Dash app instance.
    df (pd.DataFrame): The DataFrame containing the data.
    """
    @app.callback(
        [Output("category-chart", "spec"),
         Output("engagement-chart", "spec"),
         Output("mean-rating", "children"),
         Output("mean-reviews", "children"),
         Output("mean-installs", "children"),
         Output("category-filter", "value"),
         Output("density-plot", "spec"),
         Output("reviews-histogram", "spec"),
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
                {}, {}, "-", "-", "-", [], {}, {}, {}
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
                {}, {}, "-", "-", "-", selected_categories, {}, {}, {}
            )

        # Calculate mean statistics
        stats = get_summary_stats(filtered_df)
        mean_rating = f"{stats['mean_rating']:.2f}"
        mean_reviews = f"{stats['mean_reviews']:.0f}"
        mean_installs = f"{stats['mean_installs']:.0f}"

        # Determine if "All" should remain selected
        updated_categories = (
            ["All"] if len(selected_categories) == len(df["Category"].unique()) else selected_categories
        )

        # Return updated components
        return (
            installs_chart(filtered_df).to_dict(format="vega"),
            engagement_chart(filtered_df, ["All"]).to_dict(format="vega"),
            summary_data,
            ["All"] if len(selected_categories) == len(df["Category"].unique()) else selected_categories,
            make_density_plot(filtered_df, ["All"]).to_dict(format="vega"),  
            make_reviews_histogram(filtered_df, selected_categories).to_dict(format="vega"),
            create_wordcloud(filtered_df, ["All"]) 
            engagement_chart(filtered_df).to_dict(format="vega"),
            mean_rating,
            mean_reviews,
            mean_installs,
            updated_categories,
            make_density_plot(filtered_df, updated_categories).to_dict(format="vega"),
            make_reviews_histogram(filtered_df, updated_categories).to_dict(format="vega"),
            create_wordcloud(filtered_df, updated_categories)
        )
