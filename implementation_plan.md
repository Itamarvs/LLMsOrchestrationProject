# Implementation Plan - Project Initialization

## Goal
To initialize the file system structure for the "League of AI Agents" project, ensuring a clean separation between the **Player** and **Referee** agents while maintaining a unified repository.

## Proposed Changes

### Directory Structure
We will create two main subdirectories, `player/` and `referee/`, to isolate their configurations (like `js/config.json`) and dependencies.

```text
/Users/itamarv/.gemini/antigravity/LLMsOrchestration - FInalProject/
├── player/
│   ├── my_player.py       # Player agent implementation stub
│   ├── js/
│   │   └── config.template.json
│   └── requirements.txt
├── referee/
│   ├── my_referee.py      # Referee agent implementation stub
│   ├── js/
│   │   └── config.template.json
│   └── requirements.txt
└── README.md              # Existing, to be updated
```

### Files to Create

#### [NEW] [player/my_player.py](file:///Users/itamarv/.gemini/antigravity/LLMsOrchestration%20-%20FInalProject/player/my_player.py)
A stub implementation of the `PlayerAI` class with the 4 required callbacks (`get_warmup_answer`, `get_questions`, `get_guess`, `on_score_received`).

#### [NEW] [referee/my_referee.py](file:///Users/itamarv/.gemini/antigravity/LLMsOrchestration%20-%20FInalProject/referee/my_referee.py)
A stub implementation of the `RefereeAI` class with the 4 required callbacks (`get_warmup_question`, `get_round_start_info`, `get_answers`, `get_score_feedback`).

#### [NEW] `player/js/config.template.json` & `referee/js/config.template.json`
Template configuration files based on the SDK requirements.

## User Actions Required (Post-Initialization)
1.  **Download SDKs**: Place the `q21_player-*.whl` and `q21_referee-*.whl` files into their respective directories (or a shared `libs/` folder).
2.  **Credentials**: Copy `credentials.json` (Google OAuth) into both `player/` and `referee/` directories.

## Verification Plan
1.  Verify directory structure creation.
2.  Check that stub files exist and contain valid Python syntax.
