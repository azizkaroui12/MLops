prices = [100, 250, 75, 300]
discounts = [0.1, 0.2, 0.05, 0.15]

# 1. Use map () to apply the discounts .
from functools import reduce

discounted_prices = list(map(lambda p, d: p * (1 - d), prices, discounts))
print("Discounted prices:", discounted_prices)
# 2. Use filter () to find discounted prices > 200.
expensive_items = list(filter(lambda price: price > 200, discounted_prices))
print("Discounted prices greater than 200:", expensive_items)

# 3. Use reduce () to compute total discounted cost .
total_discounted_cost = reduce(lambda acc, price: acc + price, discounted_prices, 0)
print("Total discounted cost:", total_discounted_cost)

# 4. Use zip () to pair each price with a discount .
paired = list(zip(prices, discounts))
print("Paired prices and discounts:", paired)

# 5. Use enumerate () to label each product with its index .
enumerated = list(enumerate(prices))
print("Enumerated prices:", enumerated)
