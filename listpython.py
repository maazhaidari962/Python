calculation_to_units = 24
name_of_unit = "hours"

def day_to_units(num_of_days):
    #print(num_of_days > 0)
    if num_of_days > 0:
     return f"{num_of_days} days are { num_of_days * calculation_to_units} {name_of_unit}"




def validate():

     try:
        num_da = int(list_elements)
        if num_da  > 0:
            numr=day_to_units(num_da)
            print(numr)
        elif num_da ==0:

          print("you entered 0. Please enter a valid number")
        else:
            print("you entered a negative number")
     except ValueError:
       print("please input a valid number,,,,")



num_days=""
while num_days !="exit":
   # for num_days_elements in num_days:
           num_days=input("please input number of days Or press enter to exit program\n")
           for list_elements in set(num_days.split()):

            #print(num_days)
            validate()

#number=day_to_units(35)
#print(number)