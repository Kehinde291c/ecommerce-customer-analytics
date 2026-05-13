"""
Generate synthetic e-commerce customer data for analysis.
This creates a realistic dataset with customer demographics, purchase history,
and engagement metrics.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Number of customers
n_customers = 5000

# Generate customer data
customer_ids = [f'CUST{str(i).zfill(5)}' for i in range(1, n_customers + 1)]

# Demographics
ages = np.random.normal(38, 12, n_customers).astype(int)
ages = np.clip(ages, 18, 75)

genders = np.random.choice(['Male', 'Female', 'Other'], n_customers, p=[0.48, 0.48, 0.04])

locations = np.random.choice(
    ['Urban', 'Suburban', 'Rural'], 
    n_customers, 
    p=[0.45, 0.40, 0.15]
)

# Account age in days
account_age_days = np.random.gamma(2, 180, n_customers).astype(int)
account_age_days = np.clip(account_age_days, 30, 1095)  # 1 month to 3 years

# Purchase behavior
total_purchases = np.random.negative_binomial(3, 0.3, n_customers)
total_purchases = np.clip(total_purchases, 0, 50)

# Average order value
avg_order_value = np.random.gamma(3, 30, n_customers)
avg_order_value = np.clip(avg_order_value, 15, 500)

# Total revenue per customer
total_revenue = total_purchases * avg_order_value

# Days since last purchase (recency)
days_since_last_purchase = np.random.exponential(45, n_customers).astype(int)
days_since_last_purchase = np.clip(days_since_last_purchase, 0, 365)

# For churned customers, make this higher
churn_probability = 1 / (1 + np.exp(-(days_since_last_purchase - 90) / 20))
is_churned = np.random.binomial(1, churn_probability)

# Engagement metrics
email_open_rate = np.random.beta(2, 3, n_customers)
email_open_rate = np.where(is_churned, email_open_rate * 0.5, email_open_rate)

website_visits_per_month = np.random.poisson(8, n_customers)
website_visits_per_month = np.where(is_churned, website_visits_per_month // 3, website_visits_per_month)

# Product preferences
product_categories = ['Electronics', 'Fashion', 'Home & Garden', 'Books', 'Sports', 'Beauty']
primary_category = np.random.choice(product_categories, n_customers)

# Customer satisfaction (1-5 scale)
satisfaction_score = np.random.normal(3.8, 0.8, n_customers)
satisfaction_score = np.clip(satisfaction_score, 1, 5)
satisfaction_score = np.where(is_churned, satisfaction_score - 0.8, satisfaction_score)

# Support tickets
support_tickets = np.random.poisson(1.2, n_customers)
support_tickets = np.where(is_churned, support_tickets * 1.5, support_tickets).astype(int)

# Discount usage
discount_usage_rate = np.random.beta(2, 5, n_customers)

# Mobile app usage
uses_mobile_app = np.random.binomial(1, 0.65, n_customers)

# Newsletter subscription
newsletter_subscribed = np.random.binomial(1, 0.70, n_customers)
newsletter_subscribed = np.where(is_churned, newsletter_subscribed * 0.6, newsletter_subscribed).astype(int)

# Customer lifetime value (CLV) estimate
clv = total_revenue + (total_revenue * 0.3 * (1 - is_churned))

# Create DataFrame
df = pd.DataFrame({
    'customer_id': customer_ids,
    'age': ages,
    'gender': genders,
    'location': locations,
    'account_age_days': account_age_days,
    'total_purchases': total_purchases,
    'avg_order_value': np.round(avg_order_value, 2),
    'total_revenue': np.round(total_revenue, 2),
    'days_since_last_purchase': days_since_last_purchase,
    'email_open_rate': np.round(email_open_rate, 3),
    'website_visits_per_month': website_visits_per_month,
    'primary_category': primary_category,
    'satisfaction_score': np.round(satisfaction_score, 2),
    'support_tickets': support_tickets,
    'discount_usage_rate': np.round(discount_usage_rate, 3),
    'uses_mobile_app': uses_mobile_app,
    'newsletter_subscribed': newsletter_subscribed,
    'customer_lifetime_value': np.round(clv, 2),
    'is_churned': is_churned
})

# Save to CSV
df.to_csv('/home/claude/ecommerce-customer-analytics/data/customer_data.csv', index=False)

print(f"Generated {len(df)} customer records")
print(f"\nChurn rate: {df['is_churned'].mean()*100:.2f}%")
print(f"Average customer lifetime value: ${df['customer_lifetime_value'].mean():.2f}")
print(f"\nData saved to data/customer_data.csv")
print(f"\nDataset shape: {df.shape}")
print(f"\nFirst few rows:")
print(df.head())
