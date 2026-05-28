# ISHA Assistant – Intelligent Windows Automation Assistant

## Project Title

**ISHA Assistant – AI Powered Windows Automation & Voice-Control Assistant**

---

# Brief Description

ISHA Assistant is a Python-based intelligent desktop automation assistant designed for Windows systems. The project allows users to control applications, system settings, and utilities using natural language text commands, keyboard shortcuts, and voice commands.

The assistant processes user input through a custom command-processing pipeline consisting of:

* Input Processing
* Command Parsing
* Validation
* Execution Engine

It supports:

* Opening/closing applications
* Website launching
* Volume & brightness control
* Voice activation
* Keyboard shortcuts
* Internet and disk diagnostics
* Mode-based workflow automation
* REST API backend for frontend integration

The project demonstrates concepts of:

* Natural Language Command Processing
* System Automation
* Voice Recognition
* REST API Development
* Process Management
* Desktop Utility Engineering

---

# Technology Stack and Tools Used

## Programming Language

* Python 3

## Backend Framework

* Flask
* Flask-CORS

## Libraries & Modules

* `speech_recognition`
* `sounddevice`
* `numpy`
* `psutil`
* `pycaw`
* `screen-brightness-control`
* `speedtest-cli`
* `keyboard`

## Development Tools

* VS Code
* Git & GitHub

## Operating System

* Windows 10 / Windows 11

---

# Project Architecture

## Core Modules

### 1. Input Processor

Processes raw text commands and converts number words into numeric values. 

### 2. Command Parser

Converts tokens into structured command instructions using:

* Verb resolution
* Target extraction
* Synonym mapping
* App alias resolution 

### 3. Validator

Validates commands and resolves:

* URLs
* Applications
* Numeric levels
* Fallback behavior 

### 4. Executor

Dispatches validated commands to appropriate handlers. 

### 5. Voice Listener

Activates voice command mode using speech recognition. 

### 6. Flask API Server

Provides REST APIs for frontend communication. 

---

# Features and Functionalities Implemented

## System Control

* Shutdown system
* Restart system
* Lock screen

## Volume Control

* Increase volume
* Decrease volume
* Set exact volume
* Mute/unmute system audio 

## Brightness Control

* Increase brightness
* Decrease brightness
* Set brightness percentage 

## Application Management

* Open installed applications
* Close running applications
* Launch websites
* Browser fallback support

## Voice Assistant

* Wake-word activation (“Isha”)
* Speech-to-command execution

## Keyboard Shortcuts

Custom shortcut mappings supported through JSON configuration. 

## Diagnostics

* Internet speed testing
* Disk usage monitoring  

## Workflow Modes

Create grouped application launch modes such as:

* Study Mode
* Coding Mode
* College Mode
* Home Mode 

## REST API Support

Provides APIs for:

* Commands
* System status
* Metrics
* Shortcuts
* Modes
* Settings

## Smart Command Parsing

Supports:

* Synonyms
* Flexible sentence structures
* Number-word recognition
* Natural language interpretation

---

# Example Commands

```bash
open chrome
open spotify
increase brightness
set volume to 70
mute
check internet
open coding mode
shutdown
```

---

# Folder Structure

```bash
project/
│
├── api_server.py
├── main.py
├── executor.py
├── validator.py
├── command_parser.py
├── input_processor.py
├── command_ir.py
│
├── open_application.py
├── close_application.py
├── set_volume.py
├── set_brightness.py
├── shutdown_restart_lock.py
├── check_disk.py
├── check_internet.py
│
├── voice_listener.py
├── shortcuts.json
├── settings.json
├── modes.json
├── reminders.json
│
├── requirements.txt
└── README.md
```

---

# Installation / Execution Steps to Run the Project

## Step 1: Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_LINK>
```

Example:

```bash
git clone https://github.com/your-username/isha-assistant.git
```

---

## Step 2: Navigate to Project Folder

```bash
cd isha-assistant
```

---

## Step 3: Create Virtual Environment (Recommended)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

Dependencies used: 

---

## Step 5: Run the Assistant

### CLI Mode

```bash
python main.py
```

### API Server Mode

```bash
python api_server.py
```

---

# API Endpoints

| Endpoint               | Method   | Description        |
| ---------------------- | -------- | ------------------ |
| `/api/command`         | POST     | Execute commands   |
| `/api/system/status`   | GET      | System information |
| `/api/system/internet` | GET      | Internet speed     |
| `/api/system/disk`     | GET      | Disk usage         |
| `/api/modes`           | GET/POST | Manage modes       |
| `/api/shortcuts`       | GET/POST | Manage shortcuts   |
| `/api/settings`        | GET/POST | Assistant settings |

---

# Sample Output

## Voice Activation

```bash
Voice active (say 'isha')...
Activated...
Command: open chrome
```

## Disk Check

```bash
Total Disk Space: 512 GB
Used Disk Space: 320 GB
Free Disk Space: 192 GB
```

## Internet Speed

```bash
Download Speed: 120 MBPS
Upload Speed: 45 MBPS
```

---

# Team Members

1. Anushka Patidar
2. Zainab Abbas
3. Shridhi Jain

---

# Screenshots / Output

![1](Screenshots/WhatsApp%20Image%202026-05-28%20at%203.53.15%20PM.jpeg)

![2](Screenshots/WhatsApp%20Image%202026-05-28%20at%203.53.16%20PM.jpeg)

![3](Screenshots/WhatsApp%20Image%202026-05-28%20at%203.53.16%20PM1.jpeg)

![4](Screenshots/WhatsApp%20Image%202026-05-28%20at%203.53.17%20PM2.jpeg)

![5](Screenshots/WhatsApp%20Image%202026-05-28%20at%203.53.18%20PM.jpeg)




---

# Future Enhancements

* AI chatbot integration
* OCR-based automation
* Cross-platform support
* Task scheduling
* GUI desktop application
* Mobile companion app
* Advanced NLP support

---


# Conclusion

ISHA Assistant is an intelligent desktop automation system that combines natural language processing, voice recognition, and system-level automation into a single assistant platform. The project demonstrates practical implementation of automation, command parsing, API integration, and Windows system control using Python.
