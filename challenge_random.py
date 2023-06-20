
import random
def lvl_input():
    while True:
        level = input("Enter Level 1, 2, 3: \n")
        if level == "1" or level == "2" or level == "3":
            level = int(level)
            break
        else:
            print("ERROR, ENTER A NUMBER FROM 1 TO 3 FOR THE LEVEL \n")
            continue

    return level

def get_difficulty(level):
    
    if level == 1:
        maxNum = 9
        minNum = 0
    elif level == 2:
        maxNum = 99
        minNum = 10
    elif level == 3: 
        maxNum = 999
        minNum = 100

    return maxNum, minNum

def numOfQuestions(maxNum, minNum):
    while True:
        numOfQs = int(input("Enter the number of questions to ask (between 3 and 10): \n "))
        if numOfQs == 3 or numOfQs == 4 or numOfQs == 5 or numOfQs == 6 or numOfQs == 7 or numOfQs == 8 or numOfQs == 9 or numOfQs == 10:
            break
        else:
            continue
    return numOfQs

def questions(maxNum, minNum, numOfQs):
    count = 0
    while count <= numOfQs:
        a = random.randint(minNum,maxNum)
        b = random.randint(minNum,maxNum)
        answer = int(input(f"{a} + {b} = "))
        correctAnswer = (a + b)
        if answer == (a + b):
            print("CORRECT!!! \n")
        else:
            cnt = 1
            print("WRONG!!!")
            while cnt  <= 2:
                answer = int(input(f"{a} + {b} = "))
                if answer == (a + b):
                    print("CORRECT!!! \n")
                    quit()
                else:
                    cnt += 1
                    print("WRONG!!!")
                    continue
            print(f"CORRECT ANSWER = {correctAnswer}")
        count += 1



def main():

    level = lvl_input()

    maxNum, minNum = get_difficulty(level)
    numOfQs = numOfQuestions(maxNum,minNum)
    questions(maxNum,minNum, numOfQs)

main()