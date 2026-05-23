message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

choice = input("Type 'e' for encrypt or 'd' for decrypt: ")

result = ""

for char in message:

    if char.isalpha():

        ascii_value = ord(char)

        # ENCRYPT
        if choice == 'e':
            new_ascii = ascii_value + shift

        # DECRYPT
        elif choice == 'd':
            new_ascii = ascii_value - shift

        # Uppercase handling
        if char.isupper():

            if new_ascii > ord('Z'):
                new_ascii -= 26

            if new_ascii < ord('A'):
                new_ascii += 26

        # Lowercase handling
        else:

            if new_ascii > ord('z'):
                new_ascii -= 26

            if new_ascii < ord('a'):
                new_ascii += 26

        result += chr(new_ascii)

    else:
        result += char

print("Result:", result)