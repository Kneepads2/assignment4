
import time
import csv
import random

data = {}
#filewrite = open("resourceData.json","w")
#filewrite.write("ID\t\tName\t\tOccupation\t\tSalary\t\tAge\t\tEmployment Status\t\t\n")
#filewrite.close()

counter = 0
class Create:
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
                if (age < 0):
                    raise ValueError
                elif(age < 14):
                    print("It is illegal to employ someone of that age.")
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Please enter a valid age.")
        while True:
            try:
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
        id = random.randint(1,100000)#creates a unique id number
        global data
        data = [name,occupation,salary,age,workstatus,id]
        
        with open ('resourceData.csv','w',newline='') as f:
            header = ['name','occupation','salary','age','work status']
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerow(data)
            f.close()
            
            
            
        print("\nResource created. Sending you back to the main menu...\n======================================================")
        time.sleep(2)
        
class Read():
    def __init__(self):
        self.a=0
        self.b=0
    def readResource(self):
        time.sleep(2)
        print("\n=================================\nPrinting employee data...\n") #i have to create first everytime
        f = open('resourceData.csv')
        
        while True:
            try:
                searchUp = int(input("Which employee are you searching for? Enter their ID number: "))
                break
            except ValueError:
                print("Please enter a valid ID number.")
        
        with open('resourceData.csv','r') as f:
            #fieldnames2 = ['name','occupation','salary','age','workstatus','id']
            csv_reader = csv.reader(f,delimiter=',')
            next(csv_reader)
            for resource in csv_reader:
                
                if ((f"{resource[5]}") == str(searchUp)):
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
    
class Delete:
    def __init__(self):
        pass 
    def deleteResource(self):
        pass
        


class Resource(Create,Read,Delete):
    
    def __init__(self):
        self.read = Read()
        self.delete = Delete()
        self.create = Create()
        
    
    def CRUDmenu(self):
        
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
                    print("c")
                    break

                elif (menuInput.upper() == "DELETE"):
                    self.delete.deleteResource()
                    break

                elif (menuInput.upper() == "EXIT"):
                    print("Exiting menu........\n\n=================================")
                    quit()
                else:
                    raise Exception
            
            except Exception:
                print("Not an option.")     
          

print(Resource().CRUDmenu())
