
def binary(nums, low, high, val):

    if low > high:
        return False

    mid = low + ((high-low) >> 1)

    if nums[mid] == val:
        return True

    elif nums[mid] < val:
        return binary(nums, mid+1, high, val)
    else:
        return binary(nums, low, mid-1, val)


if __name__ == "__main__":

    nums = [1, 4, 5, 8, 9, 12, 23, 33, 44, 56]
    print(binary(nums, 0, len(nums)- 1, 22))