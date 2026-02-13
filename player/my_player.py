"""
My Q21 Player Implementation.
"""

from q21_player import PlayerAI

class MyPlayerAI(PlayerAI):
    def get_warmup_answer(self, ctx: dict) -> dict:
        """Answer the warmup math question."""
        question = ctx["dynamic"]["warmup_question"]
        # TODO: Implement logic
        return {"answer": "0"}

    def get_questions(self, ctx: dict) -> dict:
        """Generate 20 strategic questions."""
        book_name = ctx["dynamic"]["book_name"]
        
        questions = []
        for i in range(1, 21):
            questions.append({
                "question_number": i,
                "question_text": f"Is it related to {book_name}?",
                "options": {"A": "Yes", "B": "No", "C": "Partially", "D": "Unknown"}
            })
        return {"questions": questions}

    def get_guess(self, ctx: dict) -> dict:
        """Guess the opening sentence."""
        return {
            "opening_sentence": "Placeholder opening sentence.",
            "sentence_justification": "This is a placeholder justification that meets the thirty-five word minimum requirement to ensure compliance with the project rules. We will implement the actual logic using an LLM in the next steps.",
            "associative_word": "Placeholder",
            "word_justification": "This is a placeholder justification for the word that meets the thirty-five word minimum requirement to ensure compliance with the project rules. We will implement the actual logic using an LLM in the next steps.",
            "confidence": 0.5
        }

    def on_score_received(self, ctx: dict) -> None:
        """Handle score notification."""
        points = ctx["dynamic"].get("league_points", 0)
        print(f"Game complete! Points: {points}")
