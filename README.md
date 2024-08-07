# ToDo App using Flask and SQLAlchemy

## Description

A simple ToDo application built with Flask. This application allows users to manage tasks with optional deadlines, mark tasks as done or not done, and view the list of tasks in a user-friendly interface.

## Features

- Add tasks with optional deadlines
- Mark tasks as done or not done
- View tasks in a table format
- Strikethrough completed tasks
- Responsive and styled with CSS

## Requirements

Ensure you have Python installed on your system. This project requires the following Python packages:

- Flask
- Flask-SQLAlchemy
- SQLAlchemy
- Flask-WTF

You can install these packages using the `requirements.txt` file.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/ToDo-using-Flask.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd ToDo-using-Flask
   ```

3. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment:**

   ```bash
   venv\Scripts\activate
   ```

5. **Install the Required Packages:**

   ```bash
   pip install -r requirements.txt
   ```

6. **Run the Application:**

   ```bash
   flask run
   ```

## Usage

- Add a Task: Enter the task name and an optional deadline in the form and click "Add Task".
- Update a Task: Click the "Update" link next to a task to modify its details.
- Delete a Task: Click the "Delete" link next to a task to remove it.

## Contributing

Feel free to submit issues and pull requests. Please ensure that any changes adhere to the project's coding style and include appropriate tests.
