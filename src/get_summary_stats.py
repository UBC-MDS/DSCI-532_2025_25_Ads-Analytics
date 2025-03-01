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
    min_rating = filtered_df['Rating'].min()
    max_rating = filtered_df['Rating'].max()

    mean_installs = filtered_df['Installs'].mean()
    min_installs = filtered_df['Installs'].min()
    max_installs = filtered_df['Installs'].max()

    mean_reviews = filtered_df['Reviews'].mean()
    min_reviews = filtered_df['Reviews'].min()
    max_reviews = filtered_df['Reviews'].max()

    return {
        "mean_rating": round(mean_rating, 2),
        "min_rating": min_rating,
        "max_rating": max_rating,
        "mean_installs": round(mean_installs, 0),
        "min_installs": min_installs,
        "max_installs": max_installs,
        "mean_reviews": round(mean_reviews, 0),
        "min_reviews": min_reviews,
        "max_reviews": max_reviews,
    }