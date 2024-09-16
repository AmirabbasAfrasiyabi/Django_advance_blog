"""
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.
    You can return the answer in any order.

    Example:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    Constraints:
        2 <= nums.length <= 10^6
        -10^9 <= nums[i] <= 10^9
        -10^9 <= target <= 10^9
"""

nums = [2, 7, 11, 15, 27]
target = 26
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print(i, j)
#             break


# d = {}
# for i in range(len(nums)):
#     d[nums[i]] = i
#     print(d)
#     x = nums[i]
#     y = target - x
#     if y in d:
#         print(i, d[y])
#         break
# else:
#     print('Not found')


