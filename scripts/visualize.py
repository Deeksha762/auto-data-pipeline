import pandas as pd
import matplotlib.pyplot as plt

def make_chart(clean_file=r"C:\Users\DELL\Desktop\auto-data-pipeline\auto-data-pipeline\output\clean.csv", out_file=r"C:\Users\DELL\Desktop\auto-data-pipeline\auto-data-pipeline\output\chart.png"):
    df = pd.read_csv(clean_file)
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    monthly = (df
               .groupby(pd.Grouper(key="Order Date", freq="M"))['revenue']
               .sum()
               .reset_index())
    plt.figure(figsize=(8,4))
    plt.bar(monthly['Order Date'].dt.strftime("%Y-%m"), monthly['revenue'])
    plt.xticks(rotation=45, ha='right')
    plt.title("Monthly Revenue")
    plt.tight_layout()
    plt.savefig(out_file)
    print(f"Chart saved to {out_file}")

if __name__ == "__main__":
    make_chart()
