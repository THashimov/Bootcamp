import random

# Generate 5x5 grid
# Run a 5x5 nested loop, generating a random number with each iteration
# If num == 1, assign # to the grid
# if num == 0 assign - to the grid
# Iterate over the grid
# If col is 0, we cannot check above 
# If row is 0, we cannot check left
# If row is 4, we cannot check right
# If col is 4, we cannot check down
# Check all round, being sure not to check out of bounds
def create_grid() :
    grid = [[0] * 5 for _ in range(5)]

    for col in range(len(grid)) :
        for row in range(len(grid[col])) :
            rnd_num = random.randint(0, 1)
            if rnd_num == 1 :
                rnd_num = str('#')
            else :
                rnd_num = str('-')
            grid[row][col] = rnd_num    

    for row in range(len(grid)) :
        for col in range(len(grid[row])) :
            mines_in_vicinity = 0
            if grid[row][col] == '-' :
                if row == 0 :
                    if col == 0 :
                        if grid[row][col + 1] == '#' :
                            mines_in_vicinity += 1
                        if grid[row + 1][col + 1] == '#' :
                            mines_in_vicinity += 1
                        if grid[row + 1][col] == '#' :
                            mines_in_vicinity += 1
                        grid[row][col] = mines_in_vicinity
                    if col == 4 :
                        if grid[row][col - 1] == '#' :
                            mines_in_vicinity += 1
                        if grid[row + 1][col - 1] == '#' :
                            mines_in_vicinity += 1
                        if grid[row + 1][col] == '#' :
                            mines_in_vicinity += 1
                        grid[row][col] = mines_in_vicinity
                    if col > 0 and col < 4 :
                        if grid[row][col - 1] == '#' :
                            mines_in_vicinity += 1
                        if grid[row + 1][col - 1] == '#' :
                            mines_in_vicinity += 1
                        if grid[row + 1][col] == '#' :
                            mines_in_vicinity += 1
                        if grid[row + 1][col + 1] == '#' :
                            mines_in_vicinity += 1
                        if grid[row][col + 1] == '#' :
                            mines_in_vicinity += 1
                        grid[row][col] = mines_in_vicinity
                if row == 4 :
                    if col == 0 :
                        if grid[row][col + 1] == '#' :
                            mines_in_vicinity += 1
                        if grid[row - 1][col + 1] == '#' :
                            mines_in_vicinity += 1
                        if grid[row - 1][col] == '#' :
                            mines_in_vicinity += 1
                        grid[row][col] = mines_in_vicinity
                    if col == 4 :
                        if grid[row][col - 1] == '#' :
                            mines_in_vicinity += 1
                        if grid[row - 1][col - 1] == '#' :
                            mines_in_vicinity += 1
                        if grid[row - 1][col] == '#' :
                            mines_in_vicinity += 1
                        grid[row][col] = mines_in_vicinity
                    if col > 0 and col < 4 :
                        if grid[row][col - 1] == '#' :
                            mines_in_vicinity += 1
                        if grid[row - 1][col - 1] == '#' :
                            mines_in_vicinity += 1
                        if grid[row - 1][col] == '#' :
                            mines_in_vicinity += 1
                        if grid[row - 1][col + 1] == '#' :
                            mines_in_vicinity += 1
                        if grid[row][col + 1] == '#' :
                            mines_in_vicinity += 1
                        grid[row][col] = mines_in_vicinity
                elif row > 0 and row < 4 :
                    if col == 0 :
                        if grid[row + 1][col] == '#' :
                            mines_in_vicinity += 1
                        if grid[row - 1][col] == '#' :
                            mines_in_vicinity += 1
                        if grid[row][col + 1] == '#' :
                            mines_in_vicinity += 1
                        if grid[row - 1][col + 1] == '#' :
                            mines_in_vicinity += 1
                        if grid[row + 1][col + 1] == '#' :
                            mines_in_vicinity += 1
                        grid[row][col] = mines_in_vicinity
                    if col == 4 :
                        if grid[row + 1][col] == '#' :
                            mines_in_vicinity += 1
                        if grid[row - 1][col] == '#' :
                            mines_in_vicinity += 1
                        if grid[row][col - 1] == '#' :
                            mines_in_vicinity += 1
                        if grid[row - 1][col - 1] == '#' :
                            mines_in_vicinity += 1
                        if grid[row + 1][col - 1] == '#' :
                            mines_in_vicinity += 1
                        grid[row][col] = mines_in_vicinity
                    if col > 0 and col < 4 :
                        if grid[row + 1][col] == '#' :
                            mines_in_vicinity += 1
                        if grid[row + 1][col - 1] == '#' :
                            mines_in_vicinity += 1
                        if grid[row][col - 1] == '#' :
                            mines_in_vicinity += 1
                        if grid[row - 1][col - 1] == '#' :
                            mines_in_vicinity += 1
                        if grid[row - 1][col] == '#' :
                            mines_in_vicinity += 1
                        if grid[row - 1][col + 1] == '#' :
                            mines_in_vicinity += 1 
                        if grid[row][col + 1] == '#' :
                            mines_in_vicinity += 1
                        if grid[row + 1][col + 1] == '#' :
                            mines_in_vicinity += 1   
                        grid[row][col] = mines_in_vicinity

    for row in grid :
        print(row)

create_grid()