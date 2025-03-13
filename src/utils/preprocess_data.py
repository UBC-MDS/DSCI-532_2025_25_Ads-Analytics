import pandas as pd
import os
import numpy as np

def clean_and_save_data():
    """
    Clean the Google Play Store dataset by applying necessary transformations 
    and saving the cleaned data to a CSV file.

    This function:
    - Reads the raw dataset from the specified path.
    - Removes rows with ratings greater than 5.
    - Fills missing ratings with the mean of their respective categories.
    - Drops the columns 'Current Ver', 'Last Updated', and 'Android Ver'.
    - Imputes missing values in the 'Type' column based on the 'Price' column.
    - Converts the 'Installs' column to a numeric format (removing commas and plus signs).
    - Rounds the 'Rating' column to 1 decimal place.
    - Saves the cleaned dataset to a CSV file in the 'preprocessed' directory.

    Parameters
    ----------
    None

    Returns
    -------
    None

    Raises
    ------
    FileNotFoundError
        If the input raw data file does not exist at the specified path.
    
    FileExistsError
        If the output directory cannot be created.

    Notes
    -----
    This function MUST be ran from the project directory.
    e.g. python src/utils/prepreocess_data.py
    The cleaned data is saved as "clean_data.csv" in the relative path:
    "data/preprocessed". The 'preprocessed' directory will be created
    if it does not already exist.

    Example
    -------
    To clean the data and save it:
    
    >>> clean_and_save_data()
    Cleaned data saved to data/preprocessed/clean_data.csv
    """
    
    try:
        df = pd.read_csv("data/raw/googleplaystore.csv")

        df.drop(df[df['Rating'] > 5].index, inplace=True)
        df.reset_index(drop=True, inplace=True)

        category_means = df.groupby('Category')['Rating'].transform(lambda x: x.fillna(x.mean()))
        df['Rating'] = df['Rating'].fillna(category_means)

        df.drop(['Current Ver', 'Last Updated', 'Android Ver'], axis=1, inplace=True)

        df['Type'] = df.apply(lambda row: 'Free' if row['Price'] == 0 else 'Paid' if pd.isna(row['Type']) else row['Type'], axis=1)

        df['Installs'] = df['Installs'].str.replace(',', '').str.replace('+', '').astype(int)

        df['Reviews'] = df['Reviews'].astype(int)

        df['Rating'] = df['Rating'].round(1)
        
        df['Reviews_log'] = np.log1p(df['Reviews'])
    
        df['Installs_log'] = np.log1p(df['Installs'])
        
        df['Rating_normalized'] = (df['Rating'] - df['Rating'].min()) / (df['Rating'].max() - df['Rating'].min())
    
        df['Reviews_normalized'] = (df['Reviews_log'] - df['Reviews_log'].min()) / (df['Reviews_log'].max() - df['Reviews_log'].min())
    
        df['Installs_normalized'] = (df['Installs_log'] - df['Installs_log'].min()) / (df['Installs_log'].max() - df['Installs_log'].min())

        df['popularity_score'] = round((df['Rating_normalized'] + df['Reviews_normalized'] + df['Installs_normalized']) / 3, 5)
        
        category_popularity_avg = df.groupby('Category')['popularity_score'].mean().reset_index(name='avg_popularity_score')

        # Sort categories by average popularity_score in descending order and get top 10
        top_categories = category_popularity_avg.sort_values(by='avg_popularity_score', ascending=False).head(10)['Category'].tolist()
        df_score = df[df['Category'].isin(top_categories)]

        # Drop unncessary columns
        df_score = df_score.drop(["Size", "Price", "Genres"], axis=1)

        output_dir = "data/preprocessed"
        os.makedirs(output_dir, exist_ok=True)

        cleaned_file_path = os.path.join(output_dir, "clean_data.csv")
        df.to_csv(cleaned_file_path, index=False)

        print(f"Cleaned data saved to {cleaned_file_path}")
        
        cleaned_file_path_score = os.path.join(output_dir, "clean_data_score.csv")
        df_score.to_csv(cleaned_file_path_score, index=False)
        print(f"Cleaned data score saved to {cleaned_file_path_score}")

    except FileNotFoundError:
        print("Error: Raw data file not found at the specified path.")
    except FileExistsError:
        print("Error: Unable to create the output directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    clean_and_save_data()