import pandas as pc
df=pc.read_excel('test.xlsx',header=None)
df.to_csv('2.txt',header=None,sep=',',index=False)