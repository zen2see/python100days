import csv
import pandas

# PANDAS DOCS - https://pandas.pydata.org/docs/
# CREATES TABLE\DATAFRAME AND COLUMN IS A SERIES - COLUMNS LIKE A LIST

""" 
WITHOUT PANDAS
with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)

def main():
    with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "tmep":
            temperatures.append(int(row[1]))
        print(temperatures)
"""
# ERRORS WITH PANDAS HAD TO "echo PATH=$HOME/.local/bin:$PATH"
# THEN sudo pip3 install pandas

def cvsreader():
    data = pandas.read_csv("weather_data.csv")
    
    # PRINT AS DICTIONARY
    data_dict = data.to_dict()
    print("Data as a dictionary:", data_dict,'\n')
    
    # PRINT LENGTH OF TEMPS 
    temp_list = data["Temp"].to_list()
    print("Length of temps:", len(temp_list),'\n')
    
    # GET AVERAGE TEMP (MEAN)
    temp_mean = data['Temp'].mean()
    print("Average of temps2:", data['Temp'].mean(),'\n') # OR temp_mean 
    
    # GET MAX OF TEMP
    print("Max of temp: ", data['Temp'].max())
    print("Max of temp2:\n ", data[data.Temp == data.Temp.max()],"\n")
    
    # GET GET CONDITION (DATA IN COLUMNS)
    print("Conditions:")
    for condition in data['Condition']:
        print(f" {condition}")
        #, data['condition'].to_string(index=False),'\n')
    print("\nCondisions2:")
    
    # PRINT( data.condition,'\n')
    for condition in data['Condition']:
        print(f" {condition}")
    
    # GET DATA IN A ROW
    print("\nDAY OF WEEK: ")
    print(data[data.Day == 'Monday'])
    monday = data[data.Day =="Monday"]
    # print(f"\nMonday's condition : {monday.Condition}")
    monday_condition = data.loc[data['Day'] == 'Monday', 'Condition'].values[0]
    monday_temp = data.loc[data['Day'] == 'Monday', 'Temp'].values[0] 
    # OR
    mondaytemp = monday.Temp[0]
    print(f"\nMonday Temp in Farenheit = {monday_temp*9/5+32}\u00b0")

    # CREATE A DATAFRAME FROM DICTIONARY
    data_dict = { "students": ["Amy", "James", "Angela"], "scores": [76, 56, 65] }
    dataframe = pandas.DataFrame(data_dict)
    print(f"\nStudent Dataframe\n{dataframe}")
    
    # PRINT WITHOUT THE INDEX
    print(f"\nWithout Index\n{dataframe.to_string(index=False)}")
    
    # CAPITALIZE THE HEADER 
    dataframe.columns = [col.capitalize() for col in dataframe.columns]
    # CAPITALIZE THE ENTIRE HEADER
    dataframe.columns = [col.upper() for col in dataframe.columns]
    
    # CONVERT TO CSV AND CHANGE DELIMETER TO SPACES
    dataframe.to_csv("dataframe_students_scores.csv", sep=',', index=False, header=True)
   
def main():
    cvsreader()

if __name__ == '__main__':
    main()