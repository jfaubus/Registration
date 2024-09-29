#Base Class
class Student:
    def __init__(self, name):
        self.name = name
        self.registrationDict = {}
        self.studentCompletedCourses = []
        self.studentEnrolledClasses = {}


#single inheritance
class Course(Student):
    def __init__(self, course, course2 = None):
        self.course = course
        self.course2 = course2


#multilevel
class Electives(Course):
    def __init__(self, courseInstance):
        self.courseInstance = courseInstance
        #Electives for Engineering/Science Majors
        self.electives = ["EECE1990", "EECE2140", "EECE2150", "EECE2413", "EECE2520", "EECE2530", "EECE2531", "EECE2540"]
        self.electiveTime = {"EECE1990": "11:15", "EECE2140": "11:15", "EECE2150": "2:50", "EECE2413": "2:50", "EECE2520" : "9:15", "EECE2530": "9:15", "EECE2531": "9:15", "EECE2540": "9:15"}
        self.electives = {"EECE1990": 4, "EECE2140": 4, "EECE2150": 4, "EECE2413": 4, "EECE2520": 4, "EECE2530": 4, "EECE2531": 4, "EECE2540": 4}  

        
    def checkElective(self):
        if self.courseInstance.course in self.electives:
            return True
        else:
            return False
        


#Hierarchical Inherticance in all of the different major classes below
class ChemicalEngineering(Student): 
    CHEME = []
    def __init__(self, student = None):
        
        self.student = student
    def ChemStudents(self):
        self.CHEME.append(self.student.name)
        return self.CHEME

    def GetRequired(self):
        return {"MATH1341": [], "CHEM1151": []}


    def GetCredits(self):
        return {"MATH1341": 4, "CHEM1151": 4}

class CivilAndEnvironmentalEngineering(Student): 
    CivEnvE = []
    def __init__(self, student = None):
        self.student = student
    def CivEnvEStudents(self):
        self.CivEnvE.append(self.student.name)
        return self.CivEnvE
    

    def GetRequired(self):
        return {"MATH1341": [], "PHYS1151": []}
    def GetCredits(self):
        return {"MATH1341": 4, "CHEM1151": 4}

class ElectricalandComputerEngineering(Student): 
    EECE = []
    def __init__(self, student = None):
        self.student = student
    def EECEStudents(self):
        self.EECE.append(self.student.name)
        return self.EECE
    
    #course with their prereq
    def GetRequired(self):
        return {"MATH1341": [], "MATH3081": ["MATH1342", "MATH1252", "MATH1242"], "EECE2140": [], "EECE2160": [], "EECE2150": []}
    def GetCredits(self):
        return {"MATH1341": 4, "MATH3081": 4}

class ComputerScience(Student): 
    CS = []
    def __init__(self, student = None):
        self.student = student
    def CSStudents(self):
        self.CS.append(self.student.name)
        return self.CS
    
    def GetRequired(self):
        return {"MATH1341": []}
    def GetCredits(self):
        return {"MATH1341": 4}

class ElectricalEngineering(Student):
    EE = []
    def __init__(self, student = None):
        self.student = student
    def EEStudents(self):
        self.EE.append(self.student.name)
        return self.EE

    def GetRequired(self):
        return {"MATH1341": []}
    def GetCredits(self):
        return {"MATH1341": 4}

class Physics(Student):
    phys = []
    def __init__(self, student = None):
        self.student = student
    def Phystudents(self):
        self.Phys.append(self.student.name)
        return self.Phys
    
    def GetRequired(self):
        return{"MATH1341": []}
    def GetCredits(self):
        return {"MATH1341": 4}

#Base Class
class DualMajor():
    def __init__(self, major1, major2):
        self.major1 = major1
        self.major2 = major2

            
#Multiple inheritance
class Specialization(Student, DualMajor):
        def __init__(self, specialization, minor = "no minor", StudentInstance=None, DualMajorInstance=None):
            self.specialization = specialization
            self.StudentInstance = StudentInstance
            self.DualMajorInstance = DualMajorInstance
            self.minor = minor
        def special(self):
             print(f"{self.StudentInstance.name} has dual major of {self.DualMajorInstance.major1} and {self.DualMajorInstance.major1} with a minor in {self.DualMajorInstance.major2}")
             return [self.StudentInstance.name, self.DualMajorInstance.major1, self.DualMajorInstance.major1, self.DualMajorInstance.major2]

