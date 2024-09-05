# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Loading the dataset
data = pd.read_csv('data_insurance.csv')

# Step 2: Exploring the dataset
print(data.head())          
print(data.info())          
print(data.describe())      

# Step 3: Checking for missing values
print(data.isnull().sum())  

# Step 4: Converting categorical variables into numerical values using one-hot encoding for all categorical columns
data['sex'] = data['sex'].apply(lambda x: 1 if x == 'female' else 0)
data['smoker'] = data['smoker'].apply(lambda x: 1 if x == 'yes' else 0)
data = pd.get_dummies(data, drop_first=True)  

# Step 5: Defining features (X) and target (y)
X = data.drop('charges', axis=1)  
y = data['charges']               

# Step 6: Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 7: Training the Ridge Regression model
model = Ridge(alpha=1.0)  # Ridge regression is used as an alternative to standard linear regression
model.fit(X_train, y_train)

# Step 8: Make predictions using the test dataset
y_pred = model.predict(X_test)

# Step 9: Evaluating the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R²): {r2:.2f}")

# Step 10: Analyzing the model coefficients
coefficients = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_,
    'Absolute Coefficient': np.abs(model.coef_)
})

print("\nModel Coefficients:\n", coefficients)

# Step 11: Sorting coefficients by their absolute values to identify the most influential features
sorted_coefficients = coefficients.sort_values(by='Absolute Coefficient', ascending=False)
print("\nSorted Coefficients by Absolute Value:\n", sorted_coefficients)
