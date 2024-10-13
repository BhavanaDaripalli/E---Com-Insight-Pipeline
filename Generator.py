import pandas as pd
from utils import fake, product_names, ecommerce_domains, valid_payment_types, failure_reasons, country_city_map
import numpy as np

# Function to generate fake data
def generate_data(num_records, rogue_probability=0.05):
    data = []
    for _ in range(num_records):
        product_category = fake.random_element(elements=list(product_names.keys()))
        product_name = fake.random_element(elements=product_names[product_category])
        payment_type = fake.random_element(elements=valid_payment_types)
        payment_success = fake.random_element(elements=('Y', 'N'))
        country = fake.random_element(elements=list(country_city_map.keys()))
        city = fake.random_element(elements=country_city_map[country])

        record = {
            'order_id': fake.uuid4(),
            'customer_id': fake.uuid4(),
            'customer_name': fake.name(),
            'product_id': fake.uuid4(),
            'product_name': product_name,
            'product_category': product_category,
            'payment_type': payment_type,
            'qty': np.random.randint(1, 10),
            'price': round(np.random.uniform(10, 500), 2),
            'datetime': fake.date_time_this_decade(),
            'country': country,
            'city': city,
            'ecommerce_website_name': fake.random_element(elements=ecommerce_domains),
            'payment_txn_id': fake.uuid4(),
            'payment_txn_success': payment_success,
            'failure_reason': None
        }

        if payment_success == 'N':
            record['failure_reason'] = fake.random_element(elements=failure_reasons[payment_type])
        
        if np.random.rand() < rogue_probability:
            record['qty'] = np.random.choice([-1, 0, 1000])
            record['price'] = np.random.choice([-100, 0])
            record['payment_type'] = 'Unknown'
            record['country'] = 'Unknown'
            record['city'] = 'Unknown'
        
        data.append(record)
    
    return pd.DataFrame(data)

# Generate and save data
df = generate_data(10000)
df.to_csv('generated_data.csv', index=False)
