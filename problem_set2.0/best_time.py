#!/usr/bin/env python3
"""
Best Time to Buy and Sell Stock

Problem: Given a list of stock prices (one per day), find the maximum
         profit you can make by buying on one day and selling later.

Example: [7, 1, 5, 3, 6, 4] → Answer is 5
         Buy on day 2 (price=1), sell on day 5 (price=6) → 6-1=5

Approach: Track the minimum price seen so far. At each price,
          calculate potential profit if we sold today.
          Keep track of the maximum profit found.
"""


def max_profit(prices: list[int]) -> int:
    """
    Find the maximum profit from buying and selling stock once.

    Args:
        prices: A list of stock prices (one per day)

    Returns:
        The maximum profit possible (0 if no profit can be made)

    Examples:
        >>> max_profit([7, 1, 5, 3, 6, 4])
        5
        >>> max_profit([7, 6, 4, 3, 1])
        0
    """
    # Edge case: need at least 2 days to make a trade
    if len(prices) < 2:
        return 0

    min_price = prices[0]  # Cheapest price seen so far
    max_profit_found = 0   # Best profit found so far

    for price in prices:
        # Update minimum price if we found a cheaper day
        min_price = min(min_price, price)

        # Calculate profit if we sold today
        profit = price - min_price

        # Update max profit if this is better
        max_profit_found = max(max_profit_found, profit)

    return max_profit_found


# --- Run only when executed directly ---
if __name__ == "__main__":
    # Test case
    stock_prices = [7, 1, 5, 3, 6, 4]
    print(f"Prices: {stock_prices}")
    print(f"Max profit: {max_profit(stock_prices)}")
    # Output: 5 (buy at 1, sell at 6)
