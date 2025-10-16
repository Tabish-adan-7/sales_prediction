import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns


#Title and description
st.title("Sales predition based on advertisement spends")
st.write("""
This app predicts Sales based on your advertisements spending on TV, Radio, and Newspaper""")

model = joblib.load(r"D:\advertisement_prediction\sales\advertising_model.joblib")

#sidebar for user input
st.sidebar.header("Enter advertisement spend")

tv = st.sidebar.slider("TV Advertisement spend",min_value=0.0,max_value=1000.0,value=100.0,step=1.0)
radio =st.sidebar.slider("Radio advertisement spend", min_value=0.0,max_value=500.0,value=25.0,step=1.0)
newspaper= st.sidebar.slider("Newspaper advertisement spend",min_value=0.0,max_value=700.0,value=30.0,step=1.0)

#Convert input to a dataframes for prediction
input_data=pd.DataFrame({
    'TV':[tv],
    'Radio':[radio],
    'Newspaper':[newspaper]
})

#prediction
if st.sidebar.button("Predict sales"):
    prediction = model.predict(input_data)[0]
    st.subheader("predict Sales")
    st.success(f"estimated sales: {prediction:.2f} units")

    #prepare CSV for download
    result_df = input_data.copy()
    result_df['predicted sales'] = prediction

    csv= result_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download prediction as CSV",
        data=csv,
        file_name='sales_prediction.csv',
        mime='text/csv'

    )

st.markdown("---")
st.subheader("About This App")
st.write("""
This Sales Prediction app was built using **Linear Regression** and trained on an Advertisement dataset.  
It predicts sales based on money spent on **TV**, **Radio**, and **Newspaper** ads.

**How it works:**
1. Enter your ad spend values in the sidebar.
2. Click "Predict Sales" to get the estimated sales.
3. Optionally, download your prediction as a CSV file.

**Note:** Predictions are based on historical data patterns and may not reflect real-world results exactly.
""")