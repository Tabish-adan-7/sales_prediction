# Import Reguired Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(filepath):
    """Load data from CSV file"""
    try:
        data = pd.read_csv(filepath)
        print(f"Successfully loaded data with shape {data.shape}")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None


def perform_eda(data):
    """Perform exploratory data analysis"""
    print("\n=== EXPLORATORY DATA ANALYSIS ===")

    # Basic data inspection
    print("\nFirst 5 rows:")
    print(data.head())

    print("\nData Information:")
    print(data.info())

    print("\nMissing Values:")
    print(data.isnull().sum())

    print("\nDescriptive Statistics:")
    print(data.describe())

    print("\nCorrelation Matrix:")
    print(data.corr())


def visualize_data(data):
    """Create visualizations for EDA"""
    print("\n=== DATA VISUALIZATIONS ===")

    # Set style
    sns.set(style="whitegrid")
    plt.figure(figsize=(15, 10))

    # Scatter plots
    print("\nCreating scatter plots...")
    features = ['TV', 'Radio', 'Newspaper']
    for i, feature in enumerate(features, 1):
        plt.subplot(2, 2, i)
        sns.scatterplot(data=data, x=feature, y='Sales')
        plt.title(f'Sales vs {feature}')
    plt.tight_layout()
    plt.show()

    # Pair plot
    print("\nCreating pair plot...")
    sns.pairplot(data)
    plt.show()

    # Heatmap
    print("\nCreating correlation heatmap...")
    plt.figure(figsize=(8, 6))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Heatmap')
    plt.show()


def preprocess_data(data):
    """Prepare data for modeling"""
    print("\n=== DATA PREPROCESSING ===")

    # Handle missing values
    if data.isnull().sum().sum() > 0:
        print("Missing values detected - handling them...")
        data = data.dropna()
    else:
        print("No missing values found")

    # Check for categorical variables
    categorical_cols = data.select_dtypes(include=['object']).columns
    if not categorical_cols.empty:
        print(f"Categorical variables found: {list(categorical_cols)}")
        data = pd.get_dummies(data, columns=categorical_cols)
    else:
        print("No categorical variables to encode")

    # Separate features and target
    X = data[['TV', 'Radio', 'Newspaper']]
    y = data['Sales']

    # Combine and save as one file
    preprocessed_df = X.copy()
    preprocessed_df['Sales'] = y
    preprocessed_df.to_csv("D:/advertisement_prediction/sales/preprocessed_data.csv", index=False)
    print(" Preprocessed data saved as preprocessed_data.csv")

    print("\nPreprocessing complete!")
    print(f"Features shape: {X.shape}")
    print(f"Target shape: {y.shape}")

    return X, y



def main():
    """Main execution flow"""
    # Load data
    data = load_data(r"D:\advertisement_prediction\sales\advertising.csv")
    if data is None:
        return

    # Perform EDA
    perform_eda(data)

    # Visualize data
    visualize_data(data)

    # Preprocess data
    X, y = preprocess_data(data)

    return X, y


if __name__ == "__main__":
    X, y = main()