# Countdown_Timer

## Overview
This is a simple Countdown Timer application built using Python and Tkinter. It allows users to set a countdown duration in minutes or seconds, displays a live countdown, and alerts the user when the time is up using a popup notification and sound.

## Features
- **GUI Interface**: Users can enter the countdown time and control the timer with buttons.
- **Countdown Display**: The timer updates in real-time.
- **Popup Notification**: Alerts the user when time is up.
- **Sound Alert**: Beeps when the countdown ends.
- **Pause/Resume Functionality**: Users can pause and resume the countdown.

## Technologies Used
- **Python** (Core logic)
- **Tkinter** (GUI interface)
- **Threading** (For handling countdown without freezing the UI)
- **Winsound** (For sound alerts, Windows only)

## Installation
### Requirements
Ensure you have Python installed on your system. This program requires the following libraries:
```sh
pip install tk
```

## Usage
1. Run the Python script:
```sh
python countdown_timer.py
```
2. Enter the countdown duration in the input field (e.g., `2m` for 2 minutes, `30s` for 30 seconds).
3. Click the **Start** button to begin the countdown.
4. Click **Pause/Resume** to control the timer.
5. A popup and sound alert will notify you when the countdown ends.

## Notes
- This program is designed for Windows. If running on another OS, replace `winsound` with an equivalent sound alert library.
- The GUI is built using Tkinter, which is included in standard Python distributions.

## License
This project is open-source and available for modification and distribution.

## Author
Developed by Kanisha

![Screenshot 2025-02-24 162201](https://github.com/user-attachments/assets/3916a313-ebcc-4994-8554-4235219a5cec)
![Screenshot 2025-02-24 162143](https://github.com/user-attachments/assets/accee6f5-2255-46a8-81cb-7adbf90d99ee)
