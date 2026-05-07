# SecureShield Toolkit

## Project Overview

This project is developed for the Information Security final project course. The toolkit contains two security-related tools:

1. Secure Password Generator
2. File Integrity Checker

Both tools are connected to cybersecurity and help improve system security and data protection.

---

# Problem Statement

Weak passwords and unauthorized file modifications are common security problems. Many users create simple passwords that are easy to guess, and important system files can be modified without detection.

This project helps solve these problems by:
- generating strong and secure passwords
- detecting file tampering using SHA-256 hashing

---

# Tools Included

## 1. Secure Password Generator

This tool generates strong passwords using:
- uppercase letters
- lowercase letters
- numbers
- symbols

The Python `secrets` module is used for cryptographically secure random generation.

### Features
- User chooses password length
- Strong random password generation
- Improved account security

---

## 2. File Integrity Checker

This tool checks whether a file has been modified or tampered with.

The program:
- creates SHA-256 hashes
- stores hashes
- compares hashes during verification

### Features
- SHA-256 hashing
- Integrity verification
- Tampering detection
- File monitoring

---

# Technologies Used

- Python 3
- hashlib
- secrets
- os
- SHA-256

---

# Project Structure

```text
information-security-final-project/
│
├── password-generator/
│   └── password_generator.py
│
├── file-integrity-checker/
│   └── integrity_checker.py
│
├── presentation/
│
├── screenshots/
│
└── README.md
```

---

# How To Run

## Password Generator

```bash
cd password-generator
python3 password_generator.py
```

---

## File Integrity Checker

```bash
cd file-integrity-checker
python3 integrity_checker.py
```

---

# Information Security Perspective

This project demonstrates important cybersecurity concepts:
- secure authentication
- password protection
- SHA-256 cryptographic hashing
- file integrity monitoring
- tampering detection

The password generator protects user accounts, while the integrity checker protects important files from unauthorized modifications.

---

# Future Improvements

Possible future improvements:
- graphical user interface (GUI)
- real-time file monitoring
- password strength meter
- encrypted hash database
- multi-file integrity scanning

---

# Author

Mohammad Farid Hassani

Information Security Final Project
AUCA