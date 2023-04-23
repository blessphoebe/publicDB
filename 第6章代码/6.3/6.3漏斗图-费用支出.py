from pyecharts import options as opts
from pyecharts.charts import Funnel
import pandas as pd

df=pd.read_excel(r'd:\图片\财务费用支出明细.xlsx')      #注意：运行前先将数据文件复制到D盘“图片”文件夹中
df_list = df.values.tolist()


f= Funnel()
f.add('费用支出', df_list)   

f.set_global_opts(title_opts=opts.TitleOpts('公司费用支出分析',pos_left='5%'))
f.set_series_opts(label_opts=opts.LabelOpts(formatter='{b}: {c}'))
f.set_colors(['HotPink','Turquoise','MediumPurple','LightSkyBlue','Khaki','Tan']) 

f.render(path='d:\\图片\\漏斗图-费用支出.html')     #注意：运行程序前请确保D盘有“图片”文件夹


