# Read file
employee_file = open("employees.txt", "r")

if employee_file.readable():
    print(employee_file.readlines())

employee_file.close()

# Write file (append)
employee_file = open("employees.txt", "a")

if employee_file.writable():
    employee_file.write("\nToby - Human Resources")

employee_file.close()

# Write file (overwrite)
employee_file = open("employees.txt", "w")

if employee_file.writable():
    employee_file.write(
        "Jim - Salesman\nDwight - Salesman\nPam - Receptionist\nMichael - Manager\nOscar - Accountant\nToby - Human Resources\nKelly - Customer Service"
    )

employee_file.close()
