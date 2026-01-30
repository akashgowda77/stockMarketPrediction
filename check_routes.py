from app import app

print("All registered routes:")
print("-" * 50)
for rule in app.url_map.iter_rules():
    print(f"{rule.endpoint:30s} {rule.rule}")
    
print("\n" + "-" * 50)
print("Looking for watchlist route...")
watchlist_routes = [rule for rule in app.url_map.iter_rules() if 'watchlist' in rule.endpoint.lower() or 'watchlist' in rule.rule.lower()]
if watchlist_routes:
    print("Found watchlist routes:")
    for route in watchlist_routes:
        print(f"  {route.endpoint:30s} {route.rule}")
else:
    print("❌ No watchlist routes found!")
