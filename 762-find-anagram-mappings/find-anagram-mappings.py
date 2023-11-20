class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        anagramMap = []
        for i in nums1:
            anagramMap.append(nums2.index(i))
        return anagramMap