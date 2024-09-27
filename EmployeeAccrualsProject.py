import csv

# Employee_list is a list containing employee objects
# Employee list index is used to check for already exisiting employees and contains employee id's
# if an ID exists in employee_list_index, this means that the employee exists and is at the same index
# employee_list[i] and employee_list_index[i] refer to the same employee (employee object vs id)
employee_list = []
employee_list_index = []

class employee:
    def __init__(self, number, status):
        self.employee_number = number
        self.employee_status = status
    administrative_leave = 0
    bereavement = 0
    comp = 0
    donated_vacation_hold = 0
    essf = 0
    floating_holiday = 0
    fto_release_time = 0
    holiday_fire_tour = 0
    military_leave = 0
    pd_holiday = 0
    personal_leave = 0
    sick = 0
    vacation = 0


# This function takes in the balance name as a string and assigns the hours worked value to the correct employee field.

def update_employee_balance(balanceName, employee, value):
    match balanceName:
        case "Administrative Leave":
            employee.administrative_leave = value
        case "Bereavement":
            employee.bereavement = value
        case "Comp":
            employee.comp = value
        case "Donated Vacation Hold":
            employee.donated_vacation_hold = value
        case "Earned Sick & Safe":
            employee.essf = value
        case "Floating Holiday":
            employee.floating_holiday = value
        case "FTO Release Time":
            employee.fto_release_time = value
        case "Holiday Fire Tour":
            employee.holiday_fire_tour = value
        case "Military Leave":
            employee.military_leave = value
        case "PD-Holiday":
            employee.pd_holiday = value
        case "Personal Leave":
            employee.personal_leave = value
        case "Sick":
            employee.sick = value
        case "Vacation":
            employee.vacation = value


with open('accruals.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # If the employee already exists
        if row['EmpNumber'] in employee_list_index:
            employee_object_index = employee_list_index.index(row['EmpNumber'])
            update_employee_balance(row['BalanceName'],employee_list[employee_object_index],row['Hours']) # add the balance to the employee object
        else:
            # if the employee doesn't already exist, add the employee id to employee_list_index as well as create a new employee object
            employee_list_index.append(row['EmpNumber'])
            employee_list.append(employee(row['EmpNumber'],row['Emp Status']))
            employee_object_index = employee_list_index.index(row['EmpNumber'])
            update_employee_balance(row['BalanceName'],employee_list[employee_object_index],row['Hours']) # add the balance to the employee object
        
# Writing the names of all the columns. We are creating output.csv
f = open("output.csv", "w")
f.write("EmpNumber,EmpStatus,Bereavement,Comp,DonatedVacationHold,EarnedSick&Safe,FloatingHoliday,FTO,HolidayFireTour,MilitaryLeave,PDHoliday,PersonalLeave,Sick,Vacation,\n")

# populate the output.csv file with the details for each employee
for employee in employee_list:
    f.write(employee.employee_number + ","
        + employee.employee_status
        + ",BEREAVEMENT~"+ str(employee.bereavement) + "~SET"
        + ",COMP~" + str(employee.comp) + "~SET"
        + ",DONATED VACATION HOLD~" + str(employee.donated_vacation_hold) + "~SET"
        + ",ESST~" + str(employee.essf) + "~SET"
        + ",FLOATING HOLIDAY~" + str(employee.floating_holiday) + "~SET"
        + ",FTO RELEASE TIME~" + str(employee.fto_release_time) + "~SET"
        + ",HOLIDAY FIRE TOUR~" + str(employee.holiday_fire_tour) + "~SET"
        + ",MILITARY~" + str(employee.military_leave) + "~SET"
        + ",PD HOLIDAY~" + str(employee.pd_holiday) + "~SET"
        + ",PERSONAL LEAVE~" + str(employee.personal_leave) + "~SET"
        + ",SICK~" + str(employee.sick) + "~SET"
        + ",VACATION~" + str(employee.vacation) + "~SET\n")

     
f.close()
