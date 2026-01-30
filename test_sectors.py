"""Test which sectors are being returned and identify missing ones"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from app import get_stock_data

# Sample of stocks from the app.py symbols list
test_stocks = {
    'Pharma': ['SUNPHARMA', 'DRREDDY', 'CIPLA', 'DIVISLAB', 'AUROPHARMA', 'LUPIN', 'TORNTPHARM', 'BIOCON'],
    'Banking': ['HDFCBANK', 'ICICIBANK', 'SBIN', 'AXISBANK', 'KOTAKBANK', 'PNB', 'BANDHANBNK', 'INDUSINDBK'],
    'Auto': ['MARUTI', 'TATAMOTORS', 'M&M', 'BAJAJ-AUTO', 'HEROMOTOCO', 'EICHERMOT', 'ASHOKLEY', 'TVSMOTOR']
}

print('Testing stock sectors:\n')

for category, symbols in test_stocks.items():
    print(f'\n{category} Sector:')
    print('=' * 50)
    
    for symbol in symbols:
        try:
            stock_data = get_stock_data(symbol)
            if stock_data:
                sector = stock_data.get('sector', 'N/A')
                print(f'  {symbol:15} -> Sector: {sector}')
            else:
                print(f'  {symbol:15} -> [FAILED] No data returned')
        except Exception as e:
            print(f'  {symbol:15} -> [ERROR] {str(e)[:50]}')

print('\n\nTest completed!')
