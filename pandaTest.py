

# import pandas

# mydataset = {
#     'Name' : ["MgMg", "HlaHla", "KoKo"],
#     "Age" : [21, 20,18]
# }
# myvar = pandas.DataFrame(mydataset)
# print(myvar)

# myList = [0,1,2,3,4,5]
# myListVar = pandas.DataFrame(myList)
# print(myListVar)

# import pandas as pd

# list = [1,7,2]
# myvar = pd.Series(list)
# myvar2 = pd.Series(list, index=[1,2,3])
# myvar3 = pd.Series(list, index=['A','B','C'])
# print(myvar)
# print(myvar2)
# print(myvar3)

# import pandas as pd
# import numpy as np

# # Creating empty series
# emptySeries = pd.Series()

# print(emptySeries)

# # simple array
# data = np.array(['Dog','Cat','Rabbit','Snake', 'Spider'])

# emptySeries = pd.Series(data)
# print(emptySeries)

# import pandas as pd

# movieDate = {"day1": 'Naruto', "day2": 'Dark', "day3": 'MoneyHeist'}
# myvar = pd.Series(movieDate, index=['day1'])
# print(myvar)

# data = {
#     'Name' : ["MgMg", "HlaHla", "KoKo"],
#     "Age" : [21, 20,18]
# }
# df = pd.DataFrame(data)
# print(df.loc[0])
# print(df.loc[[0,1]])

import pandas as pd
df = pd.read_csv('Bella.csv')
print(df.duplicated())
print(df.drop_duplicates())
print(df.to_string)