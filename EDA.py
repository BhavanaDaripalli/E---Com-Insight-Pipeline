import pandas as pd
from utils import valid_payment_types, country_city_map

# Load dataset
data = pd.read_csv('generated_data.csv')

# Display data info and check for duplicates
print(data.info())
print(f"Duplicates: {data.duplicated().sum()}")

# Check invalid quantities
invalid_qty_data = data[data['qty'] <= 0]
print(f"Invalid quantities: {len(invalid_qty_data)}")
if not invalid_qty_data.empty:
    print(invalid_qty_data[['order_id', 'customer_id', 'qty']])

# Check invalid prices
invalid_price_data = data[data['price'] <= 0]
print(f"Invalid prices: {len(invalid_price_data)}")
if not invalid_price_data.empty:
    print(invalid_price_data[['order_id', 'customer_id', 'price']])

# Check invalid payment types
invalid_payment_type_data = data[~data['payment_type'].isin(valid_payment_types)]
print(f"Invalid payment types: {len(invalid_payment_type_data)}")
if not invalid_payment_type_data.empty:
    print(invalid_payment_type_data[['order_id', 'customer_id', 'payment_type']])

# Check invalid countries
invalid_country_data = data[~data['country'].isin(country_city_map)]
print(f"Invalid countries: {len(invalid_country_data)}")
if not invalid_country_data.empty:
    print(invalid_country_data[['order_id', 'customer_id', 'country']])
