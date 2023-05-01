# # Health_Management_System
# 3 clients: Harry, Rohan, Hammad
# Create 3 files for food and other 3 for exercise
# Write 2 functions:
#  function 1 to take input for name and input of (diet or exercise
#  function 2 to retrieve files or access data

def getdate():
    import datetime
    return datetime.datetime.now()
date = str(getdate())

def datta():
    """ This function enter diet and exercise data for clients"""
    while (True):
        what = input("What to do: log or retrieve?\nor Write 'close' to end the program\n")
        if what == 'log':
            while (True):
                name = input("Enter the client's name: \nor Write Back to go back\n")
                if name == 'Harry':
                    while (True):
                        what2 = input("What to include: Diet or Exercise?\nor Write Back to go back.\n")
                        if what2 == 'Diet':
                            print("Enter diet")
                            diet = input()
                            with open("Harry_diet.txt", "a") as F:
                                F.write("[" + date + "] " + diet + ",")
                            break
                        elif what2 == 'Exercise':
                            print("Enter exercise")
                            exercise = input()
                            with open("Harry_exercise.txt", "a") as F:
                                F.write("[" + date + "] " + exercise + ",")
                            break
                        elif what2 == 'Back':
                            break
                        else:
                            print("Error! Feature does not exist")

                elif name == 'Rohan':
                    while (True):
                        what2 = input("What to include: Diet or Exercise?\nWrite Back to go back.\n")
                        if what2 == 'Diet':
                            print("Enter diet")
                            diet = input()
                            with open("Rohan_diet.txt", "a") as F:
                                F.write("[" + date + "] " + diet + ",")
                            break
                        elif what2 == 'Exercise':
                            print("Enter exercise")
                            exercise = input()
                            with open("Rohan_exercise.txt", "a") as F:
                                F.write("[" + date + "] " + exercise + ",")
                            break
                        elif what2 == 'Back':
                            break
                        else:
                            print("Error: Feature does not exist")

                elif name == 'Hammad':
                    while (True):
                        what2 = input("What to include: Diet or Exercise?\nWrite Back to go back.\n")
                        if what2 == 'Diet':
                            print("Enter diet")
                            diet = input()
                            with open("Hammad_diet.txt", "a") as F:
                                F.write("[" + date + "] " + diet + ",")
                            break
                        elif what2 == 'Exercise':
                            print("Enter exercise")
                            exercise = input()
                            with open("Hammad_exercise.txt", "a") as F:
                                F.write("[" + date + "] " + exercise + ",")
                            break
                        elif what2 == 'Back':
                            break
                        else:
                            print("Error! Feature does not exist")

                elif name == 'Back':
                    break

                else:
                    print("Error! Client Does not Exist")

        elif what == 'retrieve':
            while (True):
                name = input("Enter the client's name: \nor Write Back to go back\n")
                if name == 'Harry':
                    while (True):
                        what2 = input("What to retrieve: Diet or Exercise?\nWrite Back to go back.\n")
                        if what2 == 'Diet':
                            with open("Harry_diet.txt", "a") as F:
                                print(F.readlines())
                            break
                        elif what2 == 'Exercise':
                            with open("Harry_exercise.txt", "a") as F:
                                print(F.readlines())
                            break
                        elif what2 == 'Back':
                            break
                        else:
                            print("Error! Feature does not exist")

                elif name == 'Rohan':
                    while (True):
                        what2 = input("What to retrieve: Diet or Exercise?\nWrite Back to go back.\n")
                        if what2 == 'Diet':
                            with open("Rohan_diet.txt", "a") as F:
                                print(F.readlines())
                            break
                        elif what2 == 'Exercise':
                            with open("Rohan_exercise.txt", "a") as F:
                                print(F.readlines())
                            break
                        elif what2 == 'Back':
                            break
                        else:
                            print("Error! Feature does not exist")

                elif name == 'Hammad':
                    while (True):
                        what2 = input("What to retrieve: Diet or Exercise?\nWrite Back to go back.\n")
                        if what2 == 'Diet':
                            with open("Hammad_diet.txt", "a") as F:
                                print(F.readlines())
                            break
                        elif what2 == 'Exercise':
                            with open("Hammad_exercise.txt", "a") as F:
                                print(F.readlines())
                            break
                        elif what2 == 'Back':
                            break
                        else:
                            print("Error! Feature does not exist")

                elif name == 'close':
                    break

                else:
                    print("Error! Client Does not Exist")

        elif what == 'close':
            break

        else:
            print("Error! Client Does not Exist")
datta()








