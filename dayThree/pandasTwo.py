import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a, index = ["xar", "yar", "zar"])
print(myvar)
print(myvar['zar'])
