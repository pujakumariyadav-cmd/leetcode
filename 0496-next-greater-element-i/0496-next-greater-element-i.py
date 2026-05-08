class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        for i in nums2:
            while stack and stack[-1] < i:
                next_greater[stack.pop()] = i
            stack.append(i)

        for i in stack:
            next_greater[i] = -1

        return [next_greater[i] for i in nums1]
       

        