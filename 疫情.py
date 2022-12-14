import requests
from data import fname

name = input('请输入保存文件时的名字（相对路径，不加文件后缀）：')#'data'
url = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=localCityNCOVDataList,diseaseh5Shelf'
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"
}
data = {
    "modules": "localCityNCOVDataList,diseaseh5Shelf"
}
responer = requests.post(url=url, headers=head, params=data)
data = responer.json()["data"]["localCityNCOVDataList"]#处理获取到国内疫情的json数据

fname('{}.css'.format(name))#调用data.py里的函数创建css文件

f = open('{}.html'.format(name), 'w', encoding="utf-8")#创建HTML文件，制作html文件head半部分
f.write("""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>最新疫情</title>
    <link href="{}.css" rel="stylesheet">
</head>
<body>
<h2 class="text-center">最新全国疫情</h2>
<table class="table table-striped table-hover mx-auto text-center">
    <thead>
        <tr>
            <th>城市</th>
            <th>本土新增</th>
            <th>本土无症状</th>
            <th>高|中风险地区</th>
            <th>数据更新时间</th>
        </tr>
    </thead>
    <tbody>
""".format(name))
for i in range(len(data)):#使用for循环写入疫情数据文本
    city =data[i]["province"] +"\t"+ data[i]["city"]
    # print("城市:"+city)
    mtime = data[i]["mtime"]
    # print("数据更新时间:"+mtime)
    local_confirm_add = str(data[i]['local_confirm_add'])
    # print('本土新增:'+local_confirm_add)
    local_wzz_add = str(data[i]['local_wzz_add'])
    # print('本土无症状:'+local_wzz_add)
    RiskAreaNum = str(data[i]['highRiskAreaNum'])+" | "+str(data[i]['mediumRiskAreaNum'])
    # print('高|中风险地区：'+RiskAreaNum)
    citys = data[i]["province"]
    # print(data[i])
    # print('\n')
    f.write("""
            <tr>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
            </tr>
        """.format(city, local_confirm_add, local_wzz_add, RiskAreaNum, mtime))
f.write("""
         </tbody>
    </table>
    </body>
    </html>
    """)
f.close()#关闭文本
def path(file1,file2):
    import os
    path = "文件放到了："+"\n"+os.path.abspath(file1)+"\n"+os.path.abspath(file2)
    print(path)
path('{}.html'.format(name),'{}.css'.format(name))