#hybrid
class Registration(DualMajor, Electives, Course, Student):
        def __init__(self, StudentInstance, CourseInstance, majorClasses=None, majorCreds = None, DualInstance=None, ElectiveInstance=None):
             self.StudentInstance = StudentInstance
             self.CourseInstance = CourseInstance
             self.DualMajorInstance = DualInstance
             self.ElectiveInstance = ElectiveInstance
             self.majorClasses = majorClasses
             self.CheckingCredsDict = {}
             self.majorCreds = majorCreds
             
 
        def register(self):

           #  if self.RegisterCheckCredits(self.StudentInstance.studentEnrolledClasses) < 20:
                self.StudentInstance.registrationDict[self.CourseInstance.course] = self.StudentInstance.name
                print(self.StudentInstance.registrationDict)
                self.StudentInstance.studentEnrolledClasses[self.CourseInstance.course] = []
               # print(self.StudentInstance.studentEnrolledClasses)

        def registerDual(self):
            try:
                if self.CourseInstance.course in self.DualMajorInstance.major1 and self.CourseInstance.course in self.DualMajorInstance.major2:
               # if self.CourseInstance.course in self.StudentInstance.MandatoryCourses[self.StudentInstance.major] and self.CourseInstance.course in self.StudentInstance.MandatoryCourses[self.DualMajorInstance.major2]:
                    print("This class is offered for both majors.")
                    Registration.register(self)
                else:
                    print("This class is not offered for both majors.")
            except KeyError:
                print("This is not a major")


        def registerElective(self):
            Electives(self.CourseInstance)
            if self.ElectiveInstance.checkElective():
            #if self.CourseInstance.course in self.ElectiveInstance.electives: 
                print("This is an acceptable elective. ")
                self.StudentInstance.registrationDict[self.CourseInstance.course] = self.StudentInstance.name
                print(self.StudentInstance.registrationDict)
            else:
                print("Not an elective")

        def registerTime(self):
             if self.ElectiveInstance.electiveTime[self.CourseInstance.course] != self.ElectiveInstance.electiveTime[self.CourseInstance.course2]:
                  print("These classes are at different times. ")
                  self.StudentInstance.registrationDict[self.CourseInstance.course] = self.StudentInstance.name
                  self.StudentInstance.registrationDict[self.CourseInstance.course2] = self.StudentInstance.name
                  print(self.StudentInstance.registrationDict)
             else:
                  print("Error: these classes are at the same time.")

        def registerCheckPre(self):
            try:
                if self.StudentInstance.studentCompletedCourses in self.majorClasses[self.CourseInstance.course]:
                    self.StudentInstance.registrationDict[self.CourseInstance.course] = self.StudentInstance.name
                    print("You have the prereq for this class. ")
                    print(self.StudentInstance.registrationDict)
                else:
                    print("You do not have the prereq for this class. ")
            except KeyError:
                [print("This is not a course in our database. ")]


        def RegisterCheckCredits(self):
                for i in self.StudentInstance.studentEnrolledClasses:
                    if self.StudentInstance.name not in self.CheckingCredsDict.keys() and i in self.majorClasses:
                        self.CheckingCredsDict[self.StudentInstance.name] = 0
                    if i in self.majorClasses:
                            self.CheckingCredsDict[self.StudentInstance.name] += self.majorCreds[i]
                    if self.StudentInstance.name not in self.CheckingCredsDict.keys() and i in self.ElectiveInstance.electives:
                            self.CheckingCredsDict[self.StudentInstance.name] = 0
                    if i in self.ElectiveInstance.electives:
                            self.CheckingCredsDict[self.StudentInstance.name] += 4
                    
                    if self.CheckingCredsDict[self.StudentInstance.name] >= 20:
                        del self.StudentInstance.registrationDict[i]
                        print(f"This is a course overload, {self.CheckingCredsDict[self.StudentInstance.name]} is more than or equal to 20, can't add {i}")
                        print(self.StudentInstance.registrationDict)
                print(self.CheckingCredsDict)

        def ElectiveORRequired(self):
            if self.CourseInstance.course in self.majorClasses:
                    self.StudentInstance.studentEnrolledClasses[self.CourseInstance.course] = "Required"
            elif self.CourseInstance.course in self.ElectiveInstance.electives:
                    self.StudentInstance.studentEnrolledClasses[self.CourseInstance.course] = "Elective"
            print(self.StudentInstance.studentEnrolledClasses)


