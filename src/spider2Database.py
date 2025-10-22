import logging
import requests
import time
import hashlib
from openpyxl import Workbook
from dataclass.goods import goods
from dataclass.goods import sqlGoods
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import Table
from sqlalchemy import create_engine
import os
import dbs
import ultils.get_goofish_cookies as get_cookies
import yaml
def get_token(cookie:str)->str:
    
    m_h5_tk_start = cookie.find("_m_h5_tk=") + len("_m_h5_tk=")
    m_h5_tk_end = cookie.find(";", m_h5_tk_start)
    m_h5_tk_value = cookie[m_h5_tk_start:m_h5_tk_end]
    token = m_h5_tk_value.split('_')[0]
    return  token



class spiderConfig:
    def __init__(self,token,goodsName):
        self.token = token
        self.goodsName=goodsName
        self.size=None
        self.isRange=False
        self.min=None
        self.max=None
        
        
    def addsize(self,size:str):
        self.size=size.split("|")
    def setRange(self,isRange:bool,min:int=None,max:int=None):
        self.isRange=isRange
        self.min=min if min != "" else None
        self.max=max if max != "" else None


class spiderTaskConfig:
    def __init__(self,cookie:str,goodsName:str,page:int=10,is_save2xls:bool=True,is_save2db:bool=None,sleeptime:float=1.25):
        self.cookie=cookie
        self.goodsName=goodsName
        self.size=None
        self.isRange=False
        self.min=None
        self.max=None
        self.is_save2xls=is_save2xls
        self.is_save2db=is_save2db
        self.page=page
        self.sleeptime=sleeptime
        
        
    def addsize(self,size:str):
        self.size=size.split("|")
    def setRange(self,isRange:bool,min:int=None,max:int=None):
        self.isRange=isRange
        self.min=min if min != "" else None
        self.max=max if max != "" else None

def getGoods(pages:int,cookie:str,goodsName:str,size:str=None,price_range:tuple=None,is_save_to_xls:bool=False):
    token=get_token(cookie)
    prjPath=os.getcwd()

    ss = goodsName
    
    config = spiderConfig(token, ss)
    if  size:
        config.addsize(size)


    if price_range:
        min = price_range[0]
        max = price_range[1]
        config.setRange(True, min, max)


    yeshu = pages


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



    if is_save_to_xls:
    # 创建 Excel 工作簿
        wb = Workbook()
    # 获取活动工作表
        wb1 = wb.active
        #添加表头
        if config.size!= None:
            wb1.append(["用户名字", "简介", "链接", "价格", "地区", "尺码"])
        else:
            wb1.append(["用户名字", "简介", "链接", "价格", "地区"])



    try:
        ws=[]
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
                    user_name = i["data"]["item"]["main"]["exContent"]["userNickName"].strip()
                except:
                    user_name = "未知(新用户未命名名字)"
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
                    print("用户名字:", user_name, "\n", "简介:", jianjei, "\n", "链接:", lianjei, "\n", "价格:", jiage, "\n",
                          "地区:", diqu)
                    #ws.append([user_name, jianjei, lianjei, jiage, diqu])
                    ws.append(k:=goods(user_name,jianjei,diqu,category=config.goodsName,link=lianjei,price=jiage))
                    if is_save_to_xls:
                        
                        wb1.append([k.user_name,k.instruction,k.link,k.price,k.location])
                else:
                    print("用户名字:", user_name, "\n", "简介:", jianjei, "\n", "链接:", lianjei, "\n", "价格:", jiage, "\n",
                          "地区:", diqu, "\n", "尺码:", chima)
                    #ws.append([user_name, jianjei, lianjei, jiage, diqu,chima])
                    ws.append(k:=goods(user_name,jianjei,diqu,category=config.goodsName,link=lianjei,price=jiage,size=chima))
                    if is_save_to_xls:
                        wb1.append([k.user_name,k.instruction,k.link,k.price,k.location,k.size])
                print("-" * 60)

                # 将数据写入 Excel 工作表

            time.sleep(1.61)
        if is_save_to_xls:
            wb.save(prjPath+'/result'+f"/{ss}.xlsx")
        #wb.save(f'{ss}.xlsx')
        return ws

    except Exception as e:
        # 保存 Excel 文件
        #print(a)
        print(e)
        #wb.save(f'{ss}.xlsx')
        if is_save:
            wb.save(prjPath+'/result'+f"/{ss}.xlsx")
        return ws

