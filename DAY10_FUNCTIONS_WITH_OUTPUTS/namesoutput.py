def format_name(fname, lname):
    # Convert first letter in name to upper case
    formattedfname = fname.title()
    formattedlname = lname.title()
    return f"{formattedfname} {formattedlname}"
print(format_name("AnGElA", "YU"))

