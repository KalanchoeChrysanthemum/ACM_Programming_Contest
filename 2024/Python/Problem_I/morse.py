def main():

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

    num_cases = input()

    results: list[list] = []

    for _ in range(0, int(num_cases)):
        word = input()

        curr_morse_code = []

        for char in word:
            curr_morse_code.append(letter_to_morse.get(char))

        results.append(curr_morse_code)

    for result in results:
        print(' '.join(result))
    
if __name__ == '__main__':
    main()