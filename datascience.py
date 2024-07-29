import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Import Libraries and Load Data
df = pd.read_csv('sales_data.csv')  # Replace 'your_data.csv' with your actual file name

# 2. Clean and Preprocess Data
# Handle missing values (replace with appropriate strategy)
df.fillna(method='ffill', inplace=True)  # Example: Forward fill missing values

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Extract month from 'Date' column
df['Month'] = df['Date'].dt.month

# 3. Conduct Exploratory Data Analysis (EDA)
# Descriptive statistics
print(df.describe())

# Visualization
sns.histplot(df['Close'])
plt.title('Distribution of Closing Prices')
plt.show()

# Correlation matrix
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True)
plt.title('Correlation Matrix')
plt.show()

# 4. Draw Conclusions and Insights
# Example: Calculate average daily volume
average_volume = df['Volume'].mean()
print('Average Daily Volume:', average_volume)

# Identify top 5 days by volume
top_5_volume = df.nlargest(5, 'Volume')
print('Top 5 Days by Volume:')
print(top_5_volume)

# Additional analysis and visualizations based on specific requirements
