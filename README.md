# Simple Caesar Cipher

## Overview

This project is a simple implementation of the Caesar Cipher algorithm using Python. The program allows users to encrypt and decrypt messages by shifting letters in the alphabet using a custom shift value entered by the user.

The Caesar Cipher is one of the oldest and most famous encryption techniques in classical cryptography. It works by replacing each letter with another letter located a fixed number of positions away in the alphabet.

---

## Features

* Encrypt text messages
* Decrypt encrypted messages
* Supports uppercase and lowercase letters
* Keeps numbers, spaces, and symbols unchanged
* Automatic alphabet wrapping
* Simple and beginner-friendly Python code

---

## How It Works

The program asks the user to:

1. Enter a message
2. Enter a shift value
3. Choose:

   * `e` for encryption
   * `d` for decryption

The program then loops through each character in the message and shifts alphabet letters based on the chosen operation.

Example with shift value = 3:

* A → D
* B → E
* X → A

---

## Example

### Input

```python id="s8k2ma"
Enter your message: hello
Enter shift value: 3
Type 'e' for encrypt or 'd' for decrypt: e
```

### Output

```python id="n2p8qx"
Result: khoor
```

---

## Technologies Used

* Python
* ASCII character manipulation using:

  * `ord()`
  * `chr()`

---

## Concepts Used

This project demonstrates:

* Loops
* Conditional statements
* String handling
* ASCII values
* Basic cryptography concepts

---

## Purpose

The purpose of this project is to practice Python programming fundamentals and understand how basic encryption algorithms work.
