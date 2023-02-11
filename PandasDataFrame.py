import  pandas as pd
def main():
    # A pandas Series is like a column in a table
    # it's one - D Array Holding Data of any type
    # Pandas DataFrame #
    ''' A pandas Series DataFrame is a 2D dataStructure ,
     like a 2D array , or a table with rows and columns '''

    data = {
        "Calories" : [420 , 380 , 390] ,
        "Duration" : [50 , 40 , 45]
    }
    df = pd.DataFrame(data)
    print("Index" , df )
    print(df.loc[2])   # to return specified row(s)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
