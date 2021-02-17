"""
David Young
CSC119-479
6/14/2020
Julie Schneider
"""

def main():
    # initial balance is $1000
    # 5% interest per year
    # find balance after first, second, and third year
    # expected answers:
        # year 0 = 1000
        # year 1 = 1050
        # year 2 = 1102.5
        # year 3 = 1157.625
    INITIAL = 1000
    INTEREST = 0.05
    print("Interest of $1000 after 3 years")
    for year in range(3):
        value = INITIAL * ((1 + INTEREST) ** (year+1))
        print("%s %.2f" % ("YEAR 1: ", value))
main()


    
    
