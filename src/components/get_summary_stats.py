import pandas as pd

def get_summary_stats(filtered_df):
    """
    Calculates summary statistics for the filtered DataFrame, including mean, min, and max values 
    for the 'Rating', 'Installs', and 'Reviews' columns.

    Args:
        filtered_df (pandas.DataFrame): The filtered DataFrame containing app data with columns 'Rating', 
                                         'Installs', and 'Reviews'.

    Returns:
        dict: A dictionary containing the calculated summary statistics:
            - mean_rating (float): The mean of the 'Rating' column, rounded to 2 decimal places.
            - min_rating (float): The minimum value in the 'Rating' column.
            - max_rating (float): The maximum value in the 'Rating' column.
            - mean_installs (float): The mean of the 'Installs' column, rounded to the nearest whole number.
            - min_installs (float): The minimum value in the 'Installs' column.
            - max_installs (float): The maximum value in the 'Installs' column.
            - mean_reviews (float): The mean of the 'Reviews' column, rounded to the nearest whole number.
            - min_reviews (float): The minimum value in the 'Reviews' column.
            - max_reviews (float): The maximum value in the 'Reviews' column.

    Example:
        filtered_df = df[(df['Rating'] > 3) & (df['Category'] == 'Games')]
        stats = get_summary_stats(filtered_df)
        print(stats)
    """
    mean_rating = filtered_df['Rating'].mean()

    mean_installs = filtered_df['Installs'].mean()

    mean_reviews = filtered_df['Reviews'].mean()

    return {
        "mean_rating": round(mean_rating, 2),
        "mean_installs": round(mean_installs, 0),
        "mean_reviews": round(mean_reviews, 0)
    }