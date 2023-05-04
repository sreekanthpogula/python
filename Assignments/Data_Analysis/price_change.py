import pandas as pd

# Load the data into a DataFrame
df = pd.read_csv('data.csv')

# Compute the rolling mean and standard deviation of the price_change column
rolling_mean = df.groupby('id')['price_change'].rolling(window=120, min_periods=1).mean().reset_index(level=0, drop=True)
rolling_std = df.groupby('id')['price_change'].rolling(window=120, min_periods=1).std().reset_index(level=0, drop=True)

# Compute the outlier score for each row
outlier_score = (df['price_change'] - rolling_mean) / rolling_std

# Check if any outlier score is greater than 5
is_outlier = (outlier_score.abs() > 5)

# Add a new column to the DataFrame indicating whether each row is an outlier or not
df['is_outlier'] = is_outlier.astype(int)

# Save the result to a new CSV file
df.to_csv('result.csv', index=False)
