# Input: The dictionary where the market identifier code is a key and the value is a stock price.
# Output: A string and the market identifier code.
# Example: best_stock({'CAC': 10.0,'ATX': 390.2,'WIG': 1.2}) == 'ATX'

def get_key(data, value):
    for k, v in data.items():
        if v == value:
            return k
def best_stock(data):
    max_val = 0
    for k, v in data.items():
        if v >= max_val:
            max_val = v
    return get_key(data, max_val)

print(best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2}))