class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsReg = {}    # numsReg = {num: reps}
        for num in nums:
            numsReg[num] = numsReg.get(num, 0) + 1
        sorted_data = sorted(numsReg, key=numsReg.get, reverse=True)
        return sorted_data[:k]