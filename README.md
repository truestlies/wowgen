# WowGen: A Cryptographically Secure Password Generator

WowGen is a command-line tool for generating truly random, cryptographically secure passwords. It offers a variety of options to customize the generated password, including length, uppercase letters, numbers, and special characters.

## Features
- **Length**: Specify the length of the password.
- **Uppercase letters**: Option to include uppercase letters.
- **Numbers**: Option to include numbers.
- **Special characters**: Option to include special characters.
- **Exclude similar characters**: Option to exclude visually similar characters like `i`, `l`, `1`, `o`, `0`.
- **Memorable passwords**: Generate memorable passwords using a combination of random words.
- **Custom character set**: Specify a custom set of characters to include in the password.
- **Default settings**: Quickly generate a password with preset settings.
- **Password strength analysis**: Automatically assesses the strength of generated passwords.

## Password strength analysis
WowGen now includes a **Password strength analysis** feature that evaluates the strength of generated passwords. This analysis is based on the length and variety of characters in the password.

### Strength Categories
- **Strong**: Meets or exceeds the recommended length and character variety criteria.
- **Moderate**: Partially meets the recommended criteria.
- **Weak**: Falls short of the recommended criteria.

### Example
When you generate a password, the script will provide a strength evaluation:

```sh
Generated password: Abc123!@#
Password strength: Strong (Length score: 9, Variety score: 8)
```
<br>

## Installation and requirements
- Python 3.x +
```sh
pip install -r requirements.xt
```

<br>

## How to use wowgen

### Basic usage
Generates a 12-character password with lowercase letters only.
```sh
python wowgen.py
```

### Custom length
Specify a different length.
```sh
python wowgen.py -l 16
```

### Include uppercase letters
Include uppercase letters in the password.
```sh
python wowgen.py -u
```

### Include numbers
Include numbers in the password.
```sh
python wowgen.py -n
```

### Include special characters
Include special characters in the password.
```sh
python wowgen.py -s
```

### Exclude similar characters
Exclude visually similar characters from the password.
```sh
python wowgen.py -e
```

### Custom character set
Specify a custom set of characters to include in the password.
```sh
python wowgen.py -c "abcdef1234!@"
```

### Memorable passwords
Generate a memorable password using random words.
```sh
python wowgen.py -m
```

### Word count for memorable passwords
Specify the number of words in a memorable password (default: 4).
```sh
python wowgen.py -m -w 5
```

### Separator for memorable passwords
Specify the separator for words in a memorable password (default: '-').
```sh
python wowgen.py -m -p "_"
```

### Default settings
Quickly generate a password with preset settings: length 16, include uppercase, numbers, and special characters.
```sh
python wowgen.py -d
```

## Example commands
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

Note: For the memorable password feature to work, ensure a file named `wordlist.txt` is in the same directory as the script containing a list of words, one per line.
