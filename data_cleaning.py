import pandas as pd

def clean_data(df):
    # Remove duplicates
    df = df.drop_duplicates()
    # Fill missing values (example)
    df['age'] = df['age'].fillna(df['age'].mean())
    return df