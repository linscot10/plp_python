# Import necessary libraries
import pandas as pd
import numpy as np

# Load the dataset (assuming the file is named 'data.csv')
df = pd.read_csv('data.csv')

# Display the first few rows of the dataset
df.head()


# Get a summary of the dataset including column names, data types, and non-null counts
df.info()

# Check for missing values
missing_values = df.isnull().sum()

# Describe the basic statistics for numerical columns
df.describe()


# If applicable, check correlations between numeric variables
correlation_matrix = df.corr()

# Example of grouping and summarizing data by a specific category (if applicable)
# Assuming we have a categorical column 'Category' and a numeric column 'Value'
category_summary = df.groupby('Category')['Value'].mean()

category_summary


# Import necessary libraries for plotting
import matplotlib.pyplot as plt
import seaborn as sns

# Create a histogram for a numerical column 'Value'
plt.figure(figsize=(8, 6))
sns.histplot(df['Value'], kde=True)
plt.title('Distribution of Value')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Create a boxplot for numerical data
plt.figure(figsize=(8, 6))
sns.boxplot(x='Category', y='Value', data=df)
plt.title('Boxplot of Value by Category')
plt.show()

# Create a heatmap of the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()
