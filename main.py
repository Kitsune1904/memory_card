# ---------- Question class ----------
class Question():
    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_ans1
        self.wrong_answer2 = wrong_ans2
        self.wrong_answer3 = wrong_ans3
        self.count_asked = 0
        self.count_right = 0


    def got_right(self):
        self.count_asked += 1
        self.count_right += 1


    def got_wrong(self):
        self.count_asked += 1

        
# ---------- Questions ----------
questions = [
    Question('Як перекладається 🍎Яблуко🍎 на англійську?', 'apple', 'application', 'pineapple', 'apply'),
    Question('Як перекладається 🏠Дім🏠 на англійську?', 'house', 'horse', 'hurry', 'hour'),
    Question('Як перекладається 🐭Миша🐭 на англійську?', 'mouse', 'mouth', 'muse', 'museum'),
    Question('Як перекладається 💯Число💯 на англійську?', 'number', 'digit', 'amount', 'summary')
]
