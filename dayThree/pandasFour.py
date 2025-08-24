import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv(r'C:\Users\sudhakar\Desktop\Kiran Bhai\RPSShubda\pulseData.csv')
#df.plot()
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plt.show()
#print(df.corr())
 

