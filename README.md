A lightweight Python CLI tool for efficiently tracking student attendance, preventing duplicates, and exporting daily reports to a text file. 📝✅


# 📚 Student Attendance Tracker

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

A simple and efficient **Python Command-Line Interface (CLI)** application designed to help teachers or class representatives record student attendance quickly. It validates inputs, prevents duplicate entries, and saves the final record to a local text file.

## 🚀 Features

* **User-Friendly Interface:** Simple text-based prompts to guide you through the process.
* **Input Validation:** Ensures names and times are not left empty.
* **Duplicate Prevention:** Checks if a student has already been recorded to avoid double entries.
* **Summary Report:** Displays a clean table of all present students in the terminal.
* **File Export:** Options to save the daily attendance log to a `attendance.txt` file for record-keeping.

## 🛠️ Technologies Used

* **Language:** Python 3
* **Libraries:** Standard Python libraries (No external installation required!)

## 📋 How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/attendance-tracker.git](https://github.com/your-username/attendance-tracker.git)
    ```
2.  **Navigate to the directory:**
    ```bash
    cd attendance-tracker
    ```
3.  **Run the script:**
    ```bash
    python main.py
    ```
    *(Note: Make sure your python file is named `main.py` or replace it with your filename)*

## 💻 Usage Example

Here is what the tool looks like when running:


--- Simple Student Attendance Tracker ---
This tool helps you record student check-in times.

How many students do you want to record? 2

Student 1:
  Enter Name: Rahul
  Enter Time (e.g., 09:00 AM): 09:05 AM
  Saved!

Student 2:
  Enter Name: Amit
  Enter Time (e.g., 09:00 AM): 09:10 AM
  Saved!

========================================
Student Name         | Time           
----------------------------------------
Rahul                | 09:05 AM       
Amit                 | 09:10 AM       
----------------------------------------
Total Present: 2
========================================


Here is the best Repository Description and a professional README.md file content, customized for your specific Python project.

1. Repository Description (For the "About" section)
Copy and paste this into the "Description" box on GitHub:

"A lightweight Python CLI tool for efficiently tracking student attendance, preventing duplicates, and exporting daily reports to a text file. 📝✅"

2. README.md Content
Create a new file named README.md in your repository and paste the following code into it. I have formatted it to look professional on GitHub.

Markdown

🔮 Future Improvements
[ ] Add Excel (.csv) export support.

[ ] specific database connectivity (SQL) for long-term storage.

[ ] Add a Graphical User Interface (GUI) using Tkinter.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

Made with ❤️ by Lokesh Tushir
