import sys, os, string, secrets, argparse, re
from pathlib import Path

def load_word_list():
    word_list_path = Path(__file__).parent / 'wordlist.txt'
    if not word_list_path.exists():
        print("Wordlist file not found. Memorable passwords will not be available.")
        return []
    with open(word_list_path, 'r') as file:
        words = file.read().splitlines()
    return words

def generate_password(length, use_uppercase, use_numbers, use_special, exclude_similar, custom_chars):
    if custom_chars:
        characters = custom_chars
    else:
        characters = string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_numbers:
            characters += string.digits
        if use_special:
            characters += string.punctuation
        if exclude_similar:
            characters = ''.join(c for c in characters if c not in 'il1o0')

    if len(characters) == 0:
        raise ValueError("No characters available to generate password")
    
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def generate_memorable_password(num_words, separator, word_list):
    if not word_list:
        raise ValueError("Word list is empty. Cannot generate memorable password.")
    return separator.join(secrets.choice(word_list) for _ in range(num_words))

def analyze_password_strength(password):
    length_score = len(password)
    variety_score = len(set(password))
    
    length_criteria = 12
    variety_criteria = 8

    if length_score >= length_criteria and variety_score >= variety_criteria:
        strength = "Strong"
    elif length_score >= length_criteria / 2 and variety_score >= variety_criteria / 2:
        strength = "Moderate"
    else:
        strength = "Weak"

    return {
        "length_score": length_score,
        "variety_score": variety_score,
        "strength": strength
    }

def main():
    parser = argparse.ArgumentParser(description="WowGen: A cryptographically secure password generator with cool features")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password (default: 12)")
    parser.add_argument("-u", "--uppercase", action="store_true", help="Include uppercase letters")
    parser.add_argument("-n", "--numbers", action="store_true", help="Include numbers")
    parser.add_argument("-s", "--special", action="store_true", help="Include special characters")
    parser.add_argument("-e", "--exclude-similar", action="store_true", help="Exclude visually similar characters (i, l, 1, o, 0)")
    parser.add_argument("-c", "--custom-chars", type=str, help="Specify a custom set of characters to include in the password")
    parser.add_argument("-m", "--memorable", action="store_true", help="Generate a memorable password using random words")
    parser.add_argument("-w", "--word-count", type=int, default=4, help="Number of words in a memorable password (default: 4)")
    parser.add_argument("-p", "--separator", type=str, default='-', help="Separator for words in a memorable password (default: '-')")
    parser.add_argument("-d", "--default", action="store_true", help="Quickly generate a password with preset settings: length 15, with: uppercase, numbers, & special characters")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    if args.default:
        password = generate_password(15, True, True, True, False, None)
    elif args.memorable:
        word_list = load_word_list()
        password = generate_memorable_password(args.word_count, args.separator, word_list)
    else:
        try:
            password = generate_password(args.length, args.uppercase, args.numbers, args.special, args.exclude_similar, args.custom_chars)
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)

    strength_info = analyze_password_strength(password)
    print(f"Generated password: {password}")
    print(f"Password strength: {strength_info['strength']} (Length score: {strength_info['length_score']}, Variety score: {strength_info['variety_score']})")

if __name__ == "__main__":
    main()
