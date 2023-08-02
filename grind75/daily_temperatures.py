class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                past_temp, past_index = stack.pop()
                answer[past_index] = idx - past_index
            
            stack.append((temp, idx))

        return answer

    

"""
Algo
- iterate over the temps
- if the stack is empty : append the current element
- if the stack is not empty : compare the top elements and pop until either the stack is empty or the current element is smaller 
- update answer[i]
- return answer

- the first element that is warmer ( find next warmer day )
- map = { temp : index }
- order indices? -> 
- Need to have future information to process the current one
    - How do we organize that look into the future

Pattern
- Finding next largest / smallest number
- Monotonic Array!
"""
