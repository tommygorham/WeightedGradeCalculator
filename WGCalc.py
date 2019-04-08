##author: Tommy Gorham
##date: 4/8/2019

# README #
# This is a python script I wrote to quickly calculate my current weighted grade for my cpsc classes that don't
# show me my weighted grade online. I wrote this becasue I couldn't find one on git to do this for me.
# All three have been tested and accurately calculate the weighted grade for each class.

#  To use this for yourself, change the if statement string checks to check for your class name
# that is input from the user (you) in the main method. Then, make the same changes to the string checks
# in the process() function within the class universityClass. In that same function, change the weights
# to match your syllabus

# Potential Updates #
# option to continue calculating other classes without automatically terminating when finished
# exception handling for bad user input
# function to write the weighted grade to a txt file
# gui

class universityClass:
    # constructor to set the name of the universityClass we are calculating the weighted grade for
    def __init__(self, name):
        self.name = name

    # "get" methods to get grades from user and calculate & store the averages
    def getTests(self):
        count = 0
        total = 0
        print("Enter your test grades, then enter -1 when finished: ")
        userIn = eval(input())
        while userIn != -1:
            count += 1
            total += userIn
            userIn = eval(input())
        self.tAvg = total / count
        #return self.tAvg

    def getQuizzes(self):
        count = 0
        total = 0
        print("Enter your quiz grades, then enter -1 when finished: ")
        userIn = eval(input())
        while userIn != -1:
            count += 1
            total += userIn
            userIn = eval(input())
        self.qAvg = total / count
        return self.qAvg

    def getAssignments(self):
        count = 0
        total = 0
        print("Enter your assignment grades, then enter -1 when finished: ")
        userIn = eval(input())
        while userIn != -1:
            count += 1
            total += userIn
            userIn = eval(input())
        self.aAvg = total / count
        return self.aAvg

    def getLabs(self):
        count = 0
        total = 0
        print("Enter your lab grades, then enter -1 when finished: ")
        userIn = eval(input())
        while userIn != -1:
            count += 1
            total += userIn
            userIn = eval(input())
        self.lAvg = total / count
        return self.lAvg

    def getDiscussionPosts(self):
        count = 0
        total = 0
        print("Enter your discussion post grades, then enter -1 when finished: ")
        userIn = eval(input())
        while userIn != -1:
            count += 1
            total += userIn
            userIn = eval(input())
        self.dAvg = total / count
        return self.dAvg

    # method to process the weighted grade based on the class syllabus
    def process(self):
        if self.name == "algorithm analysis":
            accT = self.tAvg * .65 # tests are 65%  of the total grade based on syllabus
            accA = self.aAvg * .35 # assignments are 35% based on syllabus
            self.numGrade = accT + accA # stores numGrade as the weighted grade
        # same idea for the elif statements
        elif self.name == "operating systems":
            accT = self.tAvg * .7
            accA = self.aAvg * .2
            accD = self.dAvg * .1
            self.numGrade = accT+accA+accD
        elif self.name == "digital logic":
            accT = self.tAvg *.5
            accA = self.aAvg *.15
            accQ = self.qAvg *.1
            accL = self.lAvg *.25
            self.numGrade = accT+accA+accQ+accL
        # display the weighted grade to the user, formatted to the hundreths place and based on the class
        print("Based on the class syllabus, your weighted average is currently {:.2f}".format(self.numGrade) + " points")
        print("in "+self.name.title()) # formatting

def main():
    # get the name of the class we are going to calculate the weighted grade for
    class_name = input("What is the name of the class you would like to see you accumulated weighted grade for? ")
    # sets the name of the class to all lowercase for easy string checking
    class_to_calc = class_name.lower()
    # check string to know which class we are calculating
    if "algorithm analysis" in class_to_calc:
        # creates an instance of a universityClass and passes it the name of the class to calculate
        algorithms_grade = universityClass(class_to_calc)
        # get the test grades from the user
        algorithms_grade.getTests()
        # get the assignment grades from the user
        algorithms_grade.getAssignments()
        # process the weighted grade based on the syllabus
        algorithms_grade.process()
    # same idea for other classes. calls needed functions based on syllabus
    elif "operating systems" in class_to_calc:
        os_grade = universityClass(class_to_calc)
        os_grade.getTests()
        os_grade.getAssignments()
        os_grade.getDiscussionPosts()
        os_grade.process()
    elif "digital logic" in class_to_calc:
        dl_grade = universityClass(class_to_calc)
        dl_grade.getTests()
        dl_grade.getAssignments()
        dl_grade.getQuizzes()
        dl_grade.getLabs()
        dl_grade.process()
main()

