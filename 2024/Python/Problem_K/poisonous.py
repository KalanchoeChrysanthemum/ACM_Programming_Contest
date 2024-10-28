def main():

    # Read number of test cases
    num_cases = input()

    # Initialize answer list
    answers = []

    # Loop over num cases
    for _ in range(0, int(num_cases)):

        # Read number of plants in the list (useless)
        num_plants = input()

        # Read in each of the plants and convert to int store in list
        plants = [int(plant) for plant in input().split(' ')]

        # Initialize number of days that no plant has died
        num_days = 1

        # Kill off plants that will die until no plant dies, append result to answers
        while True:

            # Kill plants
            new_plants = KILL(plants)

            # If no plants die then return
            if len(new_plants) == len(plants):
                break

            # Update plant list with updated list
            plants = new_plants
            num_days += 1

        # Add result to answers
        answers.append(num_days)

    # Print answers
    for answer in answers:
        print(answer)

def KILL(plants: list[int]) -> list[int]:
    return_list = plants

    if len(plants) == 1:
        return return_list

    for x in range(1, len(plants)):
        if plants[x] > plants[x-1]:
            return_list[x] = -1

    return_list = [plant for plant in return_list if plant > -1]

    return return_list
    
if __name__ == '__main__':
    main()