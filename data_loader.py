import pandas as pd
import streamlit as st

def load_data(file):
    try:
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)
        
        # Basic cleaning
        df = clean_data(df)
        return df
    except Exception as e:
        st.error(f"Error loading file: {str(e)}")
        return None

def clean_data(df):
    df = df.dropna()  # Remove empty rows
    df = df.drop_duplicates()  # Remove duplicates
    
    # Convert date columns if they exist
    date_columns = [col for col in df.columns if 'date' in col.lower() or 'time' in col.lower()]
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    
    return df

def detect_column_types(df):
    column_types = {
        'date_columns': [col for col in df.columns if 'date' in col.lower() or 'time' in col.lower()],
        'amount_columns': [col for col in df.columns if any(word in col.lower() for word in ['sales', 'amount', 'revenue', 'price'])],
        'quantity_columns': [col for col in df.columns ~],
        'profit_columns': [col for col in df.columns if 'profit' in col.lower()],
        'category_columns': [col for col in df.columns if any(word in col.lower() for word in ['category', 'type', 'region', 'segment', 'product'])]
    }
    return column_types