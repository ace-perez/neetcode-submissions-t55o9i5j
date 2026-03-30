class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            lr_added = numbers[left] + numbers[right]

            if lr_added == target:
                return list([left + 1,right + 1])
            elif lr_added < target:
                left += 1
            else:
                right -= 1

        

        

            