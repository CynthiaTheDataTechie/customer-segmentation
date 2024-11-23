import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df, columns_to_scale):
    """
    Preprocess data by scaling specified columns using StandardScaler.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
        columns_to_scale (list): List of column names to scale.
    
    Returns:
        pd.DataFrame: DataFrame with scaled columns.
    """
    scaler = StandardScaler()
    df[columns_to_scale] = scaler.fit_transform(df[columns_to_scale])
    return df
