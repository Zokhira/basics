# 03/25/2021 Functions with return statement

def get_formatted_name(firstname: str, lastname: str):
    name = f"{firstname.title()} {lastname.title()}"
    return name

def print_formatted_name(firstname: str, lastname: str):
    name = f"{firstname.title()} {lastname.title()}"
    print(name)

full_name = get_formatted_name('john', 'doe')
print(full_name)
print(get_formatted_name('jane', 'doe'))

print_formatted_name('ali', 'tehrani')
student = print_formatted_name('baur', 'eskara')
print(f"value of student is: {student}")
print(f"value of student is: {print_formatted_name('baur','eskara')}")

# getter, setter functions
def get_desc_of_what_you_want():
    # logic
    return

def set_desc_of_what_you_want_to_update():
    pass


#     return list(range(2, num + 1, 2))
# print(get_list_of_even_numbers(20))
# print(get_list_of_even_numbers("20"))

def get_list_of_odd_numbers(text: str) -> dict:
    odds = []
    return odds