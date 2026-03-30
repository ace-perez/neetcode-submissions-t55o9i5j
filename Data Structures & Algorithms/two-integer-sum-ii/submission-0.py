class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        I want to use two pointers as the main way of solving this. I want to use left point which
        will point to the left side of the array. There will be also a right pointer on the 
        right side of the array. I will continuely decrement the right and increment the left,
        until that I find that l + r == target
        """
        
        left, right = 0, len(numbers) - 1

        while left < right:
            value = numbers[left] + numbers[right]

            if value == target:
                return[left+1, right+1] 
            elif value > target:
                right -= 1
            elif value < target:
                left += 1


        

            