import streamlit as st
import pandas as pd
import pickle

# Load the saved model
model = pickle.load(open('real_estate_price_model.pkl', 'rb'))

# Load the saved scaler (optional, only if you used one)
# mm = pickle.load(open('scaler.pkl', 'rb'))

# Define available areas
areas = ['Anna Nagar', 'T Nagar', 'Velachery', 'Chrompet', 'Karapakkam', 'KK Nagar', 'Adyar']

# App title and layout
st.set_page_config(page_title="Real Estate Price Predictor 🏡", page_icon="🏠", layout="centered")

st.title("🏙️ Real Estate Price Prediction App")
st.write("Predict property prices across popular Chennai areas using Machine Learning (XGBoost Model).")

# Sidebar input fields
st.sidebar.header("Enter Property Details 🧾")

area = st.sidebar.selectbox("Select Area", areas)
int_sqft = st.sidebar.number_input("Enter Square Feet (sqft):", min_value=200, max_value=10000, step=50)
n_bathroom = st.sidebar.number_input("Number of Bathrooms:", min_value=1, max_value=10, step=1)
bhk = st.sidebar.number_input("Number of BHK:", min_value=1, max_value=10, step=1)

# Predict button
if st.sidebar.button("Predict Price 💰"):
    # Prepare input DataFrame
    input_data = pd.DataFrame([{
        'area': area,
        'int_sqft': int_sqft,
        'n_bathroom': n_bathroom,
        'bhk': bhk
    }])

    # One-hot encode the area feature
    input_data = pd.get_dummies(input_data, columns=['area'])

    # Reindex to match model training columns
    # You must have your X_train columns saved earlier
    # Example: columns_list.pkl
    try:
        cols = pickle.load(open('columns_list.pkl', 'rb'))
        input_data = input_data.reindex(columns=cols, fill_value=0)
    except:
        st.warning("⚠️ Columns file not found! Please save your X_train columns as columns_list.pkl.")
        st.stop()

    # If you used scaling, apply it
    # input_data_scaled = mm.transform(input_data)
    # prediction = model.predict(input_data_scaled)

    # If no scaling:
    prediction = model.predict(input_data)

    # Format predicted price
    price = prediction[0]
    formatted_price = f"₹ {price:,.0f}".replace(",", ",")
    st.success(f"🏠 **Predicted Price for {area}: {formatted_price}**")

st.markdown("---")
st.markdown("📘 *Model used: XGBRegressor | Data source: projecthms*")
