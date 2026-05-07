class Solution(object):
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        leftArr = nums[:mid]
        rightArr = nums[mid:]
        left = self.sortArray(leftArr)
        right = self.sortArray(rightArr)

        return self.merge(left, right)

    def merge(self, leftArr, rightArr):
        merged = []
        i = j = 0
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                merged.append(leftArr[i])
                i += 1
            else:
                merged.append(rightArr[j])
                j += 1

        while i < len(leftArr):
            merged.append(leftArr[i])
            i += 1
        while j < len(rightArr):
            merged.append(rightArr[j])
            j += 1

        return merged



