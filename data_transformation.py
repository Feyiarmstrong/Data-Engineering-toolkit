
def transform_data(df):
    # Example: uppercase names
    df['name'] = df['name'].str.upper()
    return df