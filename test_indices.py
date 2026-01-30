import yfinance as yf
import sys

indices = {
    '^NSEI': 'NIFTY 50',
    '^BSESN': 'SENSEX',
    '^NSEBANK': 'NIFTY BANK',
    '^INDIAVIX': 'INDIA VIX'
}

print('Testing all market indices:\n')

for symbol, name in indices.items():
    try:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period='2d', timeout=10)
        
        if not hist.empty and len(hist) > 0:
            price = hist['Close'].iloc[-1]
            prev_close = hist['Close'].iloc[-2] if len(hist) > 1 else price
            change = ((price - prev_close) / prev_close) * 100 if prev_close else 0
            
            print(f'[OK] {name} ({symbol}):')
            print(f'  Price: Rs.{price:,.2f}')
            print(f'  Change: {change:+.2f}%')
            print()
        else:
            print(f'[FAIL] {name} ({symbol}): No data returned')
            print()
    except Exception as e:
        print(f'[ERROR] {name} ({symbol}): {str(e)[:100]}')
        print()

print('\nTest completed!')
