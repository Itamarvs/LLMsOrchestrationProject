"""
My Q21 Referee Implementation.
"""

from q21_referee import RefereeAI

class MyRefereeAI(RefereeAI):
    def get_warmup_question(self, ctx: dict) -> dict:
        """Generate a warmup question."""
        return {"warmup_question": "What is 10 + 10?"}

    def get_round_start_info(self, ctx: dict) -> dict:
        """Provide book info for the round."""
        return {
            "book_name": "The Great Gatsby",
            "book_hint": "A novel about the American Dream in the 1920s.",
            "association_word": "green"
        }

    def get_answers(self, ctx: dict) -> dict:
        """Answer the player's 20 questions."""
        answers = []
        for q in ctx["dynamic"]["questions"]:
            answers.append({
                "question_number": q["question_number"],
                "answer": "D" # Default to Unknown
            })
        return {"answers": answers}

    def get_score_feedback(self, ctx: dict) -> dict:
        """Score the player's guess."""
        return {
            "league_points": 1,
            "private_score": 50.0,
            "breakdown": {
                "opening_sentence_score": 50.0,
                "sentence_justification_score": 50.0,
                "associative_word_score": 50.0,
                "word_justification_score": 50.0
            },
            "feedback": {
                "opening_sentence": "Fair attempt.",
                "associative_word": "Close."
            }
        }
