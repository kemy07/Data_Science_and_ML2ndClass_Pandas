import  pandas as pd
def main():
    # A pandas Series is like a column in a table
    # it's one - D Array Holding Data of any type
    # Pandas Read CSV #

    df = pd.read_csv ('airtravel.csv')
    print(df)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
