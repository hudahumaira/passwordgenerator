# Password Generator 

A python-based tool that generates strong passwords with built-in rules for safety. The generated passwords meet security standards like minimum length, uppercase, lowercase, digits and special characters. You can choose the length, number of passwords and optinally copy the last one to your clipboard.

## Features

- Generate one or multiple passwords
- Enforces strong password rules:
  - Minimum 8 characters
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one number
  - At least one special character
- Customize desired password length
- Automatically copy the last password to your clipboard (optional)
- Handles invalid inputs and errors gracefully

## Tech Stack

- `random` & `string`: Built-in Python libraries for character selection
- `pyperclip`: Cross-platform clipboard support

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the script:

```bash
python password_generator.py
```