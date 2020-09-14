'''
136. Single Number
Easy

4880

170

Add to List

Share
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''


#Solution 1:

from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        return 2*(sum(set(nums))) - sum(nums)


#Solution 2:

from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        result = counter.most_common()
        
        return result[len(result)-1][0]