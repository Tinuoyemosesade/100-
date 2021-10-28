bill = float(input("how much is your bill"))
no_of_people = int(input("how many people are paying"))
amount_per_person =  round((bill / no_of_people) * 1.12, 2)

print (f"each of you will pay {amount_per_person}")