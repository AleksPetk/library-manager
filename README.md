# library-manager
CLI Library Manager written in Python (macOS). Uses OOP, JSON persistence, and clean architecture. LibraryManager controls data and rules, GeneralManager extends privileges. Supports adding, borrowing, returning books, bulk operations, and report generation.

Library Manager 

A command-line Library Management System written in Python.

This project manages a small library using clean object-oriented design. It supports normal users and a General Manager with extended privileges. All data is stored persistently using JSON.

Features:
	•	Add, remove, list books
	•	Borrow and return books
	•	Persistent storage using JSON
	•	General Manager functions:
	•	Bulk add books
	•	Remove all books (protected)
	•	Generate daily TXT reports
	•	Single source of truth for library data
	•	Clear separation between logic and UI
	•	Uses inheritance for privilege control

Architecture:
	•	Book: represents a single book
	•	LibraryManager: controls all data, rules, and persistence
	•	GeneralManager: extends LibraryManager with admin privileges
	•	JSON for persistence, TXT for reports

Project Structure:
library-manager/
main.py
library_manager.py
book.py
library.json
txtFolder/

Tech Stack:
Python 3
JSON
datetime, random, os

Run:
python3 main.py

Notes:
This project was built for learning OOP, inheritance, file handling, and clean program structure. Runs entirely in terminal.
