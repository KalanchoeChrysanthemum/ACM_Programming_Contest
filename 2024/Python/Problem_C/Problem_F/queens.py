def main():

    # Read number of different boards
    num_boards = input()

    # Check for invalid input
    if num_boards == '0' or num_boards == '':
        return
    
    # Initialize results
    results = []
    
    # Loop over each game
    for x in range(0, int(num_boards)):

        # Initialize board
        board: list[str] = []

        # Read entire chess board
        for _ in range(0, 8):
            board.append(input())

        # Initialize queen locations
        queens: list[tuple] = []

        # Find queens and add to queen list
        for y_coord, row in enumerate(board):
            for x_coord, col in enumerate(row):
                if col == '*':
                    queens.append((x_coord, y_coord))

        # Initialize check
        is_possible = True

        # Loop over each queen, checking if game is valid
        for outer_index, outer_queen in enumerate(queens):
            for inner_index, inner_queen in enumerate(queens):
                if outer_index == inner_index:
                    continue

                # Checks column
                if outer_queen[0] == inner_queen[0]:
                    is_possible = False
                
                # Checks row
                if outer_queen[1] == inner_queen[1]:
                    is_possible = False

                # Checks diagonal
                if abs(outer_queen[0] - inner_queen[0]) == abs(outer_queen[1] - inner_queen[1]):
                    is_possible = False

        # Add result to results
        if is_possible:
            results.append('valid')
        else:
            results.append('invalid')

    # Print results
    for result in results:
        print(result)

if __name__ == '__main__':
    main()