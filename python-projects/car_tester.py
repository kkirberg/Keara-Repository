from car import Car

cars = []

with open("cars.txt") as file:
    for line in file:
        line = line.strip()
        lst = line.split()
        car = Car(lst[0], lst[1], int(lst[2]), int(lst[3]))
        cars.append(car)

print(cars[0])
print(cars[0].get_gas_tank())
print(cars[0].get_odometer())
cars[0].drive()
print(cars[0].get_gas_tank())
print(cars[0].get_odometer())

print(cars[1])
print(cars[1].get_gas_tank())
print(cars[1].get_odometer())
cars[1].drive()
print(cars[1].get_gas_tank())
print(cars[1].get_odometer())