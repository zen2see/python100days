def format_name(fname, lname):
    if fname == "" or lname == "":
        return "You did not provide valid inputs."
    # Convert first letter in name to upper case
    formattedfname = fname.title()
    formattedlname = lname.title()
    return f"{formattedfname} {formattedlname}"
# print(format_name("AnGElA", "YU"))
print(format_name(input("What is your first name? "), input("What is your last name? ")))
