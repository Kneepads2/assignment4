
import json
import time


data = {}
#filewrite = open("resourceData.json","w")
#filewrite.write("ID\t\tName\t\tOccupation\t\tSalary\t\tAge\t\tEmployment Status\t\t\n")
fileread = open("resourceData.json","r")
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
                salary = int(input("Enter the salary of the employee: "))
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
                    workstatus = "Full-time\n"
                    break
                elif (workstatus.upper() == "PARTTIMER" or workstatus.upper() == "PART-TIMER" or workstatus.upper() == "PART"):
                    workstatus = "Part-time\n"
                    break
                elif (workstatus.upper() == "CONTRACTOR"):
                    workstatus = "Contractor\n"
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter if they are a full-time, part-time or a contractor.\n")
        id = 0
        global data
        data = {'employee':{'name':name,'occupation':occupation,'salary':salary,'age':age,'workstatus':workstatus,'id':id}}
        
        with open ('resourceData.json','a') as f:
            json.dump(data,f,indent = 2)
            
            
        print("\nResource created. Sending you back to the main menu...\n======================================================")
        time.sleep(2)
        
class Read():
    def __init__(self):
        self.a=0
    def readResource(self):
        time.sleep(2)
        print("\n=================================\nPrinting employee data...\n") #i have to create first everytime
        f = open('resourceData.json')
        data2 = json.load(f)
        
        for resource in data2:
            data2["employee"]["id"] = self.a    
            print("\nID: "+str(data2["employee"]["id"]))
            print("\nName: "+str(data2["employee"]["name"]))
            print("\nOccupation: "+str(data2["employee"]["occupation"]))
            print("\nSalary: "+str(data2["employee"]["salary"]))
            print("\nAge: "+str(data2["employee"]["age"]))
            print("\nEmployment status: "+str(data2["employee"]["workstatus"]))
            print("======================================================")
            time.sleep(0.3)
            self.a += 1
        time.sleep(5) #16.3 exam study laws of recursion
        self.a = 0
        f.close()
    
class Delete:
    def __init__(self):
        pass 
    def deleteResource(self):
        employeeCode = int(input("Enter ID code of the employee: "))
        while fileread.readline():
            items = fileread.split()
            if (items[0] == employeeCode):
                del items[0]
                del items[1]
                del items[2]
                del items[3]
                del items[4]
            else:
                fileread = fileread.readline()
        


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
