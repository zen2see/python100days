
# DAY 26 LIST COMPREHENSION 2 EXERCISE 19

# A DICTIONARY
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14,\
             "Friday": 21, "Saturday": 22, "Sunday": 24}

# MUTATES A FUNCTION BY APPLYING A FUNCTION TO EACH KEY-VALUE PAIR
# ITERATE OVER A COPY OF THE KEYS TO AVOID A RUNTIME ERROR
def mutate_weather(input_dict, mutation_function):
    # list() =  creates a list
    for key in list(input_dict.keys()):
       # Iterate over a copy of the keys to avoid RuntimeError
       input_dict[key] = mutation_function(key, input_dict[key])
    # Return the mutated dictionary
    return input_dict  
    
# DEFINE A MUTATION FUNCTION (CELCIUS TO FARENHEIT)
def convert_to_f(key, value):
    return (value * 9/5) + 32

def weather_f_one_liner():
     return {key: round((value * 9/5) + 32, 2) for key, value in weather_c.items()}    

def main():
    weather_f = mutate_weather(weather_c, convert_to_f)
    weather_f_1l = weather_f_one_liner()
    print(weather_f)
    print(weather_f_1l)

if __name__ == '__main__':
    main()
