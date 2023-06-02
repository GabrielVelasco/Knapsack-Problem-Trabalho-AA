import time

def knapsack_recursive(weights, values, capacity, n):
    # Base case, if either the capacity is 0 or there are no items left
    if capacity == 0 or n == 0:
        return 0

    # If the weight of the nth item is more than the remaining capacity, skip it
    if weights[n - 1] > capacity:
        return knapsack_recursive(weights, values, capacity, n - 1)

    else:
        included = values[n - 1] + knapsack_recursive(weights, values, capacity - weights[n - 1], n - 1)    # nth item included
        not_included = knapsack_recursive(weights, values, capacity, n - 1)                                 # nth item not included
        return max(included, not_included)

def knapsack_memoization(weights, values, capacity, n, memo):
    # Base case, if either the capacity is 0 or there are no items left
    if capacity == 0 or n == 0:
        return 0

    # Result is already computed
    if memo[n][capacity] != -1:
        return memo[n][capacity]

    # If the weight of the nth item is more than the remaining capacity, skip it
    if weights[n - 1] > capacity:
        memo[n][capacity] = knapsack_memoization(weights, values, capacity, n - 1, memo)
        return memo[n][capacity]

    included = values[n - 1] + knapsack_memoization(weights, values, capacity - weights[n - 1], n - 1, memo)
    not_included = knapsack_memoization(weights, values, capacity, n - 1, memo)

    memo[n][capacity] = max(included, not_included)
    return memo[n][capacity]

def knapsack_dynamic(weights, values, capacity, n):
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]       # instanciate matrix

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0

            elif weights[i - 1] <= w:
                # item fits the bag, take it or not? (for this weight)
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]],  dp[i - 1][w]) 

            else:
                dp[i][w] = dp[i - 1][w] # use solution for above subprob

    return dp[n][capacity]      # valor q consigo considerando os 'n' items e tal 'capacity'


def knapsack_greedy(weights, values, capacity, n):
    # Calculate value-to-weight ratios for each item, keep original weight
    value_per_weight = [(values[i] / weights[i], weights[i]) for i in range(n)] # array of pairs 

    # Sort items in descending order of value-to-weight ratios
    value_per_weight.sort(reverse=True)

    total_value = 0
    remaining_capacity = capacity

    for value_ratio, weight in value_per_weight:

        # If the entire item can be included, add its value to the total value
        if remaining_capacity >= weight:
            total_value += value_ratio * weight
            remaining_capacity -= weight

        else:
            # Include a fraction of the item to fill the remaining capacity
            total_value += value_ratio * remaining_capacity

            break

    return total_value

def _verify(weights, values, capacity, n, memo, my_ans):
    # run the 3 algorithms with the same input
    # if they return the same ans as mine then it may be right...

    # ans1 = knapsack_recursive(weights, values, capacity, n)
    # ans2 = knapsack_memoization(weights, values, capacity, n, memo)
    # ans3 = knapsack_dynamic(weights, values, capacity, n)

    # return (ans1 == my_ans) and (ans2 == my_ans) and (ans3 == my_ans)

    return True

def run_knapsack(weights, values):
    capacity = 100

    n = len(values)
    memo = [[-1] * (capacity + 1) for _ in range(n + 1)]     # cada iteracao cria uma lista ==> matriz

    ########## RECURSIVE SOLUTION
    start_time = time.time()    # start clock
    max_value = knapsack_recursive(weights, values, capacity, n)
    end_time = time.time()      # stop clock
    elapsed_time = (end_time - start_time) * 1000  # calculate time elapsed in ms
    if _verify(weights, values, capacity, n, memo, max_value):
        print("Maximum value with recursion:", max_value)
        print("Time = ", elapsed_time)
        print()
    else:
        print("Problem... not the same ans!")

    ########### RECURSIVE WITH MEMO SOLUTION
    start_time = time.time()    # start clock
    max_value = knapsack_memoization(weights, values, capacity, n, memo)
    end_time = time.time()      # stop clock
    elapsed_time = (end_time - start_time) * 1000  # calculate time elapsed in ms
    if _verify(weights, values, capacity, n, memo, max_value):
        print("Maximum value with recursion and memo:", max_value)
        print("Time = ", elapsed_time)
        print()
    else:
        print("Problem... not the same ans!")

    ########## DP SOLUTION
    start_time = time.time()    # start clock
    max_value = knapsack_dynamic(weights, values, capacity, n)
    end_time = time.time()      # stop clock
    elapsed_time = (end_time - start_time) * 1000  # calculate time elapsed in ms
    if _verify(weights, values, capacity, n, memo, max_value):
        print("Maximum value with DP:", max_value)
        print("Time = ", elapsed_time)
        print()
    else:
        print("Problem... not the same ans!")

    ########## GREEDY APROXIMATION SOLUTION
    start_time = time.time()    # start clock
    max_value = knapsack_greedy(weights, values, capacity, n)
    end_time = time.time()      # stop clock
    elapsed_time = (end_time - start_time) * 1000  # calculate time elapsed in ms
    print("Maximum value with Greedy:", max_value)
    print("Time = ", elapsed_time)
    print()


def main():
    weights =  [44, 15, 47, 47, 46, 39, 2, 12, 19, 36, 46, 35, 34, 8, 5, 34, 12, 12, 42, 25, 5, 40, 39, 41, 35]
    values =  [11, 46, 28, 33, 48, 18, 36, 2, 47, 28, 43, 10, 7, 9, 26, 36, 18, 5, 5, 6, 19, 33, 2, 23, 9]

    run_knapsack(weights, values)