import numpy as np
import pandas as pd
from faker import Faker

# Initialize Faker
fake = Faker()

# Define valid product categories and names
product_names = {
    'Electronics': ['Smartphone', 'Laptop', 'Tablet', 'Headphones', 'Camera'],
    'Clothing': ['T-shirt', 'Jeans', 'Jacket', 'Dress', 'Sneakers'],
    'Grocery': ['Milk', 'Bread', 'Eggs', 'Fruits', 'Vegetables'],
    'Furniture': ['Chair', 'Table', 'Sofa', 'Bed', 'Bookshelf'],
    'Sports': ['Football', 'Basketball', 'Tennis Racket', 'Golf Club', 'Yoga Mat'],
    'Books': ['Novel', 'Biography', 'Comics', 'Cookbook', 'Textbook']
}

# Define valid e-commerce domains
ecommerce_domains = ['Amazon', 'Flipkart', 'Myntra', 'eBay', 'Meesho']

# Define valid payment types and failure reasons
valid_payment_types = ['card', 'Internet Banking', 'UPI', 'Wallet']
failure_reasons = {
    'card': ['Insufficient funds', 'Invalid card details', 'Card expired', 'Fraud suspected'],
    'Internet Banking': ['Payment gateway timeout', 'Exceeded transaction limit', 'Incorrect login credentials'],
    'UPI': ['Network issues', 'Incorrect UPI ID', 'Incorrect OTP'],
    'Wallet': ['Insufficient balance in wallet', 'Wallet account blocked', 'Wallet not authorized for transaction']
}

# Define valid countries and cities
country_city_map = {
    'USA': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'India': ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai'],
    'UK': ['London', 'Manchester', 'Birmingham', 'Liverpool', 'Leeds'],
    'Germany': ['Berlin', 'Munich', 'Frankfurt', 'Hamburg', 'Stuttgart'],
    'Canada': ['Toronto', 'Vancouver', 'Montreal', 'Calgary', 'Ottawa'],
    'Australia': ['Sydney', 'Melbourne', 'Brisbane', 'Perth', 'Adelaide'],
    'France': ['Paris', 'Lyon', 'Marseille', 'Nice', 'Toulouse'],
    'Brazil': ['São Paulo', 'Rio de Janeiro', 'Brasilia', 'Salvador', 'Fortaleza'],
    'Japan': ['Tokyo', 'Osaka', 'Kyoto', 'Nagoya', 'Sapporo'],
    'South Africa': ['Johannesburg', 'Cape Town', 'Durban', 'Pretoria', 'Port Elizabeth']
}


