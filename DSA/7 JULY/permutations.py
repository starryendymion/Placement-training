class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(solutions, current_buffer, used):
            if is_complete(current_buffer, nums):
                solutions.append(current_buffer.copy())
                return
            
            choices = get_valid_choices(nums, used)
            for choice in choices:
                current_buffer.append(choice)
                used.add(choice)
                backtrack(solutions, current_buffer, used)
                current_buffer.pop()
                used.remove(choice)

        solutions = []
        backtrack(solutions, [], set())
        return solutions

def get_valid_choices(nums, used):
    return [num for num in nums if num not in used]  # O(1) lookup

def is_complete(current_buffer, nums):
    return len(current_buffer) == len(nums)