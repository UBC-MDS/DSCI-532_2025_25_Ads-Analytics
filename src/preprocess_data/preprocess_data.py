import pandas as pd
import os

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
    The cleaned data is saved as "clean_data.csv" in the relative path:
    "../../data/preprocessed". The 'preprocessed' directory will be created
    if it does not already exist.

    Example
    -------
    To clean the data and save it:
    
    >>> clean_and_save_data()
    Cleaned data saved to ../../data/preprocessed/clean_data.csv
    """
    
    try:
        df = pd.read_csv("../../data/raw/googleplaystore.csv")

        df.drop(df[df['Rating'] > 5].index, inplace=True)
        df.reset_index(drop=True, inplace=True)

        category_means = df.groupby('Category')['Rating'].transform(lambda x: x.fillna(x.mean()))
        df['Rating'] = df['Rating'].fillna(category_means)

        df.drop(['Current Ver', 'Last Updated', 'Android Ver'], axis=1, inplace=True)

        df['Type'] = df.apply(lambda row: 'Free' if row['Price'] == 0 else 'Paid' if pd.isna(row['Type']) else row['Type'], axis=1)

        df['Installs'] = df['Installs'].str.replace(',', '').str.replace('+', '').astype(int)

        df['Reviews'] = df['Reviews'].astype(int)

        df['Rating'] = df['Rating'].round(1)

        output_dir = "../../data/preprocessed"
        os.makedirs(output_dir, exist_ok=True)

        cleaned_file_path = os.path.join(output_dir, "clean_data.csv")
        df.to_csv(cleaned_file_path, index=False)

        print(f"Cleaned data saved to {cleaned_file_path}")

    except FileNotFoundError:
        print("Error: Raw data file not found at the specified path.")
    except FileExistsError:
        print("Error: Unable to create the output directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    clean_and_save_data()