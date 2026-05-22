# Interactive User Configuration Manager

A Python-based Command Line Interface (CLI) application that allows users to dynamically manage their system configuration preferences (such as theme, language, and notifications) in real-time.

Built using **Python 3.13.7**, this project demonstrates the effective use of core data structures, input validation, and real-time state management.

## 🚀 Features
- **Interactive CLI Menu**: A continuous loop structure allowing smooth navigation between operations.
- **Add Settings**: Safely append new key-value pairs (handles tuples, prevents duplicates, and normalizes inputs to lowercase).
- **Update Settings**: Modify existing configurations dynamically with instant feedback.
- **Delete Settings**: Efficiently remove existing keys from the active dictionary.
- **View Settings**: Format and print current configurations cleanly with capitalized keys and proper indentation.

## 🛠️ Tech Stack & Concepts
- **Language**: Python 3.13.7
- **Data Structures**: Dictionaries (for active configurations) & Tuples (for passing key-value pairs).
- **Control Flow**: `while` loops, conditional routing (`if-elif-else`), and input sanitization using `.strip()`, `.lower()`, and `.capitalize()`.

## 📦 How to Run the App

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/ibrahim-hamouda/user-configuration-manager.git](https://github.com/ibrahim-hamouda/user-configuration-manager.git)
