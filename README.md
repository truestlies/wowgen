# WowGen: A cryptographically secure password generator

WowGen is a command-line tool for generating truly random, cryptographically secure passwords. It offers a variety of options to customize the generated password, including length, uppercase letters, numbers, and special characters.

## Features
- **Length**: Specify the length of the password.
- **Uppercase Letters**: Option to include uppercase letters.
- **Numbers**: Option to include numbers.
- **Special Characters**: Option to include special characters.

## How to Use

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

### Combine options
Include uppercase letters, numbers, and special characters, and specify a custom length.
```sh
python wowgen.py -u -n -s -l 20
```

## Example commands
Generate a 20-character password with all options:
```sh
python wowgen.py -l 20 -u -n -s
```

## Requirements
- Python 3.x +

## Installation
No installation is required. Simply download the `wowgen.py` script and run it using Python.
