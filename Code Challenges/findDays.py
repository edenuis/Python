#Challenge: The cost of stock on each day is given in an array A[] of size N. 
#           Find all the days on which you buy and sell the stock so that in 
#           between those days your profit is maximum.

def findDays(prices):
    periods = []
    start = 0
    end = 0
    for idx in range(1, len(prices)):
        if prices[end] <= prices[idx]:
            end = idx
        else:
            if end - start > 0:
                periods.append((start, end))
            start = idx
            end = idx
    if end - start > 0:
        periods.append((start, end))
    return periods
if __name__ == "__main__":
    assert findDays([1,2,3,4,5]) == [(0, 4)]
    assert findDays([1,2,2,4,5]) == [(0, 4)]
    assert findDays([100, 180, 260, 310, 40, 535, 695]) == [(0, 3), (4,6)]
    assert findDays([5,4,3,2,1]) == []
    assert findDays([5,4,3,2,1, 100, 105,110]) == [(4,7)]
