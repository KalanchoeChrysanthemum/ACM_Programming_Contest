def main():

    # Letter to morse code map
    letter_to_morse: dict = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..'
    }

    # Read in the number of inputs
    num_cases = input()

    # Initialize results
    results: list[list] = []

    # Loop over the number of words, reading in each word
    for _ in range(0, int(num_cases)):

        # Read in the word
        word = input()

        # Initialize morse code conversion array
        curr_morse_code = []

        # Convert word to morse code and store in array
        for char in word:
            curr_morse_code.append(letter_to_morse.get(char))

        # Add converted word to results
        results.append(curr_morse_code)

    # Print converted words with proper formatting
    for result in results:
        print(' '.join(result))
    
if __name__ == '__main__':
    main()