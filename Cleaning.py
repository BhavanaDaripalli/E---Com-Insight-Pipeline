import pandas as pd
import numpy as np
from utils import fake, product_names, ecommerce_domains, valid_payment_types, failure_reasons, country_city_map

# Function to clean invalid values
def clean_schema(df):
    df['qty'] = df['qty'].apply(lambda x: np.random.randint(1, 10) if pd.isnull(x) or x in [-1, 0, 1000] else x)
    df['price'] = df['price'].apply(lambda x: round(np.random.uniform(10, 500), 2) if pd.isnull(x) or x in [-100, 0] else x)
    df['payment_type'] = df['payment_type'].apply(lambda x: fake.random_element(elements=valid_payment_types) if pd.isnull(x) or x == 'Unknown' else x)

    country_mode = df['country'].mode()[0]

    def assign_country_city(country, city):
        if pd.isnull(country) or country == 'Unknown':
            country = country_mode
        if pd.isnull(city) or city == 'Unknown':
            city = fake.random_element(elements=country_city_map[country])
        return country, city

    df[['country', 'city']] = df.apply(lambda row: assign_country_city(row['country'], row['city']), axis=1, result_type='expand')
    
    df['customer_name'] = df['customer_name'].apply(lambda x: fake.name() if pd.isnull(x) or not isinstance(x, str) else x)
    df['ecommerce_website_name'] = df['ecommerce_website_name'].apply(lambda x: fake.random_element(elements=ecommerce_domains) if pd.isnull(x) or x not in ecommerce_domains else x)
    df['failure_reason'] = df['failure_reason'].fillna('No Failure')
    
    return df

# Function to load and clean data
def load_and_clean_data(input_file, output_file):
    df = pd.read_csv(input_file)
    df_cleaned = clean_schema(df)
    df_cleaned.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
    load_and_clean_data('generated_data.csv', 'ECommerce_generated_data.csv')