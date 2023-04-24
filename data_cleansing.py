import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("data.csv")

# Print the shape of the original dataset
print("Original Dataset Shape:", data.shape)

# Drop duplicates
data.drop_duplicates(inplace=True)
print("Dataset Shape after dropping duplicates:", data.shape)

# Fill missing values
data.fillna(method='ffill', inplace=True)
print("Dataset Shape after filling missing values:", data.shape)

# Rename columns
data.rename(columns={'col1': 'new_col1', 'col2': 'new_col2'}, inplace=True)

# Remove unnecessary columns
data.drop(columns=['unnecessary_col1', 'unnecessary_col2'], inplace=True)

# Normalize data
data['new_col1'] = (data['new_col1'] - np.mean(data['new_col1'])) / np.std(data['new_col1'])

# Create visualization
plt.hist(data['new_col1'], bins=50)
plt.title("Distribution of new_col1")
plt.xlabel("new_col1")
plt.ylabel("Frequency")
plt.show()

# Save cleaned dataset
data.to_csv("cleaned_data.csv", index=False)