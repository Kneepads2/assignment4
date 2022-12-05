
file = open("resourceData.txt","w")
file.write("ID code\t\tName\t\tOccupation\t\tSalary\t\tAge\t\tYear of Birth\t\tMarital Status\n")
file.close()
employeeData = []
counter = 000
class Create:
    
    def __init__(self):
        pass
    def createEmployee(self):
        employeeData[0] = str(input("Employee's name: "))
        employeeData[1] = str(input("Employee's occupation: "))
        employeeData[2] = str(input("Employee's salary: "))
        employeeData[3] = str(input("Employee's age: "))
        employeeData[4] = str(input("Employee's year of birth: "))
        self.createLine = (counter+"\t\t"+employeeData[0]+"\t\t"+employeeData[1]+"\t\t"+employeeData[2]+"\t\t"+employeeData[3]+"\t\t"+employeeData[4]+"\t\t")
        file.write(self.createLine + "\n")
        
        
    

class Delete:
    def __init__(self):
        pass 
    def deleteResource(self):
        pass



class Resource:
    
    def __init__(self):
        pass
    
    def CRUDmenu(self):
        
        print("=============================\n\nWelcome to Dylan's Employee CRUD application a!!\n\n=============================\n")
        print("\nHere, you can create a list of your employees and their information such as their name, occupation, salary, age, and birthday.\nTo create a resource, type 'CREATE'\nTo read a resource, type 'READ'\nTo update a resource, type 'UPDATE'\nTo delete a resource, type 'DELETE'\nTo exit this menu, type 'EXIT'")
        print(counter)
        while True:
            try:
                menuInput = str(input("\nWhat do you want to do?  "))
                if (menuInput.upper() == "CREATE"):
                    print("a")
                    break
                elif (menuInput.upper() == "READ"):
                    print("b")
                    break
                elif (menuInput.upper() == "UPDATE"):
                    print("c")
                    break
                elif (menuInput.upper() == "DELETE"):
                    print("d")
                    break
                elif (menuInput.upper() == "EXIT"):
                    print("Exiting menu........\n\n=================================")
                    quit()
                else:
                    raise Exception
            
            except Exception:
                print("Not an option.")     
          

print(Resource().CRUDmenu())