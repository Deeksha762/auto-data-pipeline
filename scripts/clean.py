import pandas as pd

def clean_data(input_file=r"C:\Users\DELL\Desktop\auto-data-pipeline\auto-data-pipeline\data\all_data.csv", output_file=r"C:\Users\DELL\Desktop\auto-data-pipeline\auto-data-pipeline\output\clean.csv"):
    df = pd.read_csv(input_file)
    # Basic cleaning
    df = df.dropna()
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'], errors='coerce')
    df['Price Each'] = pd.to_numeric(df['Price Each'], errors='coerce')
    df["revenue"]=df["Quantity Ordered"] * df["Price Each"]
    df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
    df = df.dropna(subset=['Order Date', 'revenue'])
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
    clean_data()
