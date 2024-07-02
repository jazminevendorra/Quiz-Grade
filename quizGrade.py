# This program will automatically grade a quiz.
# This quiz has 15 multiple choice questions.
# The number of questions may be easily modified, as it is a global variable

NUM_QUESTIONS = 15

def main():
    # Answer key list
    answer_key = ['A','C','A','B','B','D','D','A','C','A','B','C','D','C','B']
    
    # Intro
    print("Quiz Grading App ...")

    tryAgain = 'y'
    
    while tryAgain == 'y':
        # Ask for name of student
        std_name = input(format("\nEnter name of student: ",'26'))

        # Read student records and save into student's list
        stdList = readStudents()
        

        # Display results
        print("\n",std_name, "Quiz Results")
        print("--------------------------------------------")

                  
        correct_count = correct_answer(answer_key, stdList)
        incorrect_count, incorrect_index_list = incorrect_answer(answer_key, stdList)

        
        print("Correct Answers:", format(correct_count, '5'))
        print("Incorrect Answers: ", format(incorrect_count,'2'), incorrect_index_list)
        

        # Pass or Fail
        if correct_count >= 11:
            print ("\nStudent PASSED the quiz.")
        else:
            print ("\nStudent FAILED the quiz.")
        
        tryAgain = input("\nDo you have another student (y/n)?\n")




def readStudents():     # Read student file
    # Initialize student's list
    student_answers = []

    #Prompt user for file
    filename = input(format("Enter quiz answers file: ",'25'))

    try:
        #Open file
        inFile = open(filename, 'r')
        
        #Read student record into student answers list
        answer = inFile.readline().rstrip('\n')
        

        while answer != "":
            # Read student answers
            student_answers.append(answer) 

            #read next student's answer
            answer = inFile.readline().rstrip('\n')
            
        # Close File
        inFile.close()

    except:     # Exception handling
        print("Error ... could not process", filename)
        tryAgain = input("\nDo you have another student (y/n)?\n")
        
    # Return value   
    return student_answers


def correct_answer(key, std_answer):    # Determine correct answers
    # initialize correct counter
    correct_count = 0
   
    for num in range(len(key)):
        if(key[num] == std_answer[num]):
            correct_count = correct_count + 1
    # return values  
    return correct_count

def incorrect_answer(key, std_answer):  # Determine incorrect answers
    # initialize incorrect counter
    incorrect_count = 0

    # create list of incorrect index
    incorrect_index_list = []

    for value in range(len(key)):
        if(key[value] != std_answer[value]):
            incorrect_count = incorrect_count + 1
            incorrect_index_list.append(value)

    # return values     
    return incorrect_count, incorrect_index_list
main()   
    

        
              
