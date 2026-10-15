class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        freq = {}

        freq = Counter(nums)

        for key, val in freq.items():
            bucket[val].append(key)

        result = []
        position = len(bucket) - 1

        while len(result) < k and position >= 0:
            result.extend(bucket[position])
            position -= 1
        
        return result