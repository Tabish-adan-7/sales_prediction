# 📊 Sales Prediction Based on Advertisement Spend

## Overview
This project predicts product sales based on advertisement spending across three channels: **TV**, **Radio**, and **Newspaper**. It includes a complete data pipeline for loading, exploring, visualizing, and preprocessing the dataset, followed by a user-friendly Streamlit app for real-time predictions.

---

## 🔧 Project Structure

```
advertisement_prediction/
│
├── sales/
│   ├── advertising.csv                # Original dataset
│   ├── preprocessed_data.csv         # Cleaned and processed dataset
│   ├── advertising_model.joblib      # Trained Linear Regression model
│   ├── eda_pipeline.py               # Python script for EDA and preprocessing
│   └── app.py                        # Streamlit user interface
```

---

## 📁 Dataset Description

- **Source**: `advertising.csv`
- **Columns**:
  - `TV`: Budget spent on TV ads
  - `Radio`: Budget spent on radio ads
  - `Newspaper`: Budget spent on newspaper ads
  - `Sales`: Actual sales figures

---

## 🧪 Backend Pipeline (`eda_pipeline.py`)

### Key Functions:
- `load_data(filepath)`: Loads CSV data and prints shape.
- `perform_eda(data)`: Displays head, info, missing values, statistics, and correlation.
- `visualize_data(data)`: Generates scatter plots, pair plots, and heatmaps.
- `preprocess_data(data)`: Handles missing values, encodes categorical variables, and saves cleaned data.
- `main()`: Executes the full pipeline and returns features and target variables.

### Output:
- Cleaned dataset saved as `preprocessed_data.csv`
- Ready-to-use features (`X`) and target (`y`) for model training

---

## 🧠 Model Training

- **Algorithm**: Linear Regression
- **Input Features**: TV, Radio, Newspaper
- **Target**: Sales
- **Output**: Saved model as `advertising_model.joblib`

---

## 🌐 Streamlit App (`app.py`)

### Features:
- Interactive sliders for TV, Radio, and Newspaper ad spend
- Real-time prediction of sales using the trained model
- Option to download prediction as a CSV file
- Informative "About" section explaining the app's purpose

### How to Use:
1. Launch the app:  
   ```bash
   streamlit run app.py
   ```
2. Adjust ad spend values in the sidebar
3. Click **"Predict Sales"**
4. View the estimated sales and download results

---

## 📦 Requirements

Install dependencies using pip:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit joblib
```

---

## ⚠️ Disclaimer

Predictions are based on historical data and a simple linear model. They may not reflect real-world outcomes precisely. Use this tool for educational or exploratory purposes.

---

## 🙌 Credits

Developed by Muhammad Tabish Adan  
Powered by Python, Streamlit, and Scikit-learn

---

