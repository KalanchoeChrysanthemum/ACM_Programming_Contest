def main():
    # Read number of parties
    num_iterations = input()

    # Check for invalid num
    if num_iterations == '0' or num_iterations == '':
        return
    
    # Initialize results
    answers: list[int] = []
    
    # Loop over each party
    for x in range(0, int(num_iterations)):
        # Read num people coming to party (this is useless)
        num_people = input()

        # Read in each of the people in the party, converting to int and sorting
        people = sorted([int(person) for person in input().split(' ')])

        # Initialize current people in the party
        curr_people = 0

        # Loop over each person coming to the party and see if there's enough people for them to join
        for person in people:
            if person <= curr_people:
                curr_people += 1

        # Add number of people in the current party to answers
        answers.append(curr_people)

    # Print results
    for answer in answers:
        print(str(answer))


if __name__ == '__main__':
    main()