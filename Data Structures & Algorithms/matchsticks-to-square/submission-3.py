from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        target = total // 4
        matchsticks.sort(reverse=True)

        # quick fail: biggest stick can't fit
        if matchsticks and matchsticks[0] > target:
            return False

        sides = [0, 0, 0, 0]
        memo = set()  # states we've already proven impossible

        def backtrack(i: int) -> bool:
            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3] == target

            state = (i, tuple(sorted(sides)))
            if state in memo:
                return False

            stick = matchsticks[i]
            for s in range(4):
                if sides[s] + stick > target:
                    continue

                sides[s] += stick
                if backtrack(i + 1):
                    return True
                sides[s] -= stick

                # symmetry prune: if we tried putting it on an empty side and it failed,
                # no need to try other empty sides
                if sides[s] == 0:
                    break

            memo.add(state)
            return False

        return backtrack(0)