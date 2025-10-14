🏠 Real Estate Price Prediction using XGBoost
📘 Overview

This project predicts property prices based on key features such as area, square footage, number of bathrooms, and BHK. Using XGBoost Regressor, the model achieves high accuracy and provides reliable price predictions. A simple Streamlit web app allows users to interact with the model and get instant predictions.

🎯 Objectives

Build a predictive model that estimates real estate prices.

Use feature engineering and scaling to improve accuracy.

Compare multiple ML algorithms and finalize the best one.

Deploy the model using an interactive Streamlit interface.

💡 Key Features

Supports multiple Chennai areas: Anna Nagar, T Nagar, Velachery, Chrompet, Karapakkam, KK Nagar, Adyar.

Model trained with XGBoost Regressor for best performance.

Input scaling using MinMaxScaler and StandardScaler.

Outputs predictions in Indian Rupee format (e.g., ₹5,67,890).

Includes .pkl files for easy model loading in the app.

🧠 Machine Learning Workflow

Data Cleaning: Removed missing and irrelevant data.

Feature Engineering: Converted categorical data to numeric (One-Hot Encoding).

Scaling: Applied Min-Max and Standard Scalers.

Model Selection: Compared Linear, Ridge, Lasso, RandomForest, and XGBoost.

Model Building: Finalized XGBoost Regressor with an R² score of 0.99.

Export: Saved trained model as model.pkl and columns as columns_list.pkl.

⚙️ Installation & Setup

Clone this repository:

git clone https://github.com/your-username/real-estate-predictor.git
cd real-estate-predictor


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py

🧩 Files in the Project
File Name	Description
app.py	Streamlit web application
model.pkl	Trained XGBoost model
columns_list.pkl	Feature list used during training
requirements.txt	Python dependencies
README.md	Project documentation
data.csv	Dataset used for model training (optional)
🧪 Example Prediction
Area	Int Sqft	Bathrooms	BHK	Predicted Price
Anna Nagar	1000	2	2	₹56,78,907
T Nagar	1200	1	1	₹45,32,100
📊 Results

✅ Best Model: XGBoost Regressor

✅ R² Score: 0.99

✅ MAE: Very Low

✅ RMSE: Optimized

🚀 Future Enhancements

Add more features like furnishing, floor, and age of the property.

Integrate a map-based UI for area selection.

Use live data for dynamic price updates.