def data2db(goodsList:list)->None:
    # 创建数据库连接
    engine=dbs.sqlEngine
    
    # 创建会话
    Session = sessionmaker(bind=engine)
    session = Session()
    for good in goodsList:
        # 创建新对象
        new_good = sqlGoods(uuid=good.uuid,
                            price=good.price, 
                            category=good.category,
                            location=good.location, 
                            user_name=good.user_name, 
                            instruction=good.instruction,
                            link=good.link,
                            )
        # 添加到数据库
        session.add(new_good)
    #提交
    session.commit()
    # 关闭会话
    session.close()


import argparse



def start_with_config(config:spiderTaskConfig)->None:
    _range=None
    if(config.isRange):
        _range=(config.min,config.max)
    lists=getGoods(config.page,
                   config.cookie,
                   config.goodsName,
                   size=config.size,
                   price_range=_range,
                   is_save_to_xls=config.is_save2xls)
    if(config.is_save2db):
        data2db(lists)






def getConfigFromYaml(path:str)->spiderTaskConfig:
    _path=os.path.abspath(path)
    s={}
    with open(_path,'r',encoding="utf-8") as configFile:
        s1=yaml.safe_load(configFile)
        print(s)
        s=s1["spiderConfig"]
        



        _config=spiderTaskConfig(
            cookie=s["cookie"],
            goodsName=s["goods_name"],
            page=s["pages"],
            is_save2db=s["is_save_to_db"],
            is_save2xls=s["is_save_to_excel"]
            )
        if(s["is_need_size"]):
            _config.addsize(s["size"])
        if(s["is_need_price_range"]):
            _config.setRange(s["min_price"],s["max_price"])
        if("sleeptime" in s):
            _config.sleeptime=s["sleeptime"]
        return _config


if __name__=="__main__":
   config=getConfigFromYaml("./config.yaml")
   config.sleeptime=1.3
   start_with_config(config)
"""
    co=r"_m_h5_tk_enc=c9b522a1794fcbc5191764e485359258;sdkSilent=1754801600652;xlly_s=1;tfstk=gJbsQ298OAD_GKSJfEPEP6_CQf8fcWzrhjOAZs3ZMFLtHxCJLOJw7S4XHOvF7d5wWrOAU96Xm5v2HK6VMGPUzz5GsEYvl8zzzA6ivY_6Hx8vSeENhU6_zz5G6fRTa6UPumRPlIJvkhKv92pHaqHAHhLpJpADMAdxWW1pKpd9MILxp6dMam3OHEFC9pAvkCBvDW1pKILvHjZtNIZ6I1N5RtIqk-9A6pgxkwUDfL1t0q3ARCt1k1pC_17B1h9JxGTd6NBFMN7Mxln6o6S5hiBLRV6f6gBvQwe-lKSlS6QebbgW7OjpVNWauR5CldtRWHGoyF1HMtKfx8gy1FSBVNsgivCOUdsJSsl7Q6t5A3Apvji97g5Po3QT5YveqI6WNOM14x0yF9fEcXtolB9zOWimmmoGfNJnwbGDXBA6YWNIBix9tB9zOWimmhdH1pPQOAIc.;havana_lgc2_77=eyJoaWQiOjIyMDU4NjU1MTc1NTIsInNnIjoiYzkyNDllNjQwZjQ1NDYxODk0MjAwN2RkMzJjZWZmMmQiLCJzaXRlIjo3NywidG9rZW4iOiIxbHJQT0poNC1FaXVJOXl4dENKbjdRQSJ9;sgcookie=E100Q08HRlUV7FeKQOO9JqeWQdvOZeNFpVbawVd1LNNRCLj80otL6l8xTmofQbqcb%2BHWFPLBMokKuAgKExzHNriTjYLV8owUCGVvmDha6xifJ8WmM8euq%2B8ayey%2FRvD280nk;_tb_token_=e073537ae93e3;havana_lgc_exp=1757227924979;t=630549d4a3155233f811f79174530aa0;_hvn_lgc_=77;_m_h5_tk=cb86332b75474b5d5ca0e45e5a844d92_1754724918677;_samesite_flag_=true;cna=dLr7H+iY8R8CAbf3CTLIDAhh;cookie2=26a0eca1202ced5a2df4401f1c3a1182;csg=a97b503d;isg=BPLyLl1xziUXUv1FIEMKssQ8QzjUg_YdjZ5pqLzLr6WQT5NJpBAAL7fsO-tzP261;tracknick=tb454737635;unb=2205865517552"
    #co=get_cookies.get_cookies("https://www.goofish.com/")
    print(co)
    a=getGoods(30,co,"RTX5070",price_range=(4000,5000),is_save_to_xls=True)
    #print(a)
    #data2db(a)
    k="11"  
"""