# Mobile Phone Price Prediction Project
## Overview
This project focuses on predicting mobile phone prices using machine learning techniques. The dataset used contains information about various mobile phone models including their brand, model name, RAM, storage, and price.

## Files
mobile_phone_price.csv: This is the dataset containing information about mobile phones.
main.py: This is the Python script containing the code for data preprocessing and modeling.
Code Explanation
The project is divided into two main parts:

### Part 1: Filling Missing Values (Method 1)
In this part, missing values are filled using a combination of manual techniques and pandas functions. The steps include:
  Importing necessary libraries and reading the CSV file into a DataFrame.
  Preprocessing the data by cleaning and converting data types.
  Filling missing values using method 1 which involves replacing missing values in 'Brand' and 'Model' with 'missing', filling missing 'RAM' and 'Storage' values with their respective means, and dropping any remaining rows with missing values.
  Printing the number of missing values before and after applying method 1.

### Part 2: Filling Missing Values (Imputer Method)
In this part, missing values are filled using the scikit-learn SimpleImputer along with ColumnTransformer. The steps include:
  Re-reading the CSV file into a new DataFrame.
  Preprocessing the data as in Part 1.
  Dropping rows with missing 'Price' values.
  Separating features (x) and target variable (y).
  Importing necessary libraries for imputation.
  Defining imputation strategies for different features ('Brand', 'Model', 'RAM', 'Storage').
  Applying imputation using ColumnTransformer.
  Printing the number of missing values after applying the imputer method.

## Learnings and Insights
1. Data Preprocessing: Data cleaning and type conversion are crucial steps before applying machine learning models. In this project, we cleaned 'Price' by removing special characters and converting it to float, and similarly processed 'RAM' and 'Storage' columns.
2. Handling Missing Values: There are multiple ways to handle missing data. Method 1 involved a combination of manual filling and dropping rows, while the Imputer Method used scikit-learn's SimpleImputer along with ColumnTransformer to systematically fill missing values based on defined strategies.
3. Comparing Methods: It's important to compare the effectiveness of different methods for handling missing values. Method 1 is more manual and may not always be the most efficient, while the Imputer Method provides a structured approach.
4. GitHub Repository Usage: This project is structured for easy sharing and collaboration on GitHub. The code is organized into separate files, making it clear and accessible for others.

## Output
### Part 1: Filling Missing Values (Method 1)

phones_csv_1 before adding missing values by method 1
Brand         0
Model         3
RAM           2
Storage       1
Price ($)     0
dtype: int64

phones_csv_1 after adding missing values by method 1
Brand         0
Model         0
RAM           0
Storage       0
Price ($)     0
dtype: int64

### Part 2: Filling Missing Values (Imputer Method)

phones_csv_2 before adding missing values by imputer method
Brand         0
Model         3
RAM           2
Storage       1
Price ($)     3
dtype: int64

phones_csv_2 after adding missing values by imputer method
Brand         0
Model         0
RAM           0
Storage       0
dtype: int64

## Acknowledgments:
This program was created as part of the AI, DS and Machine Learning course offered by the National Emerging Skills Program (NESP).
