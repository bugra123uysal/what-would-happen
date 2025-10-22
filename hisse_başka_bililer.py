import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


al=pd.read_excel("C:\\Users\\buğra\\Desktop\\ne-olur\\hisseler_hakkında_başka_bilgiler.xlsx")
print(al.columns)

shares=al["Shares"].value_counts()
shares.plot(kind='bar')
plt.title("Share")
plt.grid(True)
plt.show()
name=al['Hisse']
value=['Volume', 'Marketcap', 'Pe', 'Eps', 'Changepct', 'Shares',
       'Beta']



for i in value:
    maxx=al[i].max()
    minn=al[i].min()

    print(f"{i} Max değeri",  maxx)
    print(f"{i} Min değeri ", minn)





