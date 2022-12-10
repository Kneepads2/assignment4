
import time
import csv
import random


#filewrite = open("resourceData.json","w")
#filewrite.write("ID\t\tName\t\tOccupation\t\tSalary\t\tAge\t\tEmployment Status\t\t\n")
#filewrite.close()

class Create: #the Create class, user enters their input to form a resource, which in this case is an employee
    name=""
    age=0
    salary=0
    workstatus=""
    occupation =""
    def __init__(self):
        pass
    def createEmployee(self):
        
        print("\n============================================\nEMPLOYEE DETAILS")
        time.sleep(2)
        
        name = str(input("\nEnter the full name of the employee: "))

        occupation = str(input("Enter the occupation of the employee: "))
        while True:
            try:
                salary = int(input("Enter the yearly salary of the employee: "))
                if (salary < 0):
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Please enter a valid salary.")

        while True:
            try:
                age = int(input("Enter the age of the employee: "))
                if (age < 0): #cannot have a negative age
                    raise ValueError
                elif(age < 14): #illegal i think. Would do an elif for like >130 because its almost impossible to live that long but maybe someone can
                    print("It is illegal to employ someone of that age.")
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Please enter a valid age.")
        while True:
            try:
                #didnt know what category this would be called so just called it work status
                workstatus = str(input("Is the employee a part-timer, full-timer, or a contractor? "))
                if (workstatus.upper() == "FULLTIMER" or workstatus.upper() == "FULL" or workstatus.upper() == "FULL-TIMER"):
                    workstatus = "Full-time"
                    break
                elif (workstatus.upper() == "PARTTIMER" or workstatus.upper() == "PART-TIMER" or workstatus.upper() == "PART"):
                    workstatus = "Part-time"
                    break
                elif (workstatus.upper() == "CONTRACTOR" or workstatus.upper() == "CON" or workstatus.upper() == "CONTRACT"):
                    workstatus = "Contractor"
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter if they are a full-time, part-time or a contractor.\n")
        id = random.randint(1,100000)#creates a unique id number for the employee. Yes theres a chance employees might get the same number but the range is so big its unlikely
        #if people do end up with the same id number, then when they go to Read or Delete, they'll print/delete the first one they find.
        print("This employee's ID number shall be: "+str(id))
        global data
        data = [name,occupation,salary,age,workstatus,id]
        
        with open ('resourceData.csv','w',newline='') as f:
            header = ['name','occupation','salary','age','work status','id']#created a header because every I go I see everyone makes a header row for some reason
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerow(data)# it is not possible for me to get the data to persist. 
            f.close()#Every time I go to create something, it overwrites the file so data can never truly persist
            
            
            
        print("\nResource created. Sending you back to the main menu...\n======================================================")
        time.sleep(2)
        
class Read(): # the Read class
    def __init__(self):
        self.a=0
        self.b=0
    def readResource(self):
        time.sleep(2)
        g = open('resourceData.csv')
        
        while True:
            try:
                reading = int(input("\nWhich employee are you searching for? Enter their ID number: "))
                break
            except ValueError:
                print("Please enter a valid ID number.")
        
        with open('resourceData.csv','r') as f:
            #fieldnames2 = ['name','occupation','salary','age','workstatus','id']
            csv_reader = csv.reader(f,delimiter=',')
            next(csv_reader)
            for resource in csv_reader:
                
                if ((f"{resource[5]}") == str(reading)):
                    print("======================================================\n")
                    print(f"Employee name: {resource[0]}")
                    print(f"Employee occupation: {resource[1]}")
                    print(f"Employee yearly salary: {resource[2]} CAD")
                    print(f"Employee age: {resource[3]}")
                    print(f"Employee work status: {resource[4]}")
                    print(f"Employee ID number: {resource[5]}")
                    self.a +=1
                    print("\n======================================================\nReturning to main menu..")
                else:
                    print("...")
                    #if (f"{resource[5]}" != searchUp):
                        #print("Cannot find employee.") 
                    self.a +=1
                    
                time.sleep(0.25)

        time.sleep(3) #16.3 exam study laws of recursion
        self.a = 0
        f.close()

