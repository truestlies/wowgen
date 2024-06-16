# WowGen: A Cryptographically Secure Password Generator

WowGen is a command-line tool for generating truly random, cryptographically secure passwords. It offers a variety of options to customize the generated password, including length, uppercase letters, numbers, and special characters.

## Features
- **Length**: Specify the length of the password.
- **Uppercase Letters**: Option to include uppercase letters.
- **Numbers**: Option to include numbers.
- **Special Characters**: Option to include special characters.
- **Exclude Similar Characters**: Option to exclude visually similar characters like `i`, `l`, `1`, `o`, `0`.
- **Memorable Passwords**: Generate memorable passwords using a combination of random words.
- **Custom Character Set**: Specify a custom set of characters to include in the password.
- **Default Settings**: Quickly generate a password with preset settings.

## How to Use

### Basic Usage
Generates a 12-character password with lowercase letters only.
```sh
python wowgen.py
```

### Custom Length
Specify a different length.
```sh
python wowgen.py -l 16
```

### Include Uppercase Letters
Include uppercase letters in the password.
```sh
python wowgen.py -u
```

### Include Numbers
Include numbers in the password.
```sh
python wowgen.py -n
```

### Include Special Characters
Include special characters in the password.
```sh
python wowgen.py -s
```

### Exclude Similar Characters
Exclude visually similar characters from the password.
```sh
python wowgen.py -e
```

### Custom Character Set
Specify a custom set of characters to include in the password.
```sh
python wowgen.py -c "abcdef1234!@"
```

### Memorable Passwords
Generate a memorable password using random words.
```sh
python wowgen.py -m
```

### Word Count for Memorable Passwords
Specify the number of words in a memorable password (default: 4).
```sh
python wowgen.py -m -w 5
```

### Separator for Memorable Passwords
Specify the separator for words in a memorable password (default: '-').
```sh
python wowgen.py -m -p "_"
```

### Default Settings
Quickly generate a password with preset settings: length 16, include uppercase, numbers, and special characters.
```sh
python wowgen.py -d
```

## Example Commands
Generate a 20-character password with all options:
```sh
python wowgen.py -l 20 -u -n -s
```

Generate a memorable password with 4 words and hyphens as separators:
```sh
python wowgen.py -m
```

Generate a 12-character password excluding similar characters:
```sh
python wowgen.py -l 12 -e
```

Generate a password with a custom character set:
```sh
python wowgen.py -c "abcdef1234!@"
```

## Requirements
- Python 3.x +

## Installation
No installation is required. Simply download the `wowgen.py` script and run it using Python.

## Note
For the memorable password feature to work, ensure there is a file named `wordlist.txt` in the same directory as the script containing a list of words, one per line.
```
