from pyecharts import options as opts
from pyecharts.charts import Bar,Pie,Grid,Page
from pyecharts.globals import ThemeType
import pandas as pd
df=pd.read_excel(r'd:\图表\资产负债表.xlsx')    #注意：运行前先将数据文件复制到D盘“图片”文件夹中
#df_list = df.values.tolist()
x1=df['资产项目']
y1=df['金额（百万）']
x2=df['负债项目']
y2=df['金额（百万）.1']
print(df)
p1=Pie()
p1.add('',[list(z) for z in zip(x1,y1)],radius=['40%','55%'])   #制作饼图图表
p1.set_global_opts( title_opts=opts.TitleOpts(title='资产分析'))  #设置标题和图例
p1.set_series_opts(label_opts=opts.LabelOpts(position='outside',
                                            background_color='#eee',
                                            border_color='#aaa',
                                            border_width=1,
                                            border_radius=4,
                                            formatter='{a|资产合计：3900}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}',
                                            rich={ 'a': {'color': '#696969', 'lineHeight': 22, 'align': 'center'},
                'abg': {'backgroundColor': '#e3e3e3','width': '100%','align': 'right','height': 22,'borderRadius': [4, 4, 0, 0]},
                'hr': {'borderColor': '#aaa','width': '100%','borderWidth': 0.5, 'height': 0},
                'b': {'fontSize': 16, 'lineHeight': 33},
                'per': {'color': '#eee','backgroundColor':'#334455','padding': [2, 4],'borderRadius': 2}}
            ))  #设置数据系列
p1.set_colors(['red','blue','orange','lightgreen','purple','grey','lightblue'])  #设置扇形颜色
p1.render(path='e:\\练习\\图表\\柱图饼图组成图-资产负债表1.html')

p2=Pie()
p2.add('',[list(z) for z in zip(x2,y2)],radius=['40%', '55%'])   #制作饼图图表
p2.set_global_opts( title_opts=opts.TitleOpts(title='负债分析',pos_left='5%'))  #设置标题和图例
p2.set_series_opts(label_opts=opts.LabelOpts(position='outside',
                                            background_color='#eee',
                                            border_color='#aaa',
                                            border_width=1,
                                            border_radius=4,
                                            formatter='{a|负债合计：440}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%} ',
                                            rich={ 'a': {'color': '#696969', 'lineHeight': 22, 'align': 'center'},
                'abg': {'backgroundColor': '#e3e3e3','width':'100%','align':'right','height': 22,'borderRadius': [4, 4, 0, 0]},
                'hr': {'borderColor': '#aaa','width': '100%','borderWidth': 0.5, 'height': 0},
                'b': {'fontSize': 16, 'lineHeight': 33},
                'per': {'color': '#eee','backgroundColor': '#334455','padding': [2, 4],'borderRadius': 2}}
            ))  #设置数据系列
p2.set_colors(['HotPink','Turquoise','MediumPurple','LightSkyBlue','Khaki','Tan'])  #设置扇形颜色
p2.render(path='d:\\图表\\柱图饼图组成图-资产负债表2.html')   #注意：运行程序前请确保D盘有“图片”文件夹


'''