class Update: #the Update class
    def __init__(self):
        pass
    def updateResource(self):
        
        while True:
            try:
                updating = int(input("Which employee do you want to update? Enter their ID number: "))
                break
            except ValueError:
                print("Please enter a valid ID number.")
        
        with open('resourceData.csv','w') as k:
            writer = csv.writer(k)
            for row in writer:
                    try: # could not get it to work
                        if (row[5] == updating):
                            updating2 = int(input("Which part of the employee are you updating? Their name, occupation, salary, age, or work status?"))

                            if (updating2.upper() == "NAME"):
                                updating3 = str(input("What is their new name? "))
                                row[0] = updating3
                                break

                            elif (updating2.upper() == "OCCUPATION"):
                                updating3 = str(input("What is their new occupation? "))
                                row[1] = updating3
                                break

                            elif (updating2.upper() == "SALARY"):
                                updating3 = str(input("What is their new salary? "))
                                row[2] = updating3
                                break

                            elif (updating2.upper() == "AGE"):
                                updating3 = str(input("What is their new age? "))
                                row[3] = updating3
                                break

                            elif (updating2.upper() == "WORKSTATUS" or updating2.upper() == "WORK STATUS"):
                                updating3 = str(input("What is their new salary? "))
                                row[4] = updating3
                                break
                            
                            elif (updating2.upper() == "ID"):
                                print("Cannot change ID number.")

                            else:
                                raise ValueError
                        else:
                            raise ValueError

                    except ValueError:
                        print("Not possible.")
                
    
class Delete:# the Delete class
    def __init__(self):
        pass 
    def deleteResource(self):
        
        while True:
            try:
                deleting = int(input("Which employee do you wish to delete? Enter their ID number: "))
                break
            except ValueError:
                print("Please enter a valid ID number.")

        with open('resourceData.csv', 'r') as inp, open('resourceData.csv', 'w') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                if (row[5] == deleting):
                    writer.writerow(row) #so it does actually delete the row, but deletes eveything and also doesnt print the big line below so I guess it does its job?
                else:
                    print(".....")
                    
        print("\nEmployee data deleted..............\nReturning to main menu....\n====================================================================================\n")
        time.sleep(2)
        


class Resource(Create,Read,Delete):
    
    def __init__(self):
        self.read = Read()
        self.delete = Delete()
        self.update = Update()
        self.create = Create()
        
    
    def CRUDmenu(self): #this is basically reused code from assignment 2 and 3. Nothing really speical here
        
        print("======================================================\n\nWelcome to Dylan's Employee CRUD application!!\n\n======================================================\n")
        time.sleep(2)
        print("\nHere, you can create a list of your employees and their information such as their name, occupation, salary, age, and employment status.\nTo create a resource, type 'CREATE'\nTo read a resource, type 'READ'\nTo update a resource, type 'UPDATE'\nTo delete a resource, type 'DELETE'\nTo exit this menu, type 'EXIT'")
        
        while True:
            try:
                menuInput = str(input("\nWhat do you want to do?  "))

                if (menuInput.upper() == "CREATE"):
                    self.create.createEmployee()
                    self.CRUDmenu()
                    break

                elif (menuInput.upper() == "READ"):
                    self.read.readResource()
                    self.CRUDmenu()
                    break

                elif (menuInput.upper() == "UPDATE"):
                    self.update.updateResource()
                    self.CRUDmenu()
                    break

                elif (menuInput.upper() == "DELETE"):
                    self.delete.deleteResource()
                    self.CRUDmenu()
                    break

                elif (menuInput.upper() == "EXIT"):
                    print("Exiting menu........\n\n=================================")
                    quit()
                else:
                    raise Exception
            
            except Exception:
                print("\nThat is not possible.")     
          

print(Resource().CRUDmenu())#run
