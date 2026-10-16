class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            alive = True
            while len(stack) > 0 and stack[-1] > 0 and ast < 0:
                last = stack[-1]
                if abs(last) < abs(ast):
                    stack.pop()
                elif abs(last) == abs(ast):
                    stack.pop()
                    alive = False
                    break
                else:
                    alive = False
                    break
            if alive:
                stack.append(ast)
        return stack



