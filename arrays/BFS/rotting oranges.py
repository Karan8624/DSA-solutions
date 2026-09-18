class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        def rot(grid: list[list[int]] , rotten , ripe : int):
            new_rotten = []
            for pos in rotten:
                if pos[0] > 0  and grid[pos[0] - 1][ pos[1]] == 1:
                    grid[pos[0] - 1][ pos[1]] = 2
                    new_rotten.append((pos[0] -1 , pos[1]))
                    ripe -= 1
                if pos[0] < len(grid) -1   and grid[pos[0] + 1 ][ pos[1]] == 1:
                    grid[pos[0] + 1 ][ pos[1]] = 2
                    new_rotten.append((pos[0] +1 , pos[1]))
                    ripe -= 1
                if pos[1] > 0  and grid[pos[0] ][ pos[1] -1 ] == 1:
                    grid[pos[0] ][ pos[1] -1 ] =2 
                    new_rotten.append((pos[0] , pos[1] -1 ))
                    ripe -= 1
                if pos[1] < len(grid[0]) - 1 and grid[pos[0]] [ pos[1] + 1] == 1:
                    grid[pos[0]] [ pos[1] + 1] = 2
                    new_rotten.append((pos[0]  , pos[1] + 1))
                    ripe -= 1
            return [new_rotten , ripe]
        rotten = []
        ripe =  0
        for i in range(len(grid)):
            for r in range(len(grid[0])):
                if grid[i][r] == 2:
                    rotten.append((i , r))
                elif grid[i][r] == 1:
                    ripe += 1
        mins = 0
        while ripe > 0 :
            mins += 1
            op = rot(grid , rotten , ripe)
            rotten  = op[0]
            ripe = op[1]
            if rotten == [] and ripe != 0 :
                return -1
        return mins 



                
