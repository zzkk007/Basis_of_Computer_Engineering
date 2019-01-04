# 求 三个数的和


class Solution1(object):
    def threeSum(self, nums, target):
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) -1 ):
                for k in range(i + 2, len(nums)):
                    if target == (nums[i] + nums[j] + nums[k]):
                        return [i, j, k]


class Solution2(object):

    def threeSum(self, nums):
        if len(nums) < 3:
            return []

        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            # 去掉自己本身
            if i >= 1 and v == nums[i - 1]:
                continue

            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
        return map(list, res)


if __name__ == "__main__":
    twoS = Solution2()
    list1 = [-1, 0, 1, 2, -1, -4]
    print(twoS.threeSum(list1))