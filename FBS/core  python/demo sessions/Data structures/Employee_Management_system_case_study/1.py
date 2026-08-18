def addEmp(id, name, sal, dept):
    if(id not in 'all_Emp_details'):
        all_Emp_details[id] = [id, name, sal, dept]
        return 'Employee added successfully.'
    else:
        return 'ID already exist.'
    
def showAllEmp():
    print(all_Emp_details)
    
def upEmp(id):
    print("NOTE: If don't want to change leave field blank.")
    emp = all_Emp_details.get(id)
    if(emp):
        name = input(f'Enter New NAME({emp[1]}):') or emp[1]
        sal = int(input(f'Enter New SALARY({emp[2]}):') or 0) or emp[2]
        dept = input(f'Enter New DEPARTMENT({emp[3]}):') or emp[3]
        all_Emp_details[id] = [id, name, sal, dept]
        return 'Employee update successfully.'
    else:
        return 'ID not found.'
    
def delEmp(id):
    if id in all_Emp_details:
        del all_Emp_details[id]
        return 'Employee delete successfully.'
    else:
        return 'ID not found.'

def empManage():
    print('####Employee Manage####')
    ch = 0
    while(ch != '6'):
        print('''Please select option from below:
        1. Add employee
        2. Show all employee
        3. Update employee
        4. Delete employee
        5. Search employee
        6. Logout
        ''')
        ch = input('Enter choice:')
        if(ch == '1'):
            id = input('Enter ID:')
            name = input('Enter NAME:')
            sal = input('Enter SALARY:')
            dept = input('Enter DEPARTMENT:')
            res = addEmp(id, name, sal, dept)
            print(res)
        elif(ch == '2'):
            showAllEmp()
        elif(ch == '3'):
            print('Warning: ID not allowed to update..')
            id = input('Enter ID:')
            res = upEmp(id)
            print(res)
        elif (ch == '4'):
            id = input('Enter ID:')
            res = delEmp(id)
            print(res)
        elif(ch == '6'):
            print('Logged out...')
        else:
            print('Invalid choice...')
               
def login():
    print('####Login page####')
    uid = 'admin'
    password = '1234'
    username = input('Enter USERNAME:')
    password = input('Enter PASSWORD:')
    if(uid == username and password == password):
        print('Logged in successful...')
    else:
        print('Invalid credentials...')
    
def main():    
    ch = 0
    while(ch != '2'):
        print('####DASHBOARD####')
        print('''Please select option from below:
            1. Login(Admin)
            2. Exit
            ''')
        ch = input('Enter choice:')
        if(ch == '1'):
            login()     
        elif(ch == '2'):
            print('Thank you for choosing us!')
        else:
            print('Invalid choice...')
            
#main()
all_Emp_details = {}
empManage()