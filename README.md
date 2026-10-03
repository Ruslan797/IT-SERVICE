# IT-Service Hamburg · Norderstedt

Practical IT service project for local computer support, automation, data migration and DevOps learning.

## Project Components

### Website

Responsive website for local IT services in Hamburg and Norderstedt.

Services include:

- Windows and Linux setup
- PC and laptop diagnostics
- SSD and RAM upgrades
- Data transfer and backup
- Software and driver installation
- System optimization
- Web design

### Telegram Bot

Telegram bot for receiving customer service requests.

The bot runs as a Python service and uses environment variables for configuration and secrets.

### Docker

The project can run with Docker Compose.

Services include:

- Website served by Nginx
- Python Telegram bot

### Data Transfer Tool

Python utility for safe file migration between computers, external drives and backup locations.

Current features:

- Recursive file scanning
- File and storage analysis
- File categorization
- Source and destination comparison
- Missing file detection
- Different file size detection
- Transfer size calculation
- Free disk space check
- User confirmation before copying
- Directory structure preservation
- File metadata preservation
- Post-copy verification

## Safety

The Data Transfer Tool is designed to avoid destructive operations.

- Source files are not deleted
- Missing files are copied
- Existing files with different sizes are reported separately
- Different files are not automatically overwritten
- Available disk space is checked before transfer
- Copied files are verified after transfer

## Data Transfer Tool Structure

```text
tools/data_transfer/
├── scanner.py
├── analyzer.py
├── comparator.py
├── copier.py
├── verifier.py
└── transfer.py
```

## Run Data Transfer Tool

From the project root:

```bash
python tools/data_transfer/transfer.py
```

The program asks for:

```text
Enter source folder:
Enter destination folder:
```

It analyzes the source, compares both locations and displays a transfer plan before copying any files.

## Environment Variables

Secrets and local configuration are stored in `.env`.

The `.env` file is excluded from Git and must not be committed.

## Technologies

- Python
- FastAPI
- python-telegram-bot
- HTML
- CSS
- JavaScript
- Docker
- Docker Compose
- Nginx
- Git