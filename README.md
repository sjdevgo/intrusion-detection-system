# Simple Log-Based Intrusion Detection System (LogIDS)

This project simulates a basic log intrusion detection system (IDS) using Python.

It analyzes authentication logs (`auth.log`) to detect:
- Possible brute-force login attacks (many failed login attempts from the same IP)
- Suspicious night-time login activities (between 00:00–06:00)

## Project Structure



## How to Run

1. Install Python 3 if you haven't already.
2. Clone this repository or download the project files.
3. Navigate to the project folder and run:

```bash
python detect_intrusions.py


