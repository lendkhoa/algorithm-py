def count_k_spikes(prices, k) -> int:
    n = len(prices)
    k_spikes_count = 0

    # For each element in prices, check if it's a k-Spike
    for i in range(n):
        left_count = sum(1 for j in range(0, i) if prices[j] < prices[i])
        right_count = sum(1 for j in range(i + 1, n) if prices[j] < prices[i])

        if left_count >= k and right_count >= k:
            k_spikes_count += 1

    return k_spikes_count


# Input
prices = [1, 2, 8, 5, 3, 4]
k = 2

# Count k-Spikes
count_k_spikes_result = count_k_spikes(prices, k)
print(count_k_spikes_result)
