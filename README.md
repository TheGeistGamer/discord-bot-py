# Discord Bot

A simple Discord bot built with Python using `discord.py`.

This project automatically welcomes new members when they join the server, assigns them a default role, and includes basic text commands. The project uses `uv` for dependency management and running the bot.

## Features

- Sends a welcome message when a user joins
- Automatically assigns a default role
- Basic text commands
- Uses environment variables with `.env`
- Managed and executed with `uv`
- Beginner-friendly project structure

## Commands

- `$hello` → Replies with `Hello World!`
- `$ping` → Replies with `Pong!`
- `$meme` → Sends a random meme response

## Technologies

- Python 3
- discord.py
- python-dotenv
- uv

## Project Structure

```text
project/
├── .env
├── pyproject.toml
├── uv.lock
└── src/
    └── main.py