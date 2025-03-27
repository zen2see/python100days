import pandas

# THE DATA
"https://data.cityofnewyork.us/Environment/\
2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/about_data"

# GET SQUIRREL DATA INTO A DATAFRAME
squirrel_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# MAKE A DATAFRAME
df_sd = pandas.DataFrame(squirrel_data)
# CAPITALIZE THE HEADER 
df_sd.columns = [col.capitalize() for col in df_sd.columns]

def grey_squirrels():
    grey_squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
    print(grey_squirrels)

def grey_squirrels_count():
    grey_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
    # print(f"{grey_squirrels_count}")
    return grey_squirrels_count

def cinnamon_squirrels_count():
    cinnamon_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
    # print(f"{cinnamon_squirrels_count}")
    return cinnamon_squirrels_count

def black_squirrels_count():
    black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
    # print(f"{black_squirrels_count}")
    return black_squirrels_count

def file_to_csv():
    df_sd.to_csv('Squirrel_count.csv', sep=',', header=True, float_format=str, index=False,)

# MAKE A DICTIONARY OF FUR COUNTS
data_dict = {
    "Fur Color": ["Grey", "Cinnamon",  "Black"],
    "Count": [grey_squirrels_count(), cinnamon_squirrels_count(), black_squirrels_count()]
}
def read_file():
    # Read the CSV file and format the output with fixed-width columns
    with open("dataframe_squirrel_colors.csv", "r") as file:
        lines = file.readlines()
    return lines

# Determine the maximum width for each column
def find_max_col_width(lines):
    max_widths = [max(len(str(item)) for item in col) for col in zip(*[line.split() for line in lines])]
    return max_widths

# Format each line with fixed-width columns
def fixed_width_cols(max_widths):
    formatted_lines = []
    for line in lines:
        items = line.split()
        formatted_line = " ".join(f"{item:<{max_widths[i]}}" for i, item in enumerate(items))
        formatted_lines.append(formatted_line)
    return formatted_lines

# Write the formatted lines back to the CSV file
def write_formatted():
    with open("dataframe_students_scores.csv", "w") as file:
        file.write("\n".join(formatted_lines))

# DETERMINE MAX WIDTH FOR COLUMNS
def determine_max_col_width():
    max_widths = [max(len(str(item)) for item in col) for col in zip(*[line.split() for line in lines])]

def fur_color_to_csv():
    # MAKE A DATAFRAME
    df_fc = pandas.DataFrame(data_dict)
    # CAPITALIZE THE HEADER 
    # df_fc.columns = [col.capitalize() for col in df_fc.columns]
    # CAPITALIZE THE ENTIRE HEADER
    df_fc.columns = [col.upper() for col in df_fc.columns]
    # CONVERT TO CSV AND CHANGE DELIMETER TO SPACES
    df_fc.to_csv("dataframe_squirrel_colors.csv", sep=',', index=False, header=True)

def main():
    print("Grey squirrel count: ", grey_squirrels_count(),)
    # fixed_width_cols(find_max_col_width(read_file()))
    fur_color_to_csv()

if __name__ == '__main__':
    main()