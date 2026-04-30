# v0.2.16
# { "Depends": "py-genlayer:latest" }

from genlayer import *

class MiniQuest(gl.Contract):
    question: str
    score: u256
    feedback: str

    def __init__(self):
        self.question = "What is GenLayer?"
        self.score = 0
        self.feedback = "Quest started"

    @gl.public.view
    def get_state(self) -> str:
        return f"Question: {self.question} | Score: {self.score} | Feedback: {self.feedback}"

    @gl.public.write
    def answer(self, user_answer: str) -> None:
        if "ai" in user_answer.lower() or "blockchain" in user_answer.lower():
            self.score = 1
            self.feedback = "Good answer!"
        else:
            self.score = 0
            self.feedback = "Try again!"
