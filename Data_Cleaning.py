import csv
import os
import pandas as pd

#load data as a data frame from a CSV file
def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: The loaded data as a DataFrame.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        raise Exception(f"Error loading data from {file_path}: {e}")
    

#count the number of missing values in each column
def count_missing_values(data):
    """
    Count the number of missing values in each column of the DataFrame.
    
    Parameters:
    data (pd.DataFrame): The DataFrame to check for missing values.
    
    Returns:
    pd.Series: A Series with the count of missing values for each column.
    """
    return data.isnull().sum()

    # Save the cleaned data to a new CSV file
def save_cleaned_data(data, output_file_path):
    """
    Save the cleaned DataFrame to a CSV file.
    
    Parameters:
    data (pd.DataFrame): The DataFrame to save.
    output_file_path (str): The path where the cleaned data will be saved.
    """
    try:
        data.to_csv(output_file_path, index=False)
        print(f"Cleaned data saved to {output_file_path}")
    except Exception as e:
        raise Exception(f"Error saving cleaned data to {output_file_path}: {e}")
if __name__ == "__main__":
    base_dir = os.path.expanduser("~/Documents/GitHub/DHF_Home-Loan-Automation/Assets/Datasets/")
    file_path = os.path.join(base_dir, "loan_sanction_train.csv")
    output_file_path = os.path.join(base_dir, "cleaned_loan_sanction_train.csv")

    try:
        df = load_data(file_path)
        print("Data loaded successfully:")
        print(df.head())  # Display the first few rows of the DataFrame

        # Count missing values
        missing_values = count_missing_values(df)
        print("Missing values in each column:")
        print(missing_values)

        # Drop rows with missing values in selected columns
        list_columns = ['Credit_History', 'Self_Employed', 'Gender', 'Dependents', 'Married', 'Education']
        existing_columns = [col for col in list_columns if col in df.columns]
        if existing_columns:
            df = df.dropna(subset=existing_columns)
            print("Dropped rows with missing values in:", existing_columns)
        else:
            print("Warning: None of the specified columns exist in the dataset.")


        #Fill missing values for specific numeric columns
        required_columns = ['LoanAmount', 'Loan_Amount_Term']
        missing_cols = [col for col in required_columns if col not in df.columns]

        if not missing_cols:
            df['LoanAmount'].fillna(df['LoanAmount'].mean(), inplace=True)
            df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mean(), inplace=True)
            print("Filled missing values with mean.")
            missing_values = count_missing_values(df)
            print(missing_values)
        else:
            print(f"Warning: Missing columns {missing_cols}. Data may be incomplete.")

        #Save cleaned data
        save_cleaned_data(df, output_file_path)
        print("Data cleaning and saving completed successfully.")

    except Exception as e:
        print("Error:", str(e))
