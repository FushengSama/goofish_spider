import logging

import requests
import time
import hashlib
from openpyxl import Workbook

# 1.仅作学习交流用途：本爬虫程序仅供个人学习 Python 编程、网络数据抓取技术以及对网页结构解析等相关知识的实践练习，严禁将其用于任何商业用途、非法用途或侵犯他人合法权益的行为。使用者应仅在自身学习环境内进行测试与实验，不得将该程序及相关技术应用于实际商业运营、数据交易或其他可能产生经济利益的活动中。
# 2.遵守网站规则：爬虫在运行过程中严格遵守闲鱼网站所设定的 robots.txt 协议，仅对协议允许抓取的页面及数据进行访问与提取。不会通过任何技术手段绕过闲鱼网站所设置的反爬机制，如暴力破解验证码、伪造请求头、频繁更换 IP 地址等方式来突破网站限制。对于闲鱼明确禁止爬虫访问的区域和数据类型，爬虫程序绝对不会进行尝试访问与获取。
# 3.不涉及隐私及敏感数据：爬虫程序仅抓取闲鱼平台公开展示的商品链接信息，不会获取任何涉及用户隐私的数据，如用户姓名、联系方式、身份证号、地址等，也不会获取闲鱼平台内部的敏感数据，如用户的交易记录详情、平台运营数据、未公开的商业策略等。所有抓取的数据仅以商品链接为核心，不包含任何可能侵犯用户隐私或平台商业利益的敏感内容。
# 4.不承担使用后果：本爬虫程序发布者对于任何第三方因使用该爬虫程序而产生的一切法律纠纷、责任和后果不承担任何责任。若使用者违反法律法规、闲鱼平台规定或本声明中的相关条款，导致自身或他人遭受损失、受到法律制裁，均由使用者自行承担全部责任。发布者已明确告知本程序的使用范围与限制，对于使用者超出合理合法范围使用程序所引发的一切问题概不负责。
# 5.责任自负：使用者在决定使用本爬虫程序之前，应充分了解相关法律法规以及使用该程序可能存在的风险，并确保自身的使用行为符合法律规定和道德准则。若因使用本程序而导致任何法律问题或其他不良后果，使用者需自行承担全部责任，包括但不限于可能面临的民事赔偿、行政处罚甚至刑事处罚。发布者不承担任何因使用者不当使用而引发的连带责任。

# 输入cookie
#cookie = input("请输入你的cookie值: ")





class spiderConfig:
    def __init__(self,token,goodsName):
        self.token = token
        self.goodsName=goodsName
        self.size=None
        self.isRange=False
        self.min=None
        self.max=None
    def addsize(self,size:str):
        self.size=size.split(" ")
    def setRange(self,isRange:bool,min:int=None,max:int=None):
        self.isRange=isRange
        self.min=min if min != "" else None
        self.max=max if max != "" else None

cookie="_m_h5_tk_enc=c10eab48d75e2b0f11a02300029695b3;xlly_s=1;sgcookie=E100E%2FpyDfZHPNo9%2FDKPGnJR4klbDBDH4VcycvmZ5uNBXLiGYpgh1pRJarSQLN66rKy%2FRzaFGnLzTAgDqxSus7Wo2LLiAvOAvQiyzueW5bS72kw%3D;_tb_token_=e639a308eaeb5;t=630549d4a3155233f811f79174530aa0;_m_h5_tk=0076b0c58351bd91c4297adf5edb6994_1747477033804;_samesite_flag_=true;cna=dLr7H+iY8R8CAbf3CTLIDAhh;cookie2=13ef56daea6d6d6a283c81e6617f3ca3;isg=BH19D5m7ybRrlGIEYwpto3eljNl3GrFsHleWqT_DMFQDdpyoB2qZPJtlIKowdskk;tracknick=tb454737635"
cookie=input("请输入你的cookie值: ")
m_h5_tk_start = cookie.find("_m_h5_tk=") + len("_m_h5_tk=")
m_h5_tk_end = cookie.find(";", m_h5_tk_start)
m_h5_tk_value = cookie[m_h5_tk_start:m_h5_tk_end]
token = m_h5_tk_value.split('_')[0]
#token="0076b0c58351bd91c4297adf5edb6994"
print("=" * 60)





