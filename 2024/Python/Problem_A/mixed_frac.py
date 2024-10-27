def main():
    # Create a list that stores all the results so it can be printed at the end
    results: list[str] = []

    # Read input until last case
    while True:
        # Get input
        numerator, denominator = input().split(' ')

        # Check last case - print results if done
        if numerator == '0' and denominator == '0':
            break

        # Convert to integers for mathematical operations
        numerator = int(numerator)
        denominator = int(denominator)

        # Simplify fraction
        whole_num = int(numerator / denominator)
        remainder = numerator % denominator

        # Add formatted result to results
        results.append(f'{whole_num} {remainder} / {denominator}')

    # Print simplified fractions
    for result in results:
        print(result)
    

if __name__ == '__main__':
    main()