# Network Security Scanner & Firewall Visualizer

## Objective
This project is a web-based Information Security tool designed to bridge offensive reconnaissance and defensive rule-setting. It features an active network scanning engine to identify open ports/services and an interactive firewall simulator to visualize traffic flow based on priority-chained security rules.

Created for Information Security - Assignment 3.

## Technologies Used
* **Backend:** Python 3, Flask
* **Scanning Engine:** `python-nmap` (Python wrapper for Nmap)
* **Frontend:** HTML5, CSS3, Vanilla JavaScript

## Prerequisites
⚠️ **CRITICAL:** This application relies on the Nmap scanning engine. You **must** have the Nmap system software installed on your machine for the backend to function.
* Download Nmap here: [https://nmap.org/download.html](https://nmap.org/download.html)

## Installation & Setup
1. Clone this repository to your local machine.
2. Open your terminal and navigate to the project directory.
3. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
## How to Run
1. Start the Flask backend server:
   ```bash
   python app.py
2. Open your web browser and navigate to: http://127.0.0.1:5000
3. Enter a target IP (e.g., 127.0.0.1 for localhost) and execute a scan.
4. Scroll down to the Firewall Simulator to add custom Allow/Deny rules and test simulated packet flow.
