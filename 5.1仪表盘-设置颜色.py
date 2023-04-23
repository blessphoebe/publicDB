from pyecharts import options as opts
from pyecharts.charts import Gauge

rate=0.557
g = Gauge()
g.add('',[('销售完成率',rate*100)],
      axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color=[(rate, '#37a2da'),(1, '#d2cfd5')], width=30)),
      title_label_opts=opts.LabelOpts(font_size=18, color='black', font_family='Microsoft YaHei'),
      detail_label_opts=opts.LabelOpts(formatter='{value}%',font_size=23, color='red')
      )


g.render(path='d:\\图片\\仪表盘-设置颜色.html')            #注意：运行程序前请确保D盘有“图片”文件夹



