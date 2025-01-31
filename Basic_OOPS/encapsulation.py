import random
class Interview:
    def __init__(self, interview_type, interviewer, interviewee, interview_questions, interview_solutions):
        self.interview_type = interview_type
        self.interviewer = interviewer
        self.interviewee = interviewee
        self.__interview_questions = interview_questions
        self.__interview_solutions = interview_solutions
        
    def get_details(self):
        return f"This interview is conducted by {self.interviewer} and candidate is {self.interviewee}"
    
    def get_interview_questions(self, n):
        return random.choices(self.__interview_questions, k=n)

    def get_solution(self, question):
        return self.__interview_solutions[question - 1]

num1 = Interview("OA", "A", "B", [1,2,3,4,5,6],[7,8,9,10,11,12])
print(num1.interview_type)
#print(num1.__interview_questions) # error - because we are trying to access a private variable
print(num1.get_interview_questions(3))
print(num1.get_solution(2))
        
