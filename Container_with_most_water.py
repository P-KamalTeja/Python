def maxArea(height):
    left, right = 0, len(height) - 1  # Initialize two pointers
    max_area = 0

    while left < right:
        # Calculate the area formed by the lines at left and right pointers
        width = right - left
        area = min(height[left], height[right]) * width
        max_area = max(max_area, area)

        # Move the pointer pointing to the smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

# Example usage
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))  # Output: 49