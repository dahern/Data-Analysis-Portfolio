# Data-Cleansing

The data-cleansing branch contains all the code and scripts used to clean the raw data before analysis. 
This branch was created to ensure that the data used in the analysis is accurate and consistent.

# data-cleansing.py
A Python file that demonstrates data cleaning and preprocessing using the Pandas library. 
This example focuses on cleaning a dataset with missing values, inconsistent formatting, and duplicate entries.

In this example, we use **Pandas** to load the dataset and then perform several cleaning and preprocessing steps:

We drop any **duplicate** entries using the drop_duplicates method.
We fill any missing values using the **fillna** method and the forward-fill method.
We rename columns using the **rename** method.
We remove unnecessary columns using the **drop** method.
We normalize the data using the mean and standard deviation.
We create a histogram visualization using **Matplotlib**.
We save the cleaned dataset to a new CSV file using the **to_csv** method.

This example demonstrates how we can use Python and Pandas to clean and preprocess a messy dataset, and then create visualizations to show the before and after.
