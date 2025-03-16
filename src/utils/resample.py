import pandas as pd
import random

def sample_csv(input_file, output_file, sample_size=1000):
    # Load CSV file into a DataFrame
    df = pd.read_csv(input_file)
    
    # Ensure sample size is not greater than available rows
    sample_size = min(sample_size, len(df))
    
    # Randomly sample rows
    sampled_df = df.sample(n=sample_size, random_state=random.randint(0, 10000))
    
    # Save sampled data to a new CSV file
    sampled_df.to_csv(output_file, index=False)
    
    print(f"Sampled {sample_size} rows and saved to {output_file}")

# Example usage
#sample_csv("clean_data.csv", "sampled_clean_data.csv")
sample_csv("../../data/preprocessed/clean_data_score.csv", "../../data/preprocessed/clean_data_score_1000.csv")