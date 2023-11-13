def kadane_algorithm(T):
    # Input validation
    if not T or not isinstance(T, list):
        raise ValueError("Input must be a non-empty list of integers.")

    # Initialization
    current_sum = 0
    max_sum = 0

    # Kadane's algorithm
    for i in range(len(T)):
        current_sum += T[i]

        if current_sum < 0:
            current_sum = 0

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

# Example usage
# Replace the array elements with your own values
array = [your_values_here]
result = kadane_algorithm(array)
print("Maximum subarray sum:", result)
