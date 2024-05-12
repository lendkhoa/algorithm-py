def collapse_list(values, threshold):
    if not values:
        return []

    # Initialize the result list with the first value
    result = [values[0]]

    # Start with the first element as the anchor
    anchor = values[0]

    for value in values[1:]:
        # If the difference is less than the threshold, skip it
        if value - anchor < threshold:
            continue
        # Otherwise, update the anchor and add the value to the result
        anchor = value
        result.append(value)

    return result


# Example usage
input_values = [0, 14, 18, 33, 36, 39]
threshold = 4
print(collapse_list(input_values, threshold))  # Expected output: [0, 14, 33]
