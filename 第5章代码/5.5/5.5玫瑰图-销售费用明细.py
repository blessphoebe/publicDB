import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie
df=pd.read_excel(r'd:\图片\销售费用明细.xlsx')     #注意：运行前先将数据文件复制到D盘“图片”文件夹中
x=df['销售费用项目']
y=df['金额']

p = Pie()
p.add('',[list(z) for z in zip(x, y)],radius=['30%', '40%'],center=[300,200],rosetype='radius')
p.set_global_opts(title_opts=opts.TitleOpts(title='销售费用分析',pos_left='28%'),
                  legend_opts=opts.LegendOpts(orient='vertical',pos_top='20%',pos_left='65%' ))
p.set_series_opts(label_opts=opts.LabelOpts(formatter='{b}:{c}'))
p.set_colors(['orange','blue','grey','cyan','purple','red','green','Lime']) 
p.render(path='d:\\图片\\玫瑰图-销售费用明细.html')    #注意：运行程序前请确保D盘有“图片”文件夹
