from tkinter import *


class Quiz:
    def __init__(self, master):
        self.master = master
        self.score = 0
        self.questions = [
            "What is the capital of France?",
            "What is the largest ocean in the world?",
            "What is the tallest mountain in the world?",
            "What is a group of crows called?",
            "Compared to their body weight, what animal is the strongest - Dung Beetle, Elephant, Ant, or Cow?",
            "How many dots appear on a pair of dice?",
            "Which is the only body part that is fully grown from birth?",
            "What is acrophobia a fear of?",
            "In what country was Elon Musk born?",
            "Who performs the voice of Homer Simpson?",
            "What country has the most islands?",
            "In Australia what is commonly known as a Bottle-o?",
            "How many hearts does an octopus have?",
            "December 26th is known by what names in Ireland?",
            "In what US state is the country's busiest airport located?",
            "What planet is closest to the sun?",
            "Where is the strongest human muscle located?",
            "What phone company produced the 3310?"
        ]
        self.answers = [
            "Paris",
            "Pacific",
            "Mount Everest",
            "A murder",
            "Dung Beetle",
            "42",
            "Eyes",
            "Flying",
            "South Africa",
            "Dan Castellaneta",
            "Sweden - 270,000",
            "An off-license / Liquor Store",
            "3",
            "Saint Stephen's Day",
            "Atlanta, Georgia - Hartsfield–Jackson Atlanta International Airport",
            "Mercury",
            "Jaw",
            "Nokia"
        ]
        self.current_question = 0

        self.question_label = Label(
            master,
            text=self.questions[self.current_question],
            font=("Poppins", 20),
            wraplength=800,
            justify=CENTER
        )
        self.question_label.pack(pady=20)

        self.answer_entry = Entry(master, font=("Poppins", 16))
        self.answer_entry.pack(pady=10)

        self.submit_button = Button(
            master,
            text="Submit",
            font=("Poppins", 14),
            command=self.submit
        )
        self.submit_button.pack(pady=10)

        self.score_label = Label(
            master,
            text="Score: 0",
            font=("Poppins", 16)
        )
        self.score_label.pack(pady=10)

    def submit(self):
        user_answer = self.answer_entry.get()
        if user_answer.lower() == self.answers[self.current_question].lower():
            self.score += 1
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.question_label.config(
                text=self.questions[self.current_question]
            )
            self.answer_entry.delete(0, END)
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.question_label.config(
                text=f"Quiz completed. Final score: {self.score}"
            )
            self.answer_entry.pack_forget()
            self.submit_button.pack_forget()


root = Tk()
root.geometry("900x600")
root.title("Quiz App")
quiz = Quiz(root)
root.mainloop()
