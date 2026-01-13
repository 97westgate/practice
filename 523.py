def has_good_subarray(nums, k):
    pass # your code goes here

    if not isinstance(nums, (list, tuple)): # we need a list or tuple to iterate over
        return False

    if k == 0: # we can't divide by 0
        return False

    if len(nums) < 2: # we need at least 2 elements to form a subarray
        return False

    k = abs(k) # to handle negative integers

    seen_remainders: dict[int, int] = {0: -1}
    prefix_sum: int = 0

    for i, num in enumerate(nums):
        prefix_sum += num
        remainder = prefix_sum % k

        # if we see this remainder before we found a good subarray
        if remainder in seen_remainders:
            # check if the subarray is at least 2 elements long
            if i - seen_remainders[remainder] >= 2:
                return True
        else:
            seen_remainders[remainder] = i
    return False
    
# debug your code below
print(has_good_subarray([23, 2, 4, 7], 6))