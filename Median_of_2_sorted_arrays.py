def findMedianSortedArrays(nums1, nums2):
    # Step 1: Merge the two sorted arrays
    merged = sorted(nums1 + nums2)
    
    # Step 2: Find the median
    n = len(merged)
    if n % 2 == 1:  # Odd length
        return merged[n // 2]
    else:  # Even length
        return (merged[n // 2 - 1] + merged[n // 2]) / 2

# Example usage
nums1 = [1, 3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))  # Output: 2.0

nums1 = [1, 2]
nums2 = [3, 4]
print(findMedianSortedArrays(nums1, nums2))  # Output: 2.5