# using variable in strings
first_name = "ada"
last_name = "lovelace"
# we used f format for space in between
full_name = f"{first_name} {last_name}"
print(full_name)
print(f'hello, {full_name.title()}!')
full_name = "{} {}".format(first_name, last_name)
