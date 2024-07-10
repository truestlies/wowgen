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

def get_non_empty_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if len(user_input) >= 1:
            return user_input

def interactive_mode():
    length = int(get_non_empty_input("Enter password length: "))

    if 'y' in get_non_empty_input("Use uppercase letters? (yes/no): ").lower():
        use_uppercase = True
    else: use_uppercase = False
    
    if 'y' in get_non_empty_input("Use numbers? (yes/no): ").lower():
        use_numbers = True
    else: use_numbers = False
    
    if 'y' in get_non_empty_input("Use special characters? (yes/no): ").lower():
        use_special = True
    else: use_special = False

    if 'y' in get_non_empty_input("Exclude similar characters (i, l, 1, o, 0)? (yes/no): ").lower():
        exclude_similar = True
    else: exclude_similar = False

    custom_chars = input("Enter custom characters to use (leave blank for default): ")
    
    word_list_path = Path(__file__).parent / 'wordlist.txt'
    if not word_list_path.exists():
        print("Wordlist file not found. Memorable passwords are unavailable.")
        memorable = False
        word_count = 0
        separator = ''
    else:
        if 'y' in get_non_empty_input("Generate a memorable password? (yes/no): ").lower():
            word_count = int(get_non_empty_input("Number of words for memorable password: "))
            separator = get_non_empty_input("Separator for words: ")

    return {
        "length": length,
        "use_uppercase": use_uppercase,
        "use_numbers": use_numbers,
        "use_special": use_special,
        "exclude_similar": exclude_similar,
        "custom_chars": custom_chars,
        "memorable": memorable,
        "word_count": word_count,
        "separator": separator
    }

def main():
    parser = argparse.ArgumentParser(description="Password generator script")
    parser.add_argument("-l", "--length", type=int, help="Length of the password")
    parser.add_argument("-u", "--uppercase", action="store_true", help="Include uppercase letters")
    parser.add_argument("-n", "--numbers", action="store_true", help="Include numbers")
    parser.add_argument("-s", "--special", action="store_true", help="Include special characters")
    parser.add_argument("-x", "--exclude-similar", action="store_true", help="Exclude similar characters (i, l, 1, o, 0)")
    parser.add_argument("-c", "--custom-chars", type=str, help="Custom characters to use")
    parser.add_argument("-m", "--memorable", action="store_true", help="Generate a memorable password using random words")
    parser.add_argument("-w", "--word-count", type=int, default=4, help="Number of words in a memorable password (default: 4)")
    parser.add_argument("-p", "--separator", type=str, default='-', help="Separator for words in a memorable password (default: '-')")
    parser.add_argument("-d", "--default", action="store_true", help="Quickly generate a password with preset settings: length 15, with: uppercase, numbers, & special characters")
    parser.add_argument("-i", "--interactive", action="store_true", help="Run in interactive mode")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    if args.interactive:
        user_input = interactive_mode()
        args.length = user_input["length"]
        args.uppercase = user_input["use_uppercase"]
        args.numbers = user_input["use_numbers"]
        args.special = user_input["use_special"]
        args.exclude_similar = user_input["exclude_similar"]
        args.custom_chars = user_input["custom_chars"]
        args.memorable = user_input["memorable"]
        args.word_count = user_input["word_count"]
        args.separator = user_input["separator"]

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
    print(f"\nGenerated password: {password}")
    print(f"Password strength: {strength_info['strength']} (Length score: {strength_info['length_score']}, Variety score: {strength_info['variety_score']})")

if __name__ == "__main__":
    main()
