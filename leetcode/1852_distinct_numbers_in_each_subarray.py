class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        # construct arr of size: 7 - 3 + 1 = 5
        # each subarr are size k large, converted to a set, check that length

        output = []
        output_size = len(nums) - k + 1
        unique = defaultdict(int)

        # first populate window
        for i in range(k):
            unique[nums[i]] += 1

        output.append(len(unique.keys()))
        # slide window
        for r in range(k, len(nums)):
            l = nums[r - k]
            unique[l] -= 1
            if unique[l] == 0:
                del unique[l]

            unique[nums[r]] += 1
            output.append(len(unique.keys()))

        return output
