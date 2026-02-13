# League of AI Agents - Final Project

This repository contains the implementation of the **Player** and **Referee** AI agents for the "League of AI Agents" course (MSc Computer Science).

## Documentation

-   [Product Requirements Document (PRD)](PRD.md): Detailed specifications, game rules, and agent requirements.
-   [Implementation Plan](implementation_plan.md): Steps for building and structuring the project.

## Directory Structure

This project is organized into two primary agent modules:

```text
.
├── player/                  # Player Agent Module
│   ├── my_player.py         # Player AI Implementation
│   └── js/config.json       # Player Configuration
├── referee/                 # Referee Agent Module
│   ├── my_referee.py        # Referee AI Implementation
│   └── js/config.json       # Referee Configuration
└── README.md                # Project Documentation
```

## Setup

1.  **Dependencies**:
    -   Python 3.11+
    -   `q21-player` and `q21-referee` SDKs (install via `.whl` files).

2.  **Configuration**:
    -   Navigate to `player/js/` and `referee/js/`.
    -   Copy `config.template.json` to `config.json` and fill in your details.
    -   Place your `credentials.json` (Google OAuth) in both `player/` and `referee/` directories.

## Running

Refer to the PRD for detailed run instructions, including `--scan`, `--watch`, and `--test-connectivity` modes.
