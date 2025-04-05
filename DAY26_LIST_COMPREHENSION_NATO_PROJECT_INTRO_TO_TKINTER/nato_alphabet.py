import pandas

"""Loads data from CSV file."""
def get_nato_data():
    natodata = pandas.read_csv("nato_phonetic_alphabet.csv")
    return natodata
    # OR return pandas.read_csv("nato_phonetic_alphabet.csv")

# """Returns a list of the letters"""
# def get_letters_into_list():
#     nato_letters = get_natodata().letter.to_list()
#     return nato_letters

# """Returns a list of the codes"""
# def get_codes_into_list():
#     nato_codes =get_natodata().code.to_list()
#     return nato_codes

def create_nato_lists():
    nato_data = get_nato_data()
    letters = nato_data.letter.to_list()
    codes = nato_data.code.to_list()
    return letters, codes

def create_nato_dict():
    nato_data = get_nato_data()
    nato_dict = {row.letter: row.code for index, row in nato_data.iterrows()}
    return nato_dict

def phonetic_code():
    word = input("\nEnter a word: ").upper()
    get_nato_dict = create_nato_dict()
    pcode = [get_nato_dict[letter] for letter in word if letter in get_nato_dict]
    print(pcode)

def main():
    # print(get_letters_into_list())
    # print(get_codes_into_list())
    letters, codes = create_nato_lists()
    # print(letters)
    # print(codes)
    nato_dict = create_nato_dict()
    print(nato_dict)
    phonetic_code()

if __name__ == '__main__':
    main()