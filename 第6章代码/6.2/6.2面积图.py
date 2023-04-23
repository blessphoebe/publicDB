from pyecharts import options as opts
from pyecharts.charts import Line
import pandas as pd

df=pd.read_excel(r'd:\图片\财务收入支出分析表.xlsx')    #注意：运行前先将数据文件复制到D盘“图片”文件夹中
df_list = df.values.tolist()
x=[]
y1=[]
y2=[]
for data in df_list:
    x.append(data[0])
    y1.append(data[1])
    y2.append(data[2])

l= Line()
l.add_xaxis(x)
l.add_yaxis('收入', y1,color='#8A2BE2',areastyle_opts=opts.AreaStyleOpts(opacity=0.5))   
l.add_yaxis('支出', y2,color='#FF4500',areastyle_opts=opts.AreaStyleOpts(opacity=0.5))     

l.set_global_opts(
                  title_opts=opts.TitleOpts('公司收入支出分析',pos_left='5%'),
                  xaxis_opts=opts.AxisOpts(axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                                           is_scale=False,boundary_gap=False)
                  )

l.render(path='d:\\图片\\面积图-收入支出.html')       #注意：运行程序前请确保D盘有“图片”文件夹


