class Solution:
 def combinationSum(self,candidates, target):
    def is_complete(solution):
        return sum(solution) == target
    
    def get_valid_choices(solution):
        current_sum = sum(solution)
        last_used = solution[-1] if solution else 0
        
        return [num for num in candidates 
                if num >= last_used and current_sum + num <= target]
    
    def backtrack(current_solution, all_solutions):
        if is_complete(current_solution):
            all_solutions.append(current_solution.copy())
            return
        
        for choice in get_valid_choices(current_solution):
            current_solution.append(choice)
            backtrack(current_solution, all_solutions)
            current_solution.pop()
    
    all_solutions = []
    backtrack([], all_solutions)
    return all_solutions
