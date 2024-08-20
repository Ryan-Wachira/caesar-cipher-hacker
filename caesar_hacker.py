# Displays the program title.
print('Caesar Cipher Hacker, by Ryan')

# Get the encrypted message from the user.
print('Enter the encrypted Caesar cipher message to hack.')
message = input('> ')

# Define the set of symbols that can be decrypted (A-Z).
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Trys every possible key to decrypt the message.
for key in range(len(SYMBOLS)):
    translated = ''

    # Decrypt each symbol in the message using the current key.
    for symbol in message:
        if symbol in SYMBOLS:
            # Find the position of the symbol in the SYMBOLS set.
            num = SYMBOLS.find(symbol)
            # Shift the position by the key to decrypt.
            num = num - key

            # Handles the wrap-around if the number is less than 0.
            if num < 0:
                num += len(SYMBOLS)

            # Add the decrypted symbol to the translated message.
            translated += SYMBOLS[num]
        else:
            # If the symbol is not in SYMBOLS, add it unchanged.
            translated += symbol

    # Displays the key and the decrypted message for the user to review.
    print('Key #{}: {}'.format(key, translated))
