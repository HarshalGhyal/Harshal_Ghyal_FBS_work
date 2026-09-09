from empmanage import EmpManage
class Main:
    def login():
        print('Login Page')
        uid = 'admin'
        passw = '1234'
        username =input('enter username:')
        passward =input('enter passward:')
        if(uid == username and passw == passward):
            print('login sucessfully..')
            emp =EmpManage()
            while True:
                print("Enter 1 for AddEmp")
                print("Enter 2 for DisplayEmp")
                print("Enter 3 for SearchEmp")
                print("Enter 4 for UpdateEmp")
                print("Enter 5 for DeleteEmp")
                print("Enter 6 for Exit")
                ch=int(input("enter your choice:"))
                if(ch == 1):
                    emp.addEmp()
                elif(ch == 2):
                    emp.displayEmp()
                elif(ch == 3):
                    emp.searchEmp()
                elif(ch == 4):
                    emp.updateEmp()
                elif(ch == 5):
                    emp.delEmp()
                elif(ch == 6):
                    print("Thank you...")
                else:
                    print("Invalid choice")

        else:
            print('Invalid details')

Main.login()