from functions import *
print()
print('*'*100)
print(' '*25+'Welcome to EMS (Employee management system) Portal')
print('*'*100)
print()

print('Please Confirm, Which information you want to see or modify')
print()
print('1  : Want to see all Employee details')
print('2  : Want to see the perticular Employee details')
print('3  : Want to add the New Employee details')
print('4  : Want to delete the Employee details')
print('5  : Want to promote Employee')
print()

a=int(input())
ems=Ems()
match a:
    case 1:
        ems.all()
    case 2:
        b=int(input('Enter Employee ID : '))
        print()
        ems.emp(b)
        print()
    case 3:
        name=input('Please enter the name of the Candidate : ')
        print()
        MobileNumber=input('Please enter the Contact details of the Candidate : ')
        print()
        EmailID=input('Please Enter the Email id of the Candidate : ')
        print()
        print('Please select, For which position you are going to hire the candidate : ')
        print()
        print('1 : Employee')
        print('2 : Team Lead')
        print('3 : Manager')
        print('4 : Delivery Head')
        print()
        designation=int(input())
        match designation:
            case 1:
                ems.add(name,MobileNumber,EmailID,'Employee')
            case 2:
                ems.add(name,MobileNumber,EmailID,'Team Lead')
            case 3:
                ems.add(name,MobileNumber,EmailID,'Manager')
            case 4:
                ems.add(name,MobileNumber,EmailID,'Delivery Head')
            case default:
                print('If you are not sure, Then we will add this candidate as an Employee')
                print()
                ems.add(name,MobileNumber,EmailID,'Employee')
    
    case 4:
        e=int(input('Please help me with the Employee ID : '))
        ems.dlt(e)            

    case 5 :
        e=int(input('Please help me with the Employee ID : '))
        ems.update(e)

    

