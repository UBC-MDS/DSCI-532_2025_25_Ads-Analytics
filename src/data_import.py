# data_preprocessing.py
import pandas as pd

def load_data(filepath):
    """
    Load the dataset from the specified filepath.
    
    Parameters:
    filepath (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: The loaded DataFrame.
    """
    return pd.read_csv(filepath)

def get_dropdown_options(df, column):
    """
    Generates a list of options for a dropdown menu based on the unique values in a specified column of the DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.
    column (str): The name of the column in the DataFrame for which to generate dropdown options.

    Returns:
    list: A list of dictionaries, where each dictionary contains 'label' and 'value' keys, 
          with 'All' as the first option and the unique values of the specified column as subsequent options.
    """
    unique_values = sorted(df[column].dropna().unique())
    options = [{"label": "All", "value": "All"}] + [{"label": value, "value": value} for value in unique_values]
    return options