# DATAx Project

A Python-based user authentication and task management system with SQLite database integration.

## 📋 Description

DATAx is a command-line application that provides user registration, authentication, and task management capabilities. The system uses SQLite for data persistence and implements secure password handling using Python's `getpass` module.

## 🚀 Features

- **User Registration**: Register new users with secure password input
- **User Login**: Authenticate users with username and password
- **Task Management**: Create, view, update, and delete tasks
- **User Management**: Manage user accounts and permissions
- **SQLite Database**: Persistent data storage with relational database
- **Secure Password Input**: Hidden password entry using `getpass`

## 📁 Project Structure

DATAx_Project/ \n
   ├── data/
      ├── database.db # SQLite database file 
      └── database.py # Database configuration and setup 
   ├── login_manage/ 
      ├── login.py # User login functionality
      └── register.py # User registration functionality 
   ├── tasks/ 
      ├── task_management.py # Task CRUD operations
      └── user_management.py # User account management 
   ├── main.py # Application entry point 
   └── .venv/ # Virtual environment (not in repo)``` 

## 🛠️ Technologies

- **Python 3.10.11**
- **SQLite3** - Database
- **virtualenv** - Python environment management

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd DATAx_Project
   ```

2. **Create and activate virtual environment**
   ```bash
   # Create virtual environment
   python -m venv .venv

   # Activate on macOS/Linux
   source .venv/bin/activate

   # Activate on Windows
   .venv\Scripts\activate
   ```

3. **Install dependencies** (if any)
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

### Running the Application

Run the application from a **real terminal** (not IDE console) for proper password security:
```

bash
Activate virtual environment first
source .venv/bin/activate # macOS/Linux
or
.venv\Scripts\activate # Windows
Run the main application
python main.py```
   ```

### Important: Terminal Requirement

⚠️ **Run from a real terminal** (Terminal.app, Command Prompt, etc.) instead of IDE's built-in console to ensure password input is properly hidden.

## 🔐 Security Notes

- Passwords are entered using `getpass.getpass()` which hides input from the terminal
- Always run the application from a proper terminal for security features to work correctly
- Database file (`database.db`) should not be committed to version control in production

## 📝 Database Schema

The application uses SQLite with the following main tables:

- **login_manage**: Stores user credentials and registration information
- Additional tables for task management and user data

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

[Add your license here - e.g., MIT, Apache 2.0, etc.]

## 👤 Author

Fynn C.

