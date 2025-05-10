MORSE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ' ': '/'
}

REVERSE_DICT = {v: k for k, v in MORSE_DICT.items()}

def encode_to_morse(text):
    return ' '.join(MORSE_DICT.get(char.upper(), '') for char in text)

def decode_from_morse(code):
    return ''.join(REVERSE_DICT.get(symbol, '') for symbol in code.split())

if __name__ == "__main__":
    print("📡 Morse Code Translator")
    print("1. Encode to Morse\n2. Decode from Morse\n")

    choice = input("Choose 1 or 2: ").strip()
    if choice == '1':
        msg = input("Enter message: ")
        print("🔐 Morse Code:\n", encode_to_morse(msg))
    elif choice == '2':
        code = input("Enter Morse code (use spaces between symbols): ")
        print("🔓 Decoded Message:\n", decode_from_morse(code))
    else:
        print("❌ Invalid choice.")
