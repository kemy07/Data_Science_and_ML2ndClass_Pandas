import  pandas as pd
def main():
    # A pandas Series is like a column in a table
    # it's one - D Array Holding Data of any type
    # Pandas Analyzing DataFrames #
    ''' head method returns the header and specified number of row ,
      starting from the top '''
    df = pd.read_csv ('airtravel.csv')
    print(df.head(9))
    print(df.tail(5))
    ''' tail method for viewing the last rows of the data frame
     , and also return the headers and specified number of rows , starting 
     from the bottom '''
    ###############################
    print(df.info())
    '''
    method info gives you more information about the data set
    '''
    ###############################
    print(df.describe())
    '''
    method describe returns description of the data in the data frame , 
    if the data fram contains numerical data , the description contains
    ( count - mean - std - min - 25% - 50% - 75% - max ) 
    '''
    ###############################
    print(df.corr())
    '''
    method corr calculates the relationship between each column in your data set 
    '''

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
