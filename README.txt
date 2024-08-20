# Caesar Cipher Hacker

This project is a Python script that hacks messages encrypted with the Caesar Cipher using a brute-force method. The script tries all possible keys (shifts) to decrypt the message and displays the results for each key.

## How It Works

- The program asks the user to input an encrypted message.
- It then loops through every possible key (0-25) and attempts to decrypt the message by shifting each letter.
- The program outputs each possible decryption so the user can identify the correct one.

## Features

- Brute-force decryption of Caesar Cipher.
- Handles uppercase letters and leaves non-alphabetic characters unchanged.

## Usage

1. Run the script in a Python environment.
2. Input the encrypted message when prompted.
3. Review the output for each key and identify the correct decryption.


## Example

Input (encrypted message): `GDKKN`

Output:
Key #0: GDKKN
Key #1: FCJJM
Key #2: EBIIL
Key #3: DAHHK
Key #4: CZGGJ
Key #5: BYFFI
...