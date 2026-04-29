class Candidate:

    def __init__(self, candidate_id, candidate_name, question_marks):

        self.candidate_id = candidate_id
        self.candidate_name = candidate_name
        self.question_marks = question_marks
        self.result = True

    def findSelect(self):
        total = sum(self.question_marks)
        if(total < 7.5):
            self.result = False
        else:
            self.result = True
        
        return self.result


    
        