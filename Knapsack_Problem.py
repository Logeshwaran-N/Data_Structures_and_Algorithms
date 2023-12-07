
def compute_weight(profit,weight,capacity,idx=0):
    if idx>len(weight)-1:
        return 0
    elif weight[idx] > capacity:
        return compute_weight(profit,weight,capacity,idx+1)
    else:
        option1=profit[idx]+compute_weight(profit,weight,capacity-weight[idx],idx+1)
        option2=compute_weight(profit,weight,capacity,idx+1)
    return max(option1,option2)
print(compute_weight([2,3,1],[4,5,1],15))
print(compute_weight([442, 525, 511, 593, 546, 564, 617],[41, 50, 49, 59, 55, 57, 60],170))


def knapsack_dp(profit,weights,capacity):
    n = len(weights)
    results = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for idx in range(n):
        for c in range(capacity + 1):
            if weights[idx] > c:
                results[idx + 1][c] = results[idx][c]
            else:
                results[idx + 1][c] = max(results[idx][c], profit[idx] + results[idx][c - weights[idx]])
    print(results)
    return results[-1][-1]

print(knapsack_dp([1,2,5,9,4],[2,3,3,4,6],10))
