import streamlit as st
import tensorflow as tf
import numpy as np

@st.cache_resource
def load_model():
    # Replace this with your actual model-loading logic
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(10, activation='relu', input_shape=(1,)),
        tf.keras.layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

def main():
    st.title("Next Number Prediction")
    model = load_model()
    user_input = st.number_input("Enter a number:", value=1)
    if st.button("Predict Next"):
        prediction = model.predict(np.array([[user_input]]), verbose=0)
        st.write(f"Predicted next number: {prediction[0][0]:.2f}")

if __name__ == "__main__":
    main()
