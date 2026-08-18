
def addemp():
    id=int(input('Enter ID :'))
    name=input('Enter Name:')
    sal=int(input('Enter salary:'))
    dept=input('Enter Department:')
    if(id not in all_emp_details):
        all_emp_details[id]=[id,name,sal,dept]
        return 'Employee added successfully...'
    else:
        return 'id already exists..'
def showallemp():
    return all_emp_details

def updemp(id):
    print('NOTE: If you dont want to change leave this field blank....')    
    emp=all_emp_details.get(id)
    if(emp):
        name=input(f'Enter new name({emp[1]}):') or emp[1]
        sal=int(input(f'Enter new salary({emp[2]}):')or 0) or emp[2]
        dept=input(f'Enter new department({emp[3]}):') or emp[3]
        emp=all_emp_details[id]=[id,name,sal,dept]
    else: 
        return 'ID not found..'
def delemp(id):
    
    if id in all_emp_details:
        del all_emp_details[id]
        return 'Employee delete successfully.'
    else:
        return 'ID not found.'
def searchemp(id):
    if id in all_emp_details:
        return 'given id exists..'
    else:
        return 'given id not exists...'
def empManage():
    print('###### Employee Manage ######')
    ch=0
    while(ch!='6'):
        print(''' Please select option from below...
        1.Add employee
        2.Show all employee
        3.Update employee
        4.Delete employee
        5.search employee
        6.Logout
        ''')
        ch=input("Enter Choice:")
        if(ch=='1'):
            res=addemp()
            print(res)
        elif(ch=='2'):
            res=showallemp() 
            print(res)
        elif(ch=='3'):
            print('Warning: ID not allowed to update...')
            id=int(input('Enter id:'))
            res=updemp(id)
            print(all_emp_details)
        elif(ch=='4'):
            id=int(input('Enter id you want to delete:'))
            delemp(id)
        elif(ch=='5'):
            id=int(input('Enterb id:'))
            res=searchemp(id)
            print(res)
        elif(ch=='6'):
            print('Logged out...')
        else:
            print('Invalid choice')    




def login():
    print('##### Login Page #####')
    uid='admin'
    passw='1234'
    username=input('Enter Your Username:')
    password=input('Enter your password:')
    if (uid==username) and (passw==password):
        print('Logged in Successfully...')
        empManage()
    else:
        print('Invalid Credential....')    
    
    
    
def main():    
    
    ch=0
    while(ch !='2'):
        print("####Dashboard####")
        print('''
        1. Login(Admin)
        2. Exit
        ''')
        ch=input('Enter choice :')
        if(ch=='1'):
            login()
        elif(ch=='2'):
            print("Thank for choosing us !")    
        else:
            print("invalid choice.... ")    

all_emp_details={}
empManage()            