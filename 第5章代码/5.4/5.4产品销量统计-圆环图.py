import pandas as pd
import matplotlib.pyplot as plt
import xlwings as xw
df=pd.read_excel(r'd:\图片\产品销售统计.xlsx') #注意：运行前先将数据文件复制到D盘“图片”文件夹中
fig=plt.figure()
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
x=df['品牌']
y=df['数量']
plt.pie(y,labels=x,labeldistance=1.1,autopct='%.2f%%',pctdistance=0.85,radius=1.0,wedgeprops={'width':0.3,'linewidth':2,'edgecolor':'white'})
plt.title('产品销量占比分析图',fontdict={'color':'red','size':18},loc='center')
app=xw.App(visible=True)
wb=app.books.open(r'd:\图片\产品销售统计.xlsx')  #注意：运行程序前请确保D盘有“图片”文件夹
sht=wb.sheets[0]
sht.pictures.add(fig,name='产品销量占比图表',update=True,left=200)
wb.save()
wb.close()
app.quit()
