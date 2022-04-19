# v1
hours_worked = 45
pay_rate = 7.25
total_pay = hours_worked * pay_rate
print(total_pay)

# v2
work_hours = 40
ot_pay_rate = pay_rate * 1.5
ot_hours = hours_worked - 40

if hours_worked > work_hours:
    total_pay = (work_hours * pay_rate) + (ot_hours * ot_pay_rate)
    print(total_pay)
else: 
    total_pay = hours_worked * pay_rate
    print(total_pay) 