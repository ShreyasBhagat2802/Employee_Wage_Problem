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
