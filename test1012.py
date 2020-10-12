def sum():
    result =21+ 14
    print("Inside the function:", result)
    return result
total = sum()
print("Outside the function:", total)

def print_info(name, age=35):
    print("Name:", name)
    print("Age", age)
    return
print_info(age=50, name="miki")
print_info(name = "miki")
