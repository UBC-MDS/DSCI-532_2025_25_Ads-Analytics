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
        if any(type_ != "All" for type_ in selected_types):
            # If any type other than "All" is selected, clear "All" from the selection
            return [type_ for type_ in selected_types if type_ != "All"]
        else:
            # If only "All" is selected, return ["All"]
            return ["All"]
        return selected_types

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
        if any(type_ != "All" for type_ in selected_ratings):
            # If any type other than "All" is selected, clear "All" from the selection
            return [type_ for type_ in selected_ratings if type_ != "All"]
        else:
            # If only "All" is selected, return ["All"]
            return ["All"]
        return selected_ratings