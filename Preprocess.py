import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(input_file="raw_data.csv", output_file="processed_data.csv"):
    # Step 1: Load raw data
    df = pd.read_csv(input_file)
    
    # Step 2: Handle missing values (if any)
    if df.isnull().values.any():
        df = df.fillna(method='ffill')  # Forward fill (you can use other methods)
    
    # Step 3: Normalize numerical fields (Temperature and Wind Speed)
    scaler = MinMaxScaler()
    df[["Temperature", "Wind Speed"]] = scaler.fit_transform(df[["Temperature", "Wind Speed"]])
    
    # Step 4: Save processed data
    df.to_csv(output_file, index=False)
    print(f"Preprocessed data saved to {output_file}")

# Example Usage
if __name__ == "__main__":
    preprocess_data()
