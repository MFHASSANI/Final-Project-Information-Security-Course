# Information Security Final Project

## Group Project

**Students:** Mohammad Farid Hassani and Sami Jaberi  
**Course:** Information Security  

---

# Project Description

This project was developed for the Information Security course and includes two related cybersecurity tools:

1. Simple Intrusion Detection System  
2. File Integrity Monitoring System  

The purpose of this project is to improve system security by detecting suspicious activity and monitoring important files for unauthorized modifications.

The Simple Intrusion Detection System helps users monitor unusual activity such as failed login attempts, process changes, and suspicious processes. It also creates security alerts and saves them in a log file.

The File Integrity Monitoring System uses SHA-256 hashing to detect file tampering, modifications, deleted files, and newly added files. The system also creates security logs and stores integrity hashes in a JSON database.

Both projects are related because they focus on protecting systems, detecting unauthorized activity, and securing sensitive information.

---

# Problem It Solves

Unauthorized login attempts, suspicious process activity, and unauthorized file modifications are common security problems in computer systems.

This project helps solve these problems by:

- Detecting failed login attempts
- Monitoring running system processes
- Detecting new, stopped, or suspicious processes
- Monitoring files using SHA-256 hashing
- Detecting unauthorized modifications
- Logging security events
- Improving system security and file integrity
- Helping users protect sensitive information

---

# Features

## Simple Intrusion Detection System

- Failed login detection
- Authentication log analysis
- Process baseline creation
- New process detection
- Stopped process detection
- Suspicious process detection
- Security alert logging
- Command-line support

## File Integrity Monitoring System

- SHA-256 hashing
- File integrity verification
- Tampering detection
- Deleted file detection
- New file detection
- Security logging
- JSON hash database

---

# Technologies Used

## Programming Language

- Python 3

## Simple Intrusion Detection System Libraries

- argparse
- json
- re
- subprocess
- sys
- pathlib
- datetime

## File Integrity Monitoring System Libraries

- hashlib
- json
- os
- pathlib
- datetime

---

# Architecture Overview

```text
information-security-final-project/
│
├── simple-intrusion-detection-system/
│   ├── main.py
│   ├── process_baseline.json
│   ├── ids_alerts.log
│   └── sample_auth.log
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
```

---

# Setup and Run Instructions

## Clone Repository

```bash
git clone [https://github.com/MFHASSANI/-Secure-Password-Generator-Final-Project-for-Information-Security-Course.git](https://github.com/SamiJaberii/FinalProject-Information-Security.git)
```

## Run Secure Password Generator

```bash
cd simple-intrusion-detection-system
python3 main.py
```

## Run File Integrity Monitoring System

```bash
cd file-integrity-checker
python3 main.py
```

---

# Screenshots

Project screenshots are available in the `screenshots/` folder.

Included screenshots:

- IDS banner and main menu
- IDS sample authentication log creation
- IDS failed login detection
- IDS process baseline creation
- IDS alert log results
- Integrity monitoring banner
- Tampering detection results

---

# Presentation

The final project presentation is available in the `presentation/` folder.

---

# Demo Video

## Project Walkthrough Video

[Click here to watch the demo video](https://drive.google.com/file/d/15q4SxVwViBmmEcwesXhcYqQIwxz6yNG3/view?usp=drive_link)

---

# Conclusion

This project successfully demonstrates important Information Security concepts using Python.

The Simple Intrusion Detection System improves system security by helping users detect failed login attempts, process changes, and suspicious activity.

The File Integrity Monitoring System protects important files using SHA-256 hashing and tampering detection.

Both projects help improve cybersecurity awareness and system protection.