def main():

#Test Case One:
    print("Test Case One: ")
    CourseInstance = Course("PHYS1151")
    major = CivilAndEnvironmentalEngineering()
    ElectiveInstance = Electives(CourseInstance)
    StudentInstance = Student("Julia")
    RegistrationInstance = Registration(StudentInstance, CourseInstance, major, ElectiveInstance=ElectiveInstance)
    RegistrationInstance.register()
    print()

#Test Case Two:
    print("Test Case Two: ")
    major1 = ComputerScience()
    StudentInstance = Student("Ava")
    CourseInstance = Course("MATH1341")
    ElectiveInstance = Electives(CourseInstance)
    major2 = ElectricalEngineering()
    DualMajorInstance = DualMajor(major1.GetRequired() , major2.GetRequired())
    RegistrationInstance = Registration(StudentInstance, CourseInstance, DualInstance = DualMajorInstance, ElectiveInstance=ElectiveInstance)
    RegistrationInstance.registerDual()
    print()

#Test Case Three
    print("Test Case Three: ")
    CourseInstance = Course("EECE2520")
    ElectiveInstance = Electives(CourseInstance)
    major = ElectricalandComputerEngineering()
    StudentInstance = Student("Anna")
    RegistrationInstance = Registration(StudentInstance, CourseInstance, ElectiveInstance=ElectiveInstance)
    RegistrationInstance.registerElective()
    print()

#Test Case Four
    print("Test Case Four: ")
    StudentInstance = Student("Caroline")
    CourseInstance = Course("EECE1990", "EECE2140")
    ElectiveInstance = Electives(CourseInstance)
    RegistrationInstance = Registration(StudentInstance, CourseInstance, ElectiveInstance=ElectiveInstance)
    RegistrationInstance.registerTime()   
    print()

#Test Case Five
    print("Test Case Five: ")
    major = ElectricalandComputerEngineering()
    StudentInstance = Student("Adeline")
    CourseInstance = Course("MATH1342")
    RegistrationInstance = Registration(StudentInstance, CourseInstance, majorClasses=major.GetRequired(), ElectiveInstance=ElectiveInstance)
    RegistrationInstance.registerCheckPre()
    print()

#Test Case Six
    print("Test Case Six: ")
    major = ChemicalEngineering()
    StudentInstance = Student("Diya")
    list = ["EECE1990", "EECE2140", "CHEM1151", "MATH1341", "EECE2413", "MATH1341"]
    for i in list: 
        CourseInstance1 = Course(i)
        RegistrationInstance = Registration(StudentInstance, CourseInstance1, majorClasses=major.GetRequired(), majorCreds=major.GetCredits(), ElectiveInstance=ElectiveInstance)
        RegistrationInstance.register()
    RegistrationInstance.RegisterCheckCredits()

    print()

#Test Case Seven
    print("Test Case Seven: ")
    major = ElectricalandComputerEngineering()
    CourseInstance = Course("EECE2140")
    StudentInstance = Student("Dorian")  
    ElectiveInstance = Electives(CourseInstance)
    RegistrationInstance = Registration(StudentInstance, CourseInstance, majorClasses=major.GetRequired(), ElectiveInstance=ElectiveInstance)
    RegistrationInstance.register()
    RegistrationInstance.ElectiveORRequired()

    major = ChemicalEngineering()
    CourseInstance = Course("EECE2140")
    StudentInstance = Student("Dax")  
    ElectiveInstance = Electives(CourseInstance)
    RegistrationInstance = Registration(StudentInstance, CourseInstance, majorClasses=major.GetRequired(), ElectiveInstance=ElectiveInstance)
    RegistrationInstance.register()
    RegistrationInstance.ElectiveORRequired()

    print()

if __name__ == "__main__": 
    main()
