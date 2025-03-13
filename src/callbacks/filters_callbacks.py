# callbacks/filters_callbacks.py

from dash import Input, Output

def register_filters_callbacks(app):
    """
    Register callbacks related to updating filters.

    Parameters:
    app (Dash): The Dash app instance.
    """

    @app.callback(
        Output("app-type-filter", "value"),
        Input("app-type-filter", "value"),
        prevent_initial_call=True
    )
    def update_app_type_selection(selected_types):
        """
        Ensures that selecting 'All' in App Type filter disables other selections and vice versa.

        Parameters:
        selected_types (list): Selected app types.

        Returns:
        list: Updated selected app types.
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

        Parameters:
        selected_ratings (list): Selected content ratings.

        Returns:
        list: Updated selected content ratings.
        """
        if "All" in selected_ratings and len(selected_ratings) > 1:
            return ["All"]  # Reset to "All" only
        return selected_ratings  # Allow other selections if "All" is not selected