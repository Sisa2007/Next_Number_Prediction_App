
import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

# Load model
@st.cache_resource
def load_trained_model():
    return load_model("simple_rnn_model.h5")

model = load_trained_model()

st.title("📈 RNN Sequence Predictor")
st.write("Enter 3 consecutive numbers (e.g., 88, 89, 90) to predict the next number using a trained RNN model.")

# Input fields
col1, col2, col3 = st.columns(3)
with col1:
    num1 = st.number_input("First number", value=88)
with col2:
    num2 = st.number_input("Second number", value=89)
with col3:
    num3 = st.number_input("Third number", value=90)

if st.button("Predict Next Number"):
    input_seq = np.array([num1, num2, num3]).reshape((1, 3, 1))
    prediction = model.predict(input_seq)
    st.success(f"🔮 Predicted next number: {prediction[0][0]:.2f}")
