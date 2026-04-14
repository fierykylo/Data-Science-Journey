class Candidate:
    def __init__(self, candidate_id, candidate_name, question_marks):
        self.candidate_id = candidate_id
        self.candidate_name = candidate_name
        self.question_marks = question_marks
        self.result = False  # default

    def findSelect(self):
        total_marks = sum(self.question_marks)
        max_marks = 5 * 3  # 5 questions, 3 marks each

        if total_marks < (max_marks / 2):
            self.result = False
        else:
            self.result = True

        return self.result


# Creating objects
c1 = Candidate(1, "Aarush", [3, 3, 0, 3, 0])
c2 = Candidate(2, "Rahul", [0, 0, 3, 0, 0])

# Checking results
print(c1.candidate_name, "SELECTED" if c1.findSelect() else "NOT SELECTED")
print(c2.candidate_name, "SELECTED" if c2.findSelect() else "NOT SELECTED")