"""Test the actual get_indices_data function from app.py"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

# Import the function directly from app.py
from app import get_indices_data

print('Testing get_indices_data() function from app.py:\n')

try:
    result = get_indices_data()
    print(f'Function returned {len(result)} indices:\n')
    
    for index in result:
        print(f"  {index['name']}: {index['value']} ({index['change']:+.2f}%)")
    
    # Check if we're getting real data or mock data
    if result[0]['value'] == '24,500.00':
        print('\n[WARNING] Returning MOCK data (fallback values)')
    else:
        print('\n[SUCCESS] Returning LIVE data from Yahoo Finance!')
        
except Exception as e:
    print(f'[ERROR] Function failed: {e}')
    import traceback
    traceback.print_exc()
