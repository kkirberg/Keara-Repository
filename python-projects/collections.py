# lists
lst = [10,20,30,40,50]
lst.append(5)
lst.append(6)
lst.append(7)
print(lst)

lst.remove(40)
print(lst)
lst.pop(2)
print(lst)

lst.reverse()
print(lst)
lst.sort()
print(lst)

lst[0] = 500
print(lst)

lst = lst[1:]
print(lst)

index10 = lst.index(10)
print(index10)
lst.append(20)
lst.append(20)
lst.append(20)
print(lst)
count20 = lst.count(20) # this method will be helpful for HW 2
print(count20)

copy_lst = lst
print(copy_lst)
copy_lst[0] = 99
print(copy_lst)
print(lst)

new_copy = lst.copy()
print(new_copy)
new_copy[0] = 14
print(new_copy)
print(lst)

new_copy = lst[:]

empty_lst = []
for val in lst:
    empty_lst.append(val)
print(empty_lst)

empty_lst = []
print(empty_lst)

empty_lst = [0] * 10
print(empty_lst)
empty_lst[0] = 10

squares = []
for i in range(1,10):
    squares.append(i*i) # could also say i**2
print(squares)

squares = [x * x for x in range(1,10)]
print(squares)

plus_5 = [val + 5 for val in squares]
print(plus_5)

values = [34,27,95,18,36,21,64,50,77]
even_values = [x for x in values if x%2==0]
print(even_values)
small_vals = [x for x in values if x<20]
print(small_vals)

# dictionaries
fav_foods = {"Keara" : "risotto", "Brendan" : "sushi", "Dan" : "burgers", "Katie" : "burgers"}
print(fav_foods)

kff = fav_foods["Keara"]
print(kff)

for key in fav_foods:
    print(f"{key}'s favorite food is {fav_foods[key]}")

for person, food in fav_foods.items():
    print(f"{person}'s favorite food is {food}")

if "Bob" in fav_foods:
    print(fav_foods["Bob"])
else:
    fav_foods["Bob"] = "wings"
print(fav_foods)

# dictionary comprehension
day_names = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
days = {n+1 : day_names[n] for n in range(len(day_names))}
for day_num, day_name in days.items():
    print('Day', day_num, 'is', day_name)