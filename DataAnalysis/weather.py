# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MultipleLocator
from wordcloud import WordCloud


# 2011~2023年厦门市每月最高最低温分布图
def pic_plot_fill():
    # 画图
    fig = plt.figure(dpi=128, figsize=(10, 6))
    # 按照地区分组2022年厦门市每月最高最低温分布图
    temp = weather.groupby(by='place').apply(lambda x: x[(x['place'] == '厦门')])
    # print(temp)
    plt.plot(temp['date'], temp['high'], c='red', alpha=0.5, linestyle='solid', marker='o', label='最高温')
    plt.plot(temp['date'], temp['low'], c='blue', alpha=0.5, linestyle='solid', marker='o', label='最低温')
    plt.fill_between(temp['date'], temp['high'], temp['low'], facecolor='yellow', alpha=0.2)
    # 设置图标的图形格式
    plt.title('2011~2023年厦门市每月最高最低温分布图', fontsize=24)
    plt.xlabel('月份', fontsize=12)
    fig.autofmt_xdate()
    plt.ylabel('气温', fontsize=12)
    plt.tick_params(axis='both', which='major', labelsize=10)

    x_major_locator = MultipleLocator(7)
    # 把x轴的刻度间隔设置为5，并存在变量里
    ax = plt.gca()
    # ax为两条坐标轴的实例,gc==get current axes
    ax.xaxis.set_major_locator(x_major_locator)
    # 把x轴的主刻度设置为1的倍数
    # 在图表的角落显示带有颜色的线条标签
    plt.legend()
    # 显示
    plt.savefig('2011~2023年厦门市每月最高最低温分布图.png')
    plt.show()


# 2018~2022年厦门市全年气温对比图
def pic_plot():
    # 画图
    fig = plt.figure(dpi=128, figsize=(10, 6))

    temp_18 = weather.groupby(by='place').apply(lambda x: x[(x['place'] == '厦门') & (x['year'] == '2018')])
    temp_19 = weather.groupby(by='place').apply(lambda x: x[(x['place'] == '厦门') & (x['year'] == '2019')])
    temp_20 = weather.groupby(by='place').apply(lambda x: x[(x['place'] == '厦门') & (x['year'] == '2020')])
    temp_21 = weather.groupby(by='place').apply(lambda x: x[(x['place'] == '厦门') & (x['year'] == '2021')])
    temp_22 = weather.groupby(by='place').apply(lambda x: x[(x['place'] == '厦门') & (x['year'] == '2022')])
    # print(temp_pre)
    # print(temp_next)
    # plt.scatter(temp_11['month'], temp_11['high'], c='red', alpha=0.5)
    plt.plot(temp_18['month'], temp_18['high'], c='yellow', alpha=0.5, linestyle='solid', marker='o', label='2018年')
    plt.plot(temp_19['month'], temp_19['high'], c='red', alpha=0.5, linestyle='solid', marker='o', label='2019年')
    plt.plot(temp_20['month'], temp_20['high'], c='blue', alpha=0.5, linestyle='solid', marker='o', label='2020年')
    plt.plot(temp_21['month'], temp_21['high'], c='purple', alpha=0.5, linestyle='solid', marker='o', label='2021年')
    plt.plot(temp_22['month'], temp_22['high'], c='green', alpha=0.5, linestyle='solid', marker='o', label='2022年')

    # plt.bar(temp_11['month'], temp_11['high'],  alpha=0.5)

    # 设置图标的图形格式
    plt.title('2018~2022年厦门市全年气温对比图', fontsize=24)
    plt.xlabel('月份', fontsize=12)
    fig.autofmt_xdate()
    plt.ylabel('气温', fontsize=12)
    plt.tick_params(axis='both', which='major', labelsize=10)
    # 在图表的角落显示带有颜色的线条标签
    plt.legend()
    # 显示
    plt.savefig('2018~2022年厦门市全年气温对比图.png')
    plt.show()


