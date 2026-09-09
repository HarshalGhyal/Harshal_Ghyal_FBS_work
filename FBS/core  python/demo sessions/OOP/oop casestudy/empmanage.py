from hr import Hr
from dev import Dev
class EmpManage:
    def __init__(self):
        self.addEmpDetails={}
    def addEmp(self):
        empid=int(input("Enter id of Emp:"))
        if empid in self.addEmpDetails:
            print("Emp Already Exist")
            return
        else:
            name =input("Enter name of Emp:")
            sal = int(input("Enter salary of Emp:"))
            print("1 Hr")
            print("2 Dev")
            ch = int(input("Enter your choice:"))
            if ch == 1:
                comm =float(input("Enter the commission of Hr:"))
                emp =Hr(empid,name,sal,comm)
            elif ch == 2:
                bonus =float(input("Enter the bonus of Deveploper:"))
                emp = Dev(empid,name,sal,bonus)
            else:
                print("Invalid choice......")
                return
            self.addEmpDetails[empid] =emp
            print("Emp added sucessfully...")

    def displayEmp(self):
       if len(self.addEmpDetails)==0:
           print('Employee not exist')
       else:
           for emp,empobj in self.addEmpDetails.items():
               print(emp,empobj)   
    def searchEmp(self):
        if len(self.addEmpDetails)==0:
            print('Employee not exists')
        else:
            eid=int(input('Enter the id of employee:'))
            if eid in self.addEmpDetails:
                print('Employeedetail=',self.addEmpDetails[eid])
            else:
                print(f'Employee with {eid} is not present')        
    def updateEmp(self):
        
        eid = int(input("Enter employee id: "))

        if eid in self.addEmpDetails:
            emp = self.addEmpDetails[eid]
            emp.name = input("Enter new name: ")
            emp.sal = int(input("Enter new salary: "))
            print("Employee updated successfully")
        else:
            print("ID not found")
    def delEmp(self):
        id=int(input('Enter the id of employee:'))
        if id in self.addEmpDetails:
                del self.addEmpDetails[id]
                return 'Employee delete successfully.'
        else:
                return 'ID not found.'
    def ExistEmp(self):
        print("Logout sucessfully")