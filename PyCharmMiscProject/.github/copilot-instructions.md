# Copilot Instructions for AI Timetable Project

## Overview
This project is a collection of Python scripts for managing and automating school timetables, teacher alerts, and user authentication. The codebase is organized as standalone scripts, each handling a distinct feature. There is no central framework or package structure; scripts interact via shared conventions and data formats.

## Major Components
- **AI TIMETABLE.py**: Generates a randomized timetable assigning subjects, teachers, and rooms to timeslots. Uses round-robin logic to avoid duplicate assignments within a cycle.
- **ALERT CALL.py**: Monitors the timetable and sends alerts to teachers before their classes start. Alerts are simulated via print statements; replace with actual notification logic as needed.
- **LOGIN INFO.py**: Implements a Tkinter-based login GUI with SQLite for user authentication. Registers a default admin user and validates credentials before granting access.
- **main. py.py**: Defines core data structures for days, periods, classes, subjects, and rooms. Serves as a configuration and data model reference for timetable generation.
- **app.py, timetable.py, script.py**: Currently empty or stubs; use these for future expansion or refactoring.

## Data Flow & Integration
- Timetable data is passed as Python dictionaries/lists between scripts. There is no persistent cross-script storage; each script runs independently.
- Teacher alert logic expects timetable entries with `subject`, `teacher`, `room`, and `start_time` fields.
- User authentication is handled via SQLite (`users.db`). Credentials are checked before launching timetable features.

## Developer Workflows
- **Run scripts directly**: Use `python <scriptname>.py` to execute features. No build system or test suite is present.
- **Database setup**: The first run of `LOGIN INFO.py` creates the `users.db` file and registers a default user.
- **Debugging**: Use print statements and Tkinter message boxes for feedback. No logging or error handling conventions beyond basic try/except.

## Project-Specific Patterns
- **Standalone scripts**: Each feature is a separate `.py` file. There is no import-based module structure.
- **Round-robin assignment**: Timetable generation avoids teacher/room duplication by tracking usage and resetting after each cycle.
- **Alert timing**: Alerts are sent 5 minutes before class start, checked every minute.
- **GUI conventions**: Tkinter is used for login; message boxes provide user feedback.

## Key Files
- `AI TIMETABLE.py`: Timetable generation logic
- `ALERT CALL.py`: Teacher alert system
- `LOGIN INFO.py`: User authentication GUI
- `main. py.py`: Data model and configuration

## Example Usage
- To generate a timetable: `python "AI TIMETABLE.py"`
- To send alerts: `python "ALERT CALL.py"`
- To authenticate users: `python "LOGIN INFO.py"`

## Notes
- No external dependencies beyond Python standard library and Tkinter.
- Scripts are not interconnected via imports; copy/paste data as needed for integration.
- Expand empty files (`app.py`, `timetable.py`, `script.py`) for new features.

---
For questions or missing details, review the above scripts or ask for clarification on specific workflows or conventions.
