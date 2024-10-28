def main():
    
    # Get number of cases
    num_cases = input()

    # Initialize answer list
    answers = []

    # Loop over the lights checking if they are off at the same time
    for _ in range(0, int(num_cases)):

        # Read in the lights and max seconds
        light_1, light_2, seconds = input().split(' ')

        # Get the multiples of the lights within the range of time
        first_multiples = get_multiples(int(light_1), int(seconds))
        second_multiples = get_multiples(int(light_2), int(seconds))

        # Initialize boolean for whether the lights are off at the same time
        valid = False

        # Check if the multiples contain the same value and set valid to true if so
        for num in first_multiples:
            if second_multiples.__contains__(num):
                valid = True

        # Add appropriate answer to answer list
        if valid:
            answers.append('yes')
        else:
            answers.append('no')

    # Print results when done
    for answer in answers:
        print(answer)


def get_multiples(num: int, max: int):
    
    multiples = []
    iterations = 1

    while True:
        if (num * iterations) > max:
            return multiples
        
        multiples.append((num * iterations))
        iterations += 1

if __name__ == '__main__':
    main()