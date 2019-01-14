
# 暴力解法
class Solution1(object):
    def towSum(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if target == (nums[i] + nums[j]):
                    return [i, j]

# 2、两遍哈希表:
class Solution2(object):
    def towSum(self, nums, target):
        hash_map = dict()
        for key, value in enumerate(nums):
            hash_map[value] = key

        print(hash_map)
        for i in range(len(nums)):
            number = target - nums[i]
            if number in hash_map and i != hash_map[number]:
                return [i, hash_map[number]]

# 3、 1遍哈希表：

class Solution3(object):

    def towSum(self, nums, target):
        hash_map = dict()
        for index, x in enumerate(nums):
            if target - x in hash_map:
                return [index, hash_map[target - x]]
            else:
                hash_map[x] = index


if __name__ == "__main__":
    twoS = Solution3()
    list1 = [3, 3, 1, 3, 4]
    print(twoS.towSum(list1, 6))