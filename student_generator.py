import Student

'''
Function to return list of student objedcts
Input none

'''
#Create 2 instances of Student
def load_students():
    list_of_students = []

    try:
        #create a file handler
        file = open("students.csv", "r")

        #create variable to keep track of line in file that we are reading
        line_number = 0
        #read file line by line in for loop
        for line_of_data in file:
            line_number += 1
            #skip first line in csv file
            if line_number == 1:
                continue
            
            #split the line of data at the comma
            student_data = line_of_data.split(",")

            #handle errors in data format. line_of_data should have 6 items
            if len(student_data) != 6:
                raise Exception(f"There is an error in your data file on line {line_number}")
            
            #get student data and create a student object for each student
            first_name = student_data[0]
            last_name = student_data[1]
            major = student_data[2]
            credit_hours = int(student_data[3])
            gpa = float(student_data[4])
            student_id = student_data[5].strip()

            new_student = Student.Student(first_name, last_name, major, credit_hours, gpa, student_id)
            list_of_students.append(new_student)

    except Exception as err:
        print(err)


    for student in list_of_students:
        student.print_student_data()

    return list_of_students

load_students()

def student_to_dictionary(list_of_students):
    student_dictionary_list=[]

    #loop through student list
    for student in list_of_students:
        student_dictionary = {}
        student_dictionary['id'] = student.get_ID()
        student_dictionary['first_name'] = student.get_first_name()
        student_dictionary['last_name'] = student.get_last_name()
        student_dictionary['major'] = student.get_major()
        student_dictionary['gpa'] = student.get_gpa()
        student_dictionary['class'] = student.get_class_level()

        student_dictionary_list.append(student_dictionary)

    return student_dictionary_list
student_to_dictionary()
def get_student_dictionaries(load_students, student_to_dictionary):
    student_list = load_students()

    student_dictionaries = student_to_dictionary(student_list)

    return student_dictionaries

get_student_dictionaries