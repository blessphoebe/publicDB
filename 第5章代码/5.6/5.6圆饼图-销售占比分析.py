from pyecharts import options as opts
from pyecharts.charts import Pie
import pandas as pd
df=pd.read_excel(r'd:\图片\销售额明细4.xlsx')  #注意：运行前先将数据文件复制到D盘“图片”文件夹中

x=df['产品名称']
y=df['销售额']
p = Pie()
p.add('零售',[list(z) for z in zip(x,y)])   
p.set_global_opts( title_opts=opts.TitleOpts(title='销售额占比分析',pos_left='43%'),
                   legend_opts=opts.LegendOpts( orient='vertical', pos_top='30%', pos_right='10%' ))
p.set_series_opts(label_opts=opts.LabelOpts(formatter='{b}: {c}'),
                  itemstyle_opts=opts.ItemStyleOpts(border_color = 'white',border_width=2))
p.set_colors(['red','blue','orange','lightgreen','purple','grey','lightblue'])
p.render(path='d:\\图片\\圆饼图-销售占比分析.html')   #注意：运行程序前请确保D盘有“图片”文件夹

