name=input("Enter the employees name : ")
basicSalary=input("Enter the basic Salary :")
medicalAllowance=0.15*int(basicSalary)
transportAllowance=0.1*int(basicSalary)
houseAllowance=0.20*int(basicSalary)
nhif=1000
grossPay= medicalAllowance+ transportAllowance +houseAllowance+int(basicSalary)-nhif
print('\n\n\n')
print("*********************************************")
print(f'Employees Name : {name} ')
print("*********************************************")
print(f'Basic Salary :          {basicSalary}')
print(f'Medical Allowance :     {medicalAllowance}')
print(f'transport Allowance :   {transportAllowance}')
print(f'House Allowance :       {houseAllowance}')
print(f'NHIF :                  {nhif}')
print("*********************************************")
print(f'Gross Pay :             {grossPay}')
print("*********************************************")