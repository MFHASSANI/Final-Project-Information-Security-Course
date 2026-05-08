# Information Security Final Project

## Group Project

**Students:** Mohammad Farid Hassani and Project Partner  
**Course:** Information Security  

---

# Project Description

This project was developed for the Information Security course and includes two related cybersecurity tools:

1. Secure Password Generator  
2. File Integrity Monitoring System  

The purpose of this project is to help improve system security by generating strong passwords and monitoring important files for unauthorized modifications.

The Secure Password Generator helps users create secure passwords with different complexity levels and password strength evaluation.

The File Integrity Monitoring System uses SHA-256 hashing to detect file tampering, modifications, deleted files, and newly added files.

---

# Problem It Solves

Weak passwords and unauthorized file modifications are common security problems in computer systems.

This project helps solve these problems by:

- Generating strong and secure passwords
- Monitoring files using SHA-256 hashing
- Detecting unauthorized changes
- Logging security events
- Improving authentication and file integrity security

---

# Architecture Overview

```text
information-security-final-project/
│
├── password-generator/
│   └── main.py
│
├── file-integrity-checker/
│   ├── main.py
│   ├── hashes.json
│   ├── integrity_logs.txt
│   └── monitored_files/
│
├── screenshots/
├── presentation/
└── README.md