# 2011~2023年厦门市气候分布饼图
def pic_pie_weather():
    # 天气可视化饼图
    temp = weather.groupby(by='place').apply(lambda x: x[
        (x['place'] == '厦门') & (x['year'] == '2019') | (x['year'] == '2020') | (x['year'] == '2021') | (
                x['year'] == '2022') | (x['year'] == '2018') | (x['year'] == '2017') | (x['year'] == '2016') | (
                x['year'] == '2015')
        | (x['year'] == '2014') | (x['year'] == '2013') | (x['year'] == '2012') | (x['year'] == '2011') | (
                x['year'] == '2023')])['weather']
    temp = list(temp)
    print(temp)
    # 判断元素是否在字典里如果不在就将元素放进去并加1
    dic_wea = {}
    for i in range(1, 12 * 4):
        if temp[i] in dic_wea.keys():
            dic_wea[temp[i]] += 1
        else:
            dic_wea[temp[i]] = 1
    print(dic_wea)
    explode = [0.01] * len(dic_wea.keys())
    color = ['blue', 'silver', 'yellow', 'grey', 'gold', 'red', 'green', 'pink']
    # explode：设置各部分突出       label:设置各部分标签
    # labeldistance:设置标签文本距圆心位置，1.1表示1.1倍半径
    # autopct：设置圆里面文本       shadow：设置是否有阴影
    # startangle：起始角度，默认从0开始逆时针转        pctdistance：设置圆内文本距圆心距离
    plt.figure(dpi=128, figsize=(10, 6))
    plt.pie(dic_wea.values(), explode=explode, labels=dic_wea.keys(), autopct='%1.1f%%', colors=color,
            labeldistance=1.1)
    # 设置字体样式字典
    font_dict = dict(fontsize=24,
                     weight='bold',
                     )
    plt.title('2011~2023年厦门市气候分布饼图', fontdict=font_dict)
    # 显示与设置小图位置
    # plt.legend(loc='lower left')
    plt.savefig('2011~2023年厦门市气候分布饼图.png')
    plt.show()


# 2011~2023年厦门市风向分布饼图
def pic_pie_wind():
    # 天气可视化饼图
    temp = weather.groupby(by='place').apply(lambda x: x[
        (x['place'] == '厦门') & (x['year'] == '2019') | (x['year'] == '2020') | (x['year'] == '2021') | (
                x['year'] == '2022') | (x['year'] == '2018') | (x['year'] == '2017') | (x['year'] == '2016') | (
                x['year'] == '2015')
        | (x['year'] == '2014') | (x['year'] == '2013') | (x['year'] == '2012') | (x['year'] == '2011') | (
                x['year'] == '2023')])['wind']
    temp = list(temp)
    print(temp)
    dic_wea = {}
    for i in range(1, 12 * 4):
        if temp[i] in dic_wea.keys():
            dic_wea[temp[i]] += 1
        else:
            dic_wea[temp[i]] = 1
    print(dic_wea)
    explode = [0.01] * len(dic_wea.keys())
    color = ['blue', 'silver', 'yellow', 'grey', 'gold', 'red', 'green', 'pink']
    plt.figure(dpi=128, figsize=(10, 6))
    plt.pie(dic_wea.values(), explode=explode, labels=dic_wea.keys(), autopct='%1.1f%%', colors=color,
            labeldistance=1.1)
    # 设置字体样式字典
    font_dict = dict(fontsize=24,
                     weight='bold',
                     )
    plt.title('2011~2023年厦门市风向分布饼图', fontdict=font_dict)
    # 显示与设置小图位置
    # plt.legend(loc='lower left')
    plt.savefig('2011~2023年厦门市风向分布饼图.png')
    plt.show()


