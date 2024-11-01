def calculate_love_score():
    stringTrue = "TRUE"
    stringLove = "LOVE"
    name1 = input("Please enter the 1st name: ")
    name2 = input("Please enter the 2nd name: ")
    name1name2 = name1 + name2
    for index, char in enumerate(stringTrue):
        tcount = name1name2.upper().count("T")
        rcount = name1name2.upper().count("R")
        ucount = name1name2.upper().count("U")
        ecount = name1name2.upper().count("E")
    totalTrue = tcount + rcount + ucount + ecount
    print(f"T occurs {tcount} times")
    print(f"R occurs {rcount} times")
    print(f"U occurs {ucount} times")
    print(f"E occurs {ecount} times")
    print((f"Total = {totalTrue}"))
    for index, char in enumerate(stringLove):
        lcount = name1name2.upper().count("L")
        ocount = name1name2.upper().count("O")
        vcount = name1name2.upper().count("V")
        e2count = name1name2.upper().count("E")
    totalLove = lcount + ocount + vcount + e2count
    print(f"L occurs {lcount} times")
    print(f"O occurs {ocount} times")
    print(f"V occurs {vcount} times")
    print(f"E occurs {e2count} times")
    print(f"Total = {totalLove}")
    print(f"\nLove Score = {totalTrue}{totalLove}") 
calculate_love_score()
