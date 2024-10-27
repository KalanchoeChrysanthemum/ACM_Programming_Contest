def main():

    # Dictionary that maps decimal numbers to seven segment display codes
    deci_to_segment: dict[int, str] = {
        0: '11111100',
        1: '01100000',
        2: '11011010',
        3: '11110010',
        4: '01100110',
        5: '10110110',
        6: '10111110',
        7: '11100000',
        8: '11111110',
        9: '11100110'
    }

    # 2D array containing answers
    results: list[list[int]] = []

    # Read input until done
    while True:
        num = input()

        # Check if no input
        if num == '' or num == None:
            break

        # Initialize current segment display code
        curr_result = []

        # Convert num to segment display code and add to curr_result
        for char in num:
            curr_result.append(deci_to_segment.get(int(char)))

        # Add to results
        results.append(curr_result)

    # Print results with proper formatting
    for result in results:
        print(' '.join(result))

if __name__ == '__main__':
    main()