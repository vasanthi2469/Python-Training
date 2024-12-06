import numpy as np
import pandas as pd

# NumPy examples
# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.zeros((3, 3))
arr3 = np.random.rand(4, 4)  # Random values between 0 and 1

# Basic array operations
print("Array operations:")
print("Sum:", arr1.sum())
print("Mean:", arr1.mean())
print("Standard deviation:", arr1.std())
print("Reshape:", arr1.reshape(5, 1))

# Pandas examples
# Creating a DataFrame
data = {
    'Name': ['John', 'Emma', 'Alex', 'Sarah'],
    'Age': [28, 24, 32, 27],
    'City': ['New York', 'London', 'Paris', 'Tokyo'],
    'Salary': [75000, 65000, 85000, 70000]
}
df = pd.DataFrame(data)

# Basic DataFrame operations
print("\nDataFrame operations:")
print("\nOriginal DataFrame:")
print(df)

# Filtering data
print("\nEmployees older than 25:")
print(df[df['Age'] > 25])

# Sorting data
print("\nSorted by Salary (descending):")
print(df.sort_values('Salary', ascending=False))

# Basic statistics
print("\nSummary statistics:")
print(df.describe())

# Grouping and aggregation
print("\nAverage salary by city:")
print(df.groupby('City')['Salary'].mean())

# Export to CSV
df.to_csv('employee_data.csv', index=False)
