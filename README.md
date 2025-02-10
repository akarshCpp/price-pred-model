# Real Estate Price Prediction

## Overview
This project aims to predict real estate prices using **XGBoost Regressor**. The model is trained on various property features such as **area, number of bedrooms (BHK), number of bathrooms, and square footage (int_sqft)**. The goal is to provide accurate price estimates based on these parameters.

## Features Used
- **area**: Location of the property
- **int_sqft**: Interior square footage of the property
- **n_bathroom**: Number of bathrooms
- **bhk**: Number of bedrooms, halls, and kitchens

## Data Preprocessing
- **Feature Engineering**: Selected important features for training.
- **Data Cleaning**: Removed missing or inconsistent values.
- **Outlier Detection**: Identified and removed extreme values.
- **One-Hot Encoding**: Converted categorical variables into numerical representations.
- **Scaling**: Applied **Min-Max Scaling** and **Standard Scaling** for better model performance.

## Model Details
- Model Used: **XGBRegressor**
- Parameters:
  - `learning_rate=0.7`
  - `n_estimators=100`
  - `verbosity=0`
- Achieved **R² Score: 0.99**

## Prediction Output Format
- The model predicts the property price and formats the output with commas for better readability.
- Example:
  - **Input:** `area='Velachery', int_sqft=1200, n_bathroom=2, bhk=3`
  - **Output:** `Predicted Price: 7,500,000`

## How to Use
1. Load the dataset and preprocess it.
2. Train the model using **XGBRegressor**.
3. Use the trained model to predict prices for new inputs.
4. Display the result in a readable format.

## Dependencies
- Python 3.x
- pandas
- numpy
- scikit-learn
- xgboost
- matplotlib (for data visualization)

## Future Improvements
- Adding more features like **age of the building, amenities, and proximity to landmarks**.
- Implementing a **web interface** for user-friendly price predictions.
- Deploying the model as an **API**.

