import pandas as pd
import json
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Step 1: LOAD data from CSV
def load_data(filename='banking_transactions_cleaned.csv'):
    """Load cleaned data from CSV"""
    try:
        logging.info(f"Loading data from {filename}...")
        df = pd.read_csv(filename)
        logging.info(f"Loaded {len(df)} records")
        return df
    except Exception as e:
        logging.error(f"Error loading data: {str(e)}")
        raise

# Step 2: ANALYZE - Customer Spending Patterns
def analyze_spending_patterns(df):
    """Analyze customer spending patterns"""
    try:
        logging.info("Analyzing spending patterns...")
        
        spending = df.groupby('account_number').agg({
            'amount': ['sum', 'mean', 'count'],
            'transaction_type': 'first'
        }).round(2)
        
        spending.columns = ['total_spent', 'avg_transaction', 'transaction_count', 'primary_type']
        spending = spending.sort_values('total_spent', ascending=False)
        
        logging.info("Spending pattern analysis completed")
        return spending
    
    except Exception as e:
        logging.error(f"Error in spending analysis: {str(e)}")
        raise

# Step 3: ANALYZE - Transaction Volume by Type
def analyze_transaction_volume(df):
    """Analyze transaction volume by type"""
    try:
        logging.info("Analyzing transaction volume...")
        
        volume = df['transaction_type'].value_counts().to_frame()
        volume.columns = ['count']
        volume['percentage'] = (volume['count'] / volume['count'].sum() * 100).round(2)
        
        logging.info("Transaction volume analysis completed")
        return volume
    
    except Exception as e:
        logging.error(f"Error in volume analysis: {str(e)}")
        raise

# Step 4: ANALYZE - Account-Level Analytics
def analyze_account_metrics(df):
    """Analyze account-level metrics"""
    try:
        logging.info("Analyzing account metrics...")
        
        account_metrics = df.groupby('account_number').agg({
            'amount': 'sum',
            'status': lambda x: (x == 'SUCCESS').sum(),
            'transaction_id': 'count'
        }).round(2)
        
        account_metrics.columns = ['total_amount', 'successful_transactions', 'total_transactions']
        account_metrics['success_rate'] = (account_metrics['successful_transactions'] / account_metrics['total_transactions'] * 100).round(2)
        account_metrics = account_metrics.sort_values('total_amount', ascending=False)
        
        logging.info("Account metrics analysis completed")
        return account_metrics
    
    except Exception as e:
        logging.error(f"Error in account metrics: {str(e)}")
        raise

# Step 5: EXPORT to CSV, JSON, HTML
def export_reports(spending, volume, account_metrics):
    """Export analysis to multiple formats"""
    try:
        logging.info("Exporting reports...")
        
        # CSV exports
        spending.to_csv('spending_patterns.csv')
        volume.to_csv('transaction_volume.csv')
        account_metrics.to_csv('account_metrics.csv')
        logging.info("CSV reports exported")
        
        # JSON exports
        spending.to_json('spending_patterns.json')
        volume.to_json('transaction_volume.json')
        account_metrics.to_json('account_metrics.json')
        logging.info("JSON reports exported")
        
        logging.info("All reports exported successfully")
    
    except Exception as e:
        logging.error(f"Error exporting reports: {str(e)}")
        raise

# Main Analytics Pipeline
if __name__ == "__main__":
    try:
        logging.info("=== Analytics Platform Started ===")
        
        # Load data
        df = load_data()
        
        # Analyze
        spending = analyze_spending_patterns(df)
        volume = analyze_transaction_volume(df)
        account_metrics = analyze_account_metrics(df)
        
        # Display results
        print("\n--- Spending Patterns ---")
        print(spending.head())
        
        print("\n--- Transaction Volume ---")
        print(volume)
        
        print("\n--- Account Metrics ---")
        print(account_metrics.head())
        
        # Export
        export_reports(spending, volume, account_metrics)
        
        logging.info("=== Analytics Platform Completed Successfully ===")
    
    except Exception as e:
        logging.error(f"Analytics pipeline failed: {str(e)}")

print("Spending shape:", spending.shape)
print("Volume shape:", volume.shape)
print("Account metrics shape:", account_metrics.shape)



# Step 6: CREATE HTML DASHBOARD
def create_html_dashboard(spending, volume, account_metrics):
    """Create HTML dashboard"""
    try:
        logging.info("Creating HTML dashboard...")
        
        output = open('banking_dashboard.html', 'w')
        output.write('')
        output.close()
        
        logging.info("Dashboard created")
        print("Dashboard file created successfully")
    
    except Exception as e:
        print(f"Error: {e}")


create_html_dashboard(spending, volume, account_metrics)