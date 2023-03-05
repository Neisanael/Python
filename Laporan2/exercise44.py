fetch_data = None
dict = {"George Washington":1, "Thomas Jefferson":2, "Abraham Lincoln":5, "Alexander Hamilton":10, "Andrew Jackson":20, "Ulysses S. Grant":50, "Benjamin Franklin":100}
print("{:<30} {:<30}".format('Individual', 'Amount'))

for value in dict.items() :
    indv, amount = value
    print("{:<30} {:<30}".format(indv, amount))

data = float(input("Masukan data yang akan dicari : "))
for individual, amnt in dict.items() :
    if data == amnt :
        fetch_data = individual

if fetch_data is None :
    print("No Data Found!")
else : 
    print("The name of the denomination of a banknote ",fetch_data)