# 2022年福建省地级市气温对比柱状图
def pic_hist():
    # 画图
    fig = plt.figure(dpi=128, figsize=(10, 6))
    # 福建省的8个地级市
    zhangzhou = weather.groupby(by='place').apply(lambda x: x[(x['place'] == '漳州') & (x['year'] == '2022')])
    quanzhou = weather.groupby(by='place').apply(lambda x: x[(x['place'] == '泉州') & (x['year'] == '2022')])
    fuzhou = weather.groupby(by='place').apply(lambda x: x[(x['place'] == '福州') & (x['year'] == '2022')])
    ningde = weather.groupby(by='place').apply(lambda x: x[(x['place'] == '宁德') & (x['year'] == '2022')])
    sanming = weather.groupby(by='place').apply(lambda x: x[(x['place'] == '三明') & (x['year'] == '2022')])
    xiamen = weather.groupby(by='place').apply(lambda x: x[(x['place'] == '厦门') & (x['year'] == '2022')])
    putian = weather.groupby(by='place').apply(lambda x: x[(x['place'] == '莆田') & (x['year'] == '2022')])
    nanping = weather.groupby(by='place').apply(lambda x: x[(x['place'] == '南平') & (x['year'] == '2022')])

    plt.barh(zhangzhou['month'], zhangzhou['high'], alpha=0.5, linestyle='solid', color='red', label='漳州')
    plt.barh(quanzhou['month'], quanzhou['high'], alpha=0.5, linestyle='solid', color='blue', label='泉州')
    plt.barh(fuzhou['month'], fuzhou['high'], alpha=0.5, linestyle='solid', color='orange', label='福州')
    plt.barh(ningde['month'], ningde['high'], alpha=0.5, linestyle='solid', color='yellow', label='宁德')
    plt.barh(sanming['month'], sanming['high'], alpha=0.5, linestyle='solid', color='silver', label='三明')
    plt.barh(xiamen['month'], xiamen['high'], alpha=0.5, linestyle='solid', color='green', label='厦门')
    plt.barh(putian['month'], putian['high'], alpha=0.5, linestyle='solid', color='pink', label='莆田')
    plt.barh(nanping['month'], nanping['high'], alpha=0.5, linestyle='solid', color='purple', label='南平')

    # 设置图标的图形格式
    plt.title('2022年福建省地级市气温对比柱状图', fontsize=24)
    plt.xlabel('气温', fontsize=12)
    fig.autofmt_xdate()
    plt.ylabel('月份', fontsize=12)
    plt.tick_params(axis='both', which='major', labelsize=10)
    # 在图表的角落显示带有颜色的线条标签
    plt.legend()
    # 显示
    plt.savefig('2022年福建省地级市气温对比柱状图.png')
    plt.show()


# 2011~2023年福建省所有城市的天气词云图
def pic_wordCloud():
    temp = str(list(weather['weather']))
    print(temp)
    text_list = ' '.join(temp)

    wc1 = WordCloud(
        background_color='white',  # 背景色
        width=2000,  # 宽度
        height=1000,  # 高度
        font_path='AdobeKaitiStd-Regular.otf',  # 字体文件，此处与py文件放在同一目录
        margin=1,  # 词语边缘距离
    )
    wc1.generate(text_list)  # 绘制词云
    # imshow() 可以接受不同维数的数组作为输入，从而生成对应的图像，并选择了 'bilinear' 的插值方式。
    # imshow() 中使用 'bilinear' 插值方式会使图像变得更加平滑和清晰。
    plt.figure(dpi=128, figsize=(10, 6))
    plt.imshow(wc1, interpolation='bilinear')
    plt.title('2011~2023年福建省所有城市的天气词云图', fontsize=24)
    plt.axis("off")
    '''保存图片'''
    filename = '2011~2023年福建省所有城市的天气词云图.png'
    plt.savefig(filename)
    plt.show()


if __name__ == '__main__':
    file = 'weather.csv'
    weather: pd.DataFrame = pd.read_csv(file, encoding='ANSI')

    # 数据处理
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    # 分离date数据 年、月
    weather['year'] = weather['date'].map(lambda x: str(x).split('/')[0])
    weather['month'] = weather['date'].map(lambda x: str(x)[5:7])
    weather['month'] = weather['month'].map(lambda x: str(x).split('/')[0])
    # 填充缺失值
    weather['high'].fillna(weather['high'].mean(), inplace=True)
    weather['low'].fillna(weather['low'].mean(), inplace=True)
    print(weather.dtypes)
    # 第一张图：2011~2023年厦门市每月最高最低温分布图
    pic_plot_fill()
    # # 第二张图：2018~2022年厦门市全年气温对比图
    pic_plot()
    # # 第三张图：2011~2023年厦门市气候分布饼图
    pic_pie_weather()
    # # 第四张图：2011~2023年厦门市风向分布饼图
    pic_pie_wind()
    # # 第五张图: 2022年福建省地级市气温对比柱状图
    pic_hist()
    # 第六张图:2011~2023年福建省所有城市的天气词云图
    pic_wordCloud()
