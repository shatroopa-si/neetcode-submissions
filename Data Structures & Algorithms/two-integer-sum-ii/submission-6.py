class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
            Time complexity: O(n)
            Space complexity: O(1)

            Given: Input array is sorted and only one valid solution exists.
        """

        l, r = 0, len(numbers) - 1
        while l < r:
            diff = target - numbers[l]
            if diff == numbers[r]:
                return [l + 1, r + 1]           # 1-indexed array
            else:
                if diff > numbers[r]:
                    l += 1
                else:
                    r -= 1