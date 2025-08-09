from fastmcp import FastMCP
from spider2Database import getGoods


server=FastMCP(name="first_mcp_server",
               description="a simple mcp server can read data from database")
import fastmcp.server

import pymysql
import asyncio
import spider2Database as sd

@server.tool()
async def select_from_db(sql:str)->list:
    '''
    数据库查询工具
    从数据库中获取数据
    :param sql: 查询语句
    :return: 查询结果
    '''
    conn=pymysql.connect(host='192.168.31.11',user='root',password='123456',db='spiderTest',port=3310,charset='utf8')
    cur=conn.cursor()
    cur.execute(sql)
    result=cur.fetchall()
    cur.close()
    conn.close()
    return result

@server.tool()
async def get_gooFish_data_2_db(pages:int,cookie:str,goods_name:str)->list:
    '''
    爬取商品数据并保存到数据库
    :param pages: 爬取页数
    :param cookie: 商品页面cookie
    :param goods_name: 商品名称
    '''
    goods_list=sd.getGoods(pages,cookie,goods_name)
    sd.data2db(goods_list)
@server.tool()
async def get_cookie_from_browser(url:str)->str:
    '''
    获取cookie工具,模拟浏览器操作打开页面获取cookie
    :param url: 商品页面url
    :return: cookie
    '''
    cookie=sd.get_cookies()
    return cookie

'''
@mcp.Tool()
async def get_gooFish_data_2_db(pages:int,cookie:str,goods_name:str)->list:
    goods=getGoods(pages,cookie,goods_name)
    for good in goods:
        pass
'''

if __name__=="__main__":
    #server.run(transport="stdio")
    server.run(transport="streamable-http",host="0.0.0.0",port=5000)
    #server.run(transport="sse",host="0.0.0.0",port=5000)