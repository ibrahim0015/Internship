# CLI To-Do List Application (JSON Storage)

A simple command-line based **To-Do List application** built with Python that uses a JSON file as a lightweight database. The project separates **storage logic** and **user interaction** for better structure and readability.

## Features

- Display all tasks sorted by priority
- Add new tasks with title, due date, and priority
- Delete tasks by title
- Mark tasks as completed
- Persistent storage using a JSON file (`todos.json`)

## Project Structure

.
├── main.py # CLI interface and user interaction
├── storage.py # Task storage and file handling logic
├── todos.json # JSON file used as database
└── README.md

markdown
Copy code

## How It Works

- `main.py` handles user input and menu selection
- `storage.py` handles:
  - Reading from `todos.json`
  - Writing updates back to the file
  - Sorting tasks by priority
- Each task is stored as a dictionary with:
  - `title`
  - `date`
  - `priority`
  - `done`

## Requirements

- Python 3.x
- No external libraries required

## Setup

Create a `todos.json` file in the same directory with the following initial content:

[]

csharp
Copy code

## How to Run

Run the application from the terminal:

python main.py

shell
Copy code

## Menu Options

Display the todo list

Add a task

Delete a task

Mark a task as done

Exit

pgsql
Copy code

## Notes

- Tasks are identified uniquely by their title
- Priority is numeric (lower number = higher priority)
- Data is saved persistently in `todos.json`
- Designed as a beginner-friendly project to understand file handling and modular code