def main():

    # Read num test cases
    num_cases = int(input())

    # Initialize answer list
    answers = []

    # Loop over num test cases and add result to answers
    for _ in range(0, num_cases):

        # Read number and how many times to append
        n, k = input().split(' ')

        # Initialize p
        p = ''

        # Append n to p, k times
        for _ in range(0, int(k)):
            p += n

        # Add super_digit of p to answers
        answers.append(super_digit(p))

    # Print results
    for answer in answers:
        print(answer)

def super_digit(imposter_num: str) -> str:
    if len(imposter_num) == 1:
        return imposter_num
    
    total = 0

    for digit in imposter_num:
        total += int(digit)

    return super_digit(str(total))

if __name__ == '__main__':
    main()