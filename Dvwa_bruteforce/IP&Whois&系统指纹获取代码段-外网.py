import socket,os,time,sys
import base64
#from whois import whois

#ip查询
def ip_check(url):
    ip=socket.gethostbyname(url)#通过IP反查域名
    print(ip)

#whois查询
def whois_check(url):
    data=whois(url)
    print(data)

#CDN判断-利用返回ip条数进行判断
def cnd_check(url):
    ns="nslookup"+url#linux和windows都是这个命令
    #data=
    os.system(ns)#这样打出来的含有汉字，不是纯数据
#端口扫描
#1.原生自写socket协议tcp,udp扫描
#2.调用第三方模块扫描
#3.调用系统脚本执行
# ports={'21','22','135','443','445','80','1433','3306','3389'}
# for port in ports:
#     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     result=server.connect_ex(('47.75.212.155',int(port))#netstat -ano看端口开启情况，常见端口
#     if result==0:
#         print(port+'|open')
#     else:
#         print(port 'down')
# #whois查询，第三方模块
#     data={"whois8"}
# #
# from
import base64
import requests
headers={
    'cookie':'fofapro_ars_session=xxxx',
}
search_data='"glassfish"&&port="4848"'
for yeshu in range(1,11):
    url='https://fofa.so/result?page='+str(yeshu)+'&qbase64='
    search_data_bs=str(base64.b64encode(search_data.encode("utf-8")),"utf-8")
    urls=url+search_data_bs
    print(urls)
    result=requests.get(urls,headers=headers).content
    print(result.decode('utf-8'))
    soup=etree.HTML(result)
    ip_data=soup.xpath('//div[@class="re-domain"] /a[@target="_blank"]/@href')
    ipdata='\n'.join(ip_data)#返回的是一个列表对象，通过join方法，分隔。
    with open(r'ip.txt','a+') as f:
        print(ip_data)