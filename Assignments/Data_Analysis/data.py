import pandas as pd
import numpy as np
import datetime

# Define start and end date
end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=119)

# Create a range of dates
date_range = pd.date_range(start=start_date, end=end_date)

# Generate random price change values
price_change = np.random.randn(len(date_range))

# Create a DataFrame with id, date, and price_change columns
data = pd.DataFrame({'id': 1, 'date': date_range, 'price_change': price_change})

# Save DataFrame to CSV file
data.to_csv('data.csv', index=False)