while type:
    ss = input("请输入你要爬取的商品:")
    if ss == "quit":
        break
    config = spiderConfig(token, ss)
    if input("是否输入尺码？(y/n)") == "y":
        config.addsize(input("请输入你要爬取的尺码(多个尺码用空格分隔): "))

    if input("是否输入价格范围？(y/n)") == "y":
        min = input("请输入你要爬取的价格范围的最小值 ")
        max = input("请输入你要爬取的价格范围的最大值 ")
        config.setRange(True, min, max)


    yeshu = input("请输入你要爬取的页数:")


    def GetSign(page,config:spiderConfig):
        # 使用提取的_m_h5_tk的值作为d_token
        isRange=config.isRange
        min=config.min
        max=config.max






        d_token = config.token
        j = time1 = int(time.time() * 1000)
        h = "34839810"
        #page=2
        #j="1747466238486"
        propValueStr=f'"searchFilter":"priceRange:{ min if min else "undefined" },{ max if max else "undefined" };"'
        if not isRange:
            c_data = f'{{"pageNumber":{page},"keyword":"{ss}","fromFilter":false,"rowsPerPage":30,"sortValue":"","sortField":"","customDistance":"","gps":"","propValueStr":"","customGps":"","searchReqFromPage":"pcSearch","extraFilterValue":"","userPositionJson":""}}'

        else    :
            c_data = f'{{"pageNumber":{page},"keyword":"{ss}","fromFilter":true,"rowsPerPage":30,"sortValue":"","sortField":"","customDistance":"","gps":"","propValueStr":' + "{" + propValueStr + "}" + ',"customGps":"","searchReqFromPage":"pcSearch","extraFilterValue":"{}","userPositionJson":"{}"}'
        string = d_token + "&" + str(time1) + "&" + h + "&" + c_data
        MD5 = hashlib.md5()
        MD5.update(string.encode("utf-8"))
        sign = MD5.hexdigest()
        print(sign)
        return sign, j, c_data




    # 创建 Excel 工作簿
    wb = Workbook()
    # 获取活动工作表
    ws = wb.active
    # 添加表头
    if config.size!= None:
        ws.append(["用户名字", "简介", "链接", "价格", "地区", "尺码"])
    else:
        ws.append(["用户名字", "简介", "链接", "价格", "地区"])
    try:
        a=''
        for page in range(1, int(yeshu) + 1):
            sign, j, c_data = GetSign(page,config)
            print(f"正在爬取第{page}页")
            headers = {
                "cookie": cookie,  # 使用输入的cookie
                "origin": "https://www.goofish.com",
                "referer": "https://www.goofish.com/",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
            }

            url = "https://h5api.m.goofish.com/h5/mtop.taobao.idlemtopsearch.pc.search/1.0/"
            data = {
                "data": c_data
            }
            params = {
                "jsv": "2.7.2",
                "appKey": "34839810",
                "t": j,
                "sign": sign,
                "v": "1.0",
                "type": "originaljson",
                "accountSite": "xianyu",
                "dataType": "json",
                "timeout": "20000",
                "api": "mtop.taobao.idlemtopsearch.pc.search",
                "sessionOption": "AutoLoginOnly",
                "spm_cnt": "a21ybx.search.0.0",
                "spm_pre": "a21ybx.home.searchSuggest.1.4c053da64Wswaf",
                "log_id": "4c053da64Wswaf"
            }
            response = requests.post(url, headers=headers, params=params, data=data)
            a=html_data = response.json()
            #print(html_data)
            lis = html_data["data"]["resultList"]
            if len(lis) == 0:
                #    print("没有数据了")
                print("爬取完成")
                break
            for i in lis:
                title = i["data"]["item"]["main"]["exContent"]["title"].strip()
                diqu = i["data"]["item"]["main"]["exContent"]["area"].strip()
                fishTags=i["data"]["item"]["main"]["exContent"]["fishTags"]
                chima=""
                if config.size!= None:

                    try:
                        r2=fishTags['r2']['tagList'][0]
                        if r2['data']['content'] not in config.size:

                            continue
                        else:
                            chima=r2['data']['content']
                            print(r2['data']['content'])
                    except:
                        continue

                try:
                    naem = i["data"]["item"]["main"]["exContent"]["userNickName"].strip()
                except:
                    naem = "未知(新用户未命名名字)"
                try:
                    youfei = i["data"]["item"]["main"]["clickParam"]["args"]["tagname"]
                except:
                    youfei = "不包邮"
                jianjei = str(youfei) + "+" * 5 + title
                id = i["data"]["item"]["main"]["exContent"]["itemId"]
                lianjei = f"https://www.goofish.com/item?spm=a21ybx.search.searchFeedList.1.570344f71nqzll&id={id}&categoryId=126854525"
                jiage = i["data"]["item"]["main"]["clickParam"]["args"]["price"]
                print("-" * 60)
                if config.size == None:
                    print("用户名字:", naem, "\n", "简介:", jianjei, "\n", "链接:", lianjei, "\n", "价格:", jiage, "\n",
                          "地区:", diqu)
                    ws.append([naem, jianjei, lianjei, jiage, diqu])
                else:
                    print("用户名字:", naem, "\n", "简介:", jianjei, "\n", "链接:", lianjei, "\n", "价格:", jiage, "\n",
                          "地区:", diqu, "\n", "尺码:", chima)
                    ws.append([naem, jianjei, lianjei, jiage, diqu,chima])
                print("-" * 60)

                # 将数据写入 Excel 工作表

            time.sleep(1.61)

        wb.save(f'{ss}.xlsx')

    except Exception as e:
        # 保存 Excel 文件
        print(a)
        print(e)
        wb.save(f'../result/{ss}.xlsx')