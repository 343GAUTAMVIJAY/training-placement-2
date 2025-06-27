class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon)
        m = len(dungeon[0])

        dp = [[0] * m for _ in range(n)]

        return self.helper(dungeon, n, m, 0, 0, dp)

    def helper(self, dungeon, n, m, row, col, dp):
        # base condition 1
        if row == n - 1 and col == m - 1:
            return max(1, 1 - dungeon[row][col])

        # base condition 2
        if row >= n or col >= m:
            return float('inf')

        if dp[row][col] != 0:
            return dp[row][col]

        right = self.helper(dungeon, n, m, row, col + 1, dp)
        down = self.helper(dungeon, n, m, row + 1, col, dp)

        # Calculate the minimum health needed at the current position
        dp[row][col] = max(1, min(right, down) - dungeon[row][col])

        return dp[row][col]
