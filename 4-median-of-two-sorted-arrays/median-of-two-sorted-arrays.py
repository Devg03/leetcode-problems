class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalNums = sorted(nums1 + nums2)
        
        if len(totalNums) % 2 == 1:
            index = int((len(totalNums) - 1) / 2)
            return totalNums[index]

        if len(totalNums) % 2 == 0:
            index1 = int((len(totalNums) - 1) / 2)
            index2 = int(len(totalNums) / 2)
            totalIndices = totalNums[index1] + totalNums[index2]
            return totalIndices / 2
        