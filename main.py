# Importing the necessary libraries
import pandas as pd

# Reading the CSV file into a DataFrame
phones_csv_1 = pd.read_csv('Mobile phone price.csv')

# Printing the number of missing values before any modifications
print('phones_csv_1 before adding missing values by method 1')
print(phones_csv_1.isna().sum())

# Preprocessing: Cleaning and converting data types
phones_csv_1['Price ($)'] = phones_csv_1['Price ($)'].str.replace('$', '')
phones_csv_1['Price ($)'] = phones_csv_1['Price ($)'].str.replace(',', '').astype(float)
phones_csv_1['RAM '] = phones_csv_1['RAM '].str.replace('GB', '').astype(float)
phones_csv_1['Storage '] = phones_csv_1['Storage '].str.replace('GB', '').astype(float)

# Filling missing values using method 1
phones_csv_1['Brand'].fillna('missing', inplace=True)
phones_csv_1['Model'].fillna('missing', inplace=True)
phones_csv_1['Storage '].fillna(phones_csv_1['Storage '].mean(), inplace=True)
phones_csv_1['RAM '].fillna(phones_csv_1['RAM '].mean(), inplace=True)
phones_csv_1.dropna(inplace=True)

# Printing the number of missing values after method 1
print('phones_csv_1 after adding missing values by method 1')
print(phones_csv_1.isna().sum())

# Re-reading the CSV file into a new DataFrame
phones_csv_2 = pd.read_csv('Mobile phone price.csv')

# Printing the number of missing values before any modifications
print('phones_csv_2 before adding missing values by imputer method')
print(phones_csv_2.isna().sum())

# Preprocessing: Cleaning and converting data types
phones_csv_2['Price ($)'] = phones_csv_2['Price ($)'].str.replace('$', '')
phones_csv_2['Price ($)'] = phones_csv_2['Price ($)'].str.replace(',', '').astype(float)
phones_csv_2['RAM '] = phones_csv_2['RAM '].str.replace('GB', '').astype(float)
phones_csv_2['Storage '] = phones_csv_2['Storage '].str.replace('GB', '').astype(float)

# Dropping rows with missing Price values
phones_csv_2.dropna(subset=['Price ($)'], inplace=True)

# Separating features (x) and target variable (y)
x = phones_csv_2.drop('Price ($)', axis=1)
y = phones_csv_2['Price ($)']

# Importing necessary libraries for imputation
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

# Defining imputation strategies for different features
brand_feature = SimpleImputer(strategy='constant', fill_value='missing')
ram_feature = SimpleImputer(strategy='constant', fill_value=8)
storage_feature = SimpleImputer(strategy='mean')

brand_feature_col = ['Brand', 'Model']
ram_feature2_col = ['RAM ']
storage_feature2_col = ['Storage ']

# Applying imputation using ColumnTransformer
imputer = ColumnTransformer([('brand_feature', brand_feature, brand_feature_col),
                             ('ram_feature', ram_feature, ram_feature2_col),
                             ('storage_feature', storage_feature, storage_feature2_col)])

filled_x = imputer.fit_transform(x)
filled_x_df = pd.DataFrame(filled_x, columns=['Brand', 'Model', "RAM ", "Storage "])

# Printing the number of missing values after imputer method
print('phones_csv_2 after adding missing values by imputer method')
print(filled_x_df.isna().sum())
