'''
Classes and Objects Example
'''

# Class declaration
# _ as a prefix determines private fields and constructors.


class Interviews:
    # @constructor
    def __init__(self, companyName, interviewLevel):
        self.companyName = companyName
        self.interviewLevel = interviewLevel

    # @method
    def interviewProcess(self):
        print(f"I have an Interview at {self.companyName} which is a {self.interviewLevel} Interview")


interview_one = Interviews('AWS', 'Phone Screen')
interview_one.interviewProcess()

interview_two = Interviews('ByteDance', 'Online Assessment')
interview_two.interviewProcess()
