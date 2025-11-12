{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ae8cffa1-6de8-4b99-8127-753b195acc03",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import numpy as np\n",
    "from joblib import load\n",
    "\n",
    "# Load the trained logistic regression model\n",
    "model = load('logistic_model.pk1')\n",
    "\n",
    "# Title of the web app\n",
    "st.title('Logistic Regression Model Deployment')\n",
    "\n",
    "# Subtitle and instruction for user\n",
    "st.header('Enter input values to predict')\n",
    "\n",
    "# Input fields (adjust these based on the features of your model)\n",
    "# Example: Feature names for your specific dataset\n",
    "age = st.number_input('Age', min_value=0, step=1)\n",
    "km = st.number_input('Kilometers Driven', min_value=0, step=1)\n",
    "hp = st.number_input('Horsepower', min_value=0, step=1)\n",
    "\n",
    "# Arrange the inputs in the correct format for the model\n",
    "input_data = np.array([[age, km, hp]])\n",
    "\n",
    "# Create a button for prediction\n",
    "if st.button('Predict'):\n",
    "    # Perform the prediction\n",
    "    prediction = model.predict(input_data)\n",
    "    st.write(f'Prediction: {prediction[0]}')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "03ac7ce3-431f-45ee-be46-c0851488e962",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
