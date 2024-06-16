import argparse, secrets, string, sys

def generate_password(length, use_uppercase, use_numbers, use_special):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if len(characters) == 0:
        raise ValueError("No characters available to generate password")
    
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="WowGen: A cryptographically secure password generator")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password (default: 12)")
    parser.add_argument("-u", "--uppercase", action="store_true", help="Include uppercase letters")
    parser.add_argument("-n", "--numbers", action="store_true", help="Include numbers")
    parser.add_argument("-s", "--special", action="store_true", help="Include special characters")
    args = parser.parse_args()

    try:
        password = generate_password(args.length, args.uppercase, args.numbers, args.special)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
