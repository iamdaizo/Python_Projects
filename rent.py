persons = int(input("Enter the number of persons staying in the flat: "))
rent = int(input("Enter the rent of your flat: "))
foods_ordered = int(input("Enter total foods ordered by you: "))
electricity_charges = int(input("Enter total electricity spend: "))
charge_per_unit = int(input("Enter charges per unit: "))

total_bill = electricity_charges * charge_per_unit
sum = rent + foods_ordered + total_bill
equal = sum/persons 
print(f"The amount to be paid equally by each person is: {equal}") 