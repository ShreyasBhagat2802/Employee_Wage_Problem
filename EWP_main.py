print("Welcome to Employee Wage Computation Program on Master Branch")

#UC1
import random 
attendance = random.randint(0, 1)
    
if attendance == 1:
    print("Employee is Present")
else:
    print("Employee is Absent")

#UC2
wage_per_hour = 20
full_day_hours = 8
    
full_time_wage = wage_per_hour * full_day_hours
    
print(full_time_wage)

#UC3
part_time_hours = 8
    
part_time_wage = wage_per_hour * part_time_hours
    
print(part_time_hours)

#UC4
def employee_type():
    employee_status = random.randint(0, 2)
    
    match employee_status:
        case 2:
            return "full-time"
        case 1:
            return "part-time"
        case _:
            return "absent"

employee_state = employee_type()
if employee_state == "full-time":
    print("Employee is Full Time. Wage: ", {full_time_wage})
elif employee_state == "part-time":
    print("Employee is Part Time. Wage: ", {part_time_wage})
else:
    print("Employee is Absent.")

#UC5
working_days_per_month = 20
month_wage = 0
if employee_state == "full-time":
    month_wage = working_days_per_month * full_time_wage
elif employee_state == "part-time":
    month_wage = working_days_per_month * part_time_wage
print("Month wage is : ", month_wage)