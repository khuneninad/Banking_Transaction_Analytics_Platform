from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route('/')
def dashboard():
    df = pd.read_csv('banking_transactions_cleaned.csv')
    
    total_accounts = len(df['account_number'].unique())
    total_amount = df['amount'].sum()
    total_transactions = len(df)
    
    spending = df.groupby('account_number')['amount'].sum().sort_values(ascending=False).head(10).to_frame()
    volume = df['transaction_type'].value_counts().to_frame()
    
    result = f""
    result += f""
    result += f""
    result += f""
    result += ""
    result += spending.to_html()
    result += ""
    result += volume.to_html()
    
    return result

if __name__ == '__main__':
    app.run(debug=True, port=5000)