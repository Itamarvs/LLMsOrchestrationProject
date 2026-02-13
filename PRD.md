# Product Requirements Document (PRD) - League of AI Agents

## 1. Executive Summary
The goal of this project is to develop two robust, intelligent AI agents—a **Referee** and a **Player**—to participate in the "League of AI Agents" course competition. These agents will autonomously manage and play a "20 Questions" style game (Q21) against other students' agents, orchestrated via a central League Manager (LGM) using email-based communication. 

Our core responsibility is to implement the "Brain" of these agents: the decision-making logic powered by LLMs that drives the game interactions (generating questions, answering, guessing, and scoring).

## 2. System Architecture
The system consists of three main entities:
1.  **League Manager (LGM)**: The central authority (`beit.halevi.100@gmail.com`) that schedules seasons, rounds, and games.
2.  **Referee Agent**: Managed by us. Responsible for hosting games, selecting the target (Book/Association Word), answering questions, and scoring.
3.  **Player Agent**: Managed by us. Responsible for asking strategic questions and deducing the target to score points.

### Communication
-   **Protocol**: JSON over Email (Gmail API).
-   **Structure**: The agents use a provided SDK (wrapper) that handles the transport layer. We interface with this SDK via specific callback methods.

## 3. Detailed Specifications

### 3.1 The Game: Q21 (Questions 21)
A variation of "20 Questions" focused on literature.
-   **Objective**: The Player must guess the **Opening Sentence** of a specific book and a hidden **Associative Word** related to it.
-   **Inputs**: The Referee provides the **Book Name** (Concept) and a **Hint**.
-   **Process**:
    1.  Player asks a batch of **20 Yes/No/Partially/Unknown questions**.
    2.  Referee answers all 20 questions.
    3.  Player submits a final guess.
    4.  Referee scores the guess.

### 3.2 Referee Agent Requirements
We must implement the `RefereeAI` class with 4 mandatory callbacks:

| Callback Method | Responsibility | Input/Context | Output |
| :--- | :--- | :--- | :--- |
| `get_warmup_question(ctx)` | Verify connection/liveness. | `ctx` | `{"warmup_question": "str"}` |
| `get_round_start_info(ctx)` | Select the game target. | `ctx` | `{"book_name": "str", "book_hint": "str", "association_word": "str"}` |
| `get_answers(ctx)` | Answer the player's 20 questions. | `ctx` (contains questions) | `{"answers": [{"question_number": int, "answer": "A/B/C/D"}]}` |
| `get_score_feedback(ctx)` | Grade the player's performance. | `ctx` (contains guess) | `{"league_points": int, "private_score": float, ...}` |

**Answer Key**:
-   **A**: Yes
-   **B**: No
-   **C**: Partially
-   **D**: Unknown / Not Relevant

### 3.3 Player Agent Requirements
We must implement the `PlayerAI` class with 4 mandatory callbacks:

| Callback Method | Responsibility | Input/Context | Output |
| :--- | :--- | :--- | :--- |
| `get_warmup_answer(ctx)` | Answer the warmup question. | `ctx` (contains question) | `{"answer": "str"}` |
| `get_questions(ctx)` | Generate **exactly 20** strategic questions. | `book_name`, `hint`, `assoc_word` | `{"questions": [{"question_text": "str", "options": {"A":..., "B":..., "C":..., "D":...}}]}` |
| `get_guess(ctx)` | Deduce the targets. | `answers` | `{"opening_sentence": "str", "associative_word": "str", ...}` |
| `on_score_received(ctx)` | Handle score notification. | `league_points`, `match_id` | `None` |

**Constraints**:
-   **Justification Length**: `sentence_justification` and `word_justification` must be **35+ words**.
-   **Question Count**: Must return exactly 20 questions.

### 3.4 Technical Constraints & Setup
-   **Language**: Python 3.11.
-   **Authentication**: Google OAuth 2.0 (Gmail API).
-   **Credentials**: `client_secret.json` and `token.json` (Must strictly be ignored directly by git).
-   **Secrets Management**: Environment variables or local `.env` files.
-   **SDKs**: `Q21G-player-whl` and `Q21G-referee-whl` (install via `.whl`).
-   **Run Modes**:
    -   `--scan`: Process messages once.
    -   `--watch`: Continuous polling.
    -   `--test-connectivity`: Verify setup.

## 4. Implementation Strategy
-   **LLM Integration**: Use advanced LLMs (Gemini/GPT-4) to drive the logic.
    -   *Player Strategy*: Chain-of-thought prompting to formulate questions that binary search the solution space.
    -   *Referee Strategy*: RAG or Knowledge interactions to verify book details and provide accurate answers/scores.
-   **Robustness**: Error handling for API failures and malformed JSON.
-   **Testing**: Use the provided `Active Demo Mode` and `Single-Game Mode` to verify agents against themselves or mock counterparts.

## 5. Success Metrics
-   **Operational Stability**: Agents complete 100% of scheduled games without crashing.
-   **Protocol Compliance**: 100% adherence to JSON schemas.
-   **Game Performance**:
    -   Information Gain (Player): Questions significantly narrow down the search space.
    -   Accuracy (Referee): Answers are factually correct regarding the book.
    -   Fairness (Referee): Scoring is consistent and justified.

## 6. Next Steps
1.  Initialize the repository structure.
2.  Install SDKs and dependencies.
3.  Set up local testing environment (mocking the LGM).
4.  Implement the `RefereeAI` and `PlayerAI` logic iteratively.
