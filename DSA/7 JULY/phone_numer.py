class Solution:
    
    
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        hash_map = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]}
        results=[]
        current_buffer=[]
        def backtrack(digits):
            nonlocal hash_map
            nonlocal results
            nonlocal current_buffer
            if is_complete(current_buffer,digits):
                results.append("".join(current_buffer))
                return
            
            choices = get_valid_choices(current_buffer,digits,hash_map)
            for choice in choices:
                current_buffer.append(choice)
                backtrack(digits)
                current_buffer.pop()

        backtrack(digits)
        return results

def is_complete(current_buffer,digits):
    return len(current_buffer)==len(digits)

def get_valid_choices(current_buffer,digits,hash_map):
    next_digit = digits[len(current_buffer)]
    return hash_map[next_digit]