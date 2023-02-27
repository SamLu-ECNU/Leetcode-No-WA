"""
每日一题：2023.02.27
题目链接：https://leetcode.cn/problems/decrease-elements-to-make-array-zigzag/
标签：有边界的数组遍历
思路：对于 nums 逐个遍历，对于奇数或者偶数下标 i，分组计算操作次数，
每一个 nums[i] 需要减少 max(0, nums[i] - min(left, right) + 1)，
其中，left, right 分别是 nums[i] 左边或者右边的元素值；

如果出现下标越界的情况，由于存在 min 操作符，可将越界元素置为数组最大值 mx，
保证算法能够自动根据存在的另一边数值，进行操作次数的计算。
"""

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        s = [0] * 2
        mx = 1000 + 1

        for i, num in enumerate(nums):
            left = nums[i - 1] if i else mx
            right = nums[i + 1] if i < len(nums) - 1 else mx
            s[i % 2] += max(0, num - min(left, right) + 1)

        return min(s)
