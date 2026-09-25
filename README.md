# Notes Telegram Bot 📝

An asynchronous Telegram bot for creating, viewing, and managing personal notes.  
The bot ensures privacy by strictly isolating data based on each user's unique Telegram ID.

## Features

- ➕ **Add notes** — quickly save text notes.
- 📋 **View notes** — display a numbered list of all your saved notes.
- 🗑 **Delete notes** — remove specific notes by their ID.
- 🔒 **Data isolation** — each user can only see and interact with their own notes.

## Tech Stack

- **Language:** Python 3
- **Framework:** aiogram
- **Database:** SQLite
- **Testing:** pytest

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/nikitamy73/notebot.git
cd notebot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install aiogram pytest
```

### 4. Get a Telegram Bot Token

1. Open Telegram and find **@BotFather**.
2. Send `/newbot` and follow the instructions.
3. Copy the HTTP API token.

### 5. Configure the bot

Open `bot.py` and replace the placeholder with your token:

```python
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
```

> Do not commit your real token to GitHub.

## Running the Bot

```bash
python bot.py
```

On first run, the bot automatically creates `notes.db` and starts polling for messages.

## Available Commands

| Command | Description |
|---|---|
| `/start` | Displays the welcome message and available commands. |
| `/add <text>` | Saves a new note. Example: `/add Buy groceries` |
| `/list` | Shows all your saved notes. |
| `/delete <id>` | Deletes a note by its number. Example: `/delete 1` |

## Testing

The project includes unit tests for the core database logic: adding, retrieving, and deleting notes.

Run tests:

```bash
pytest test_bot.py
```

## Project Structure

```text
notebot/
├── bot.py
├── test_bot.py
├── notes.db          # created automatically after first run
└── README.md
```

## License

This project is open-source and available for educational purposes.
