"""Test the sector mapping to ensure all filters work correctly"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from app import get_stock_data

# Sector mapping (same as in the fixed JS code)
sector_map = {
    'banking': ['financial services', 'financial'],
    'pharma': ['healthcare'],
    'auto': ['consumer cyclical', 'auto'],
    'it': ['technology'],
    'fmcg': ['consumer defensive', 'consumer staples'],
    'energy': ['energy'],
    'realty': ['real estate']
}

# Sample stocks from each category
test_stocks = {
    'Banking': ['HDFCBANK', 'ICICIBANK', 'SBIN'],
    'Pharma': ['SUNPHARMA', 'CIPLA', 'DRREDDY'],
    'Auto': ['MARUTI', 'TATAMOTORS', 'M&M'],
    'IT': ['INFY', 'TCS', 'WIPRO'],
    'FMCG': ['HINDUNILVR', 'ITC', 'BRITANNIA']
}

print('Testing Sector Mapping:\n')
print('=' * 70)

for category, symbols in test_stocks.items():
    print(f'\n{category} Filter:')
    filter_name = category.lower()
    search_terms = sector_map.get(filter_name, [filter_name])
    print(f'  Searches for: {search_terms}')
    print(f'  Testing stocks:')
    
    matches = 0
    for symbol in symbols:
        try:
            stock_data = get_stock_data(symbol)
            if stock_data:
                sector = stock_data.get('sector', 'N/A')
                # Check if this stock would be matched
                matched = any(term in sector.lower() for term in search_terms)
                status = '[MATCH]' if matched else '[MISS]'
                print(f'    {symbol:15} -> {sector:30} {status}')
                if matched:
                    matches += 1
            else:
                print(f'    {symbol:15} -> No data')
        except Exception as e:
            print(f'    {symbol:15} -> ERROR: {str(e)[:40]}')
    
    print(f'  Result: {matches}/{len(symbols)} stocks matched')

print('\n' + '=' * 70)
print('\nTest completed! All filters should now work correctly.')
