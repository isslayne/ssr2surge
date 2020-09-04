#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import ssr_decode
import argparse
import os
import io
import json
import socket
from os.path import expanduser
import re
from urllib import request

url = ""
# default port
port = 19522
home = expanduser("~")
surgePath = "/Documents/Surge/config"
# surgePath = "D:/frontEnd/surge/surge_py"


def get_data(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    req = request.Request(url, headers=header)
    with request.urlopen(req) as res:
        data = str(res.read(), encoding="utf-8")
        return data


# 解码订阅内容获得配置保存在目录config

def del_files(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".json"):
                os.remove(os.path.join(root, name))


def save_config(url, port):
    data = get_data(url)
    ssr_str = ssr_decode.decode(data)

    code_list = re.findall(r"ssr://(\w+)", ssr_str)

    if not os.path.exists(home + surgePath + '/SSRJson'):
        os.makedirs(home + surgePath + '/SSRJson')

    writepath = home + surgePath + '/external.txt'
    mode = 'a' if os.path.exists(writepath) else 'w'
    f = io.open(writepath, mode, encoding='utf8')
    f.truncate()
    f.close()
    for code in code_list:
        index = code_list.index(code)
        try:
            #            print(code,index,port) #pass port
            ssr_decode.save_as_json(code, port, name=str(index))
        except UnicodeDecodeError:
            print(ssr_decode.decode(code))  # 打印有误的链接


def getIP(domain):
    try:
        myaddr = socket.gethostbyname(domain)
    except BaseException:
        myaddr = 'unknown'
    return myaddr

def genSurgeConfig(proxyNode, nodeList):
    # 读取配置文件，清空数据
    rootDir = home + "/Documents/Surge"
    f = io.open(home + surgePath + '/surge_ssr.conf', 'w+', encoding='utf8')
    f.truncate()
    f.close()

    with io.open(rootDir + '/snippets/common.conf', 'r', encoding='utf8') as commonConf:
        commonConfData = commonConf.read()
        surgeConf = io.open(home + surgePath + '/surge_ssr.conf', 'a', encoding='utf8')
        surgeConf.write(commonConfData + '\n\n' + proxyNode)
        surgeConf.close()

    proxyGroup = '\n[Proxy Group]\n\n'
    proxyGroup += 'Proxies = select,SG,HK,JP,US,TW,other\n'
    proxyGroup += 'Netflix = select,Proxies,SG,HK,JP,US,TW,other\n'
    proxyGroup += 'Disney = select,Proxies,SG,HK,JP,US,TW,other\n'
    proxyGroup += 'line-kk = select,Proxies,SG,HK,JP,US,TW,other\n'
    proxyGroup += 'Telegram = select,Proxies,SG,HK,JP,US,TW,other\n'
    proxyGroup += 'Youtube = select,Proxies,SG,HK,JP,US,TW,other\n'
    proxyGroup += 'Netease = select,DIRECT,Proxies\n'
    proxyGroup += 'HKMTMedia = select,DIRECT,Proxies,SG,HK,TW,other\n'
    proxyGroup += 'GlobalMedia = select,Proxies,DIRECT,SG,HK,JP,US,TW,other\n'
    proxyGroup += 'Apple = select,DIRECT,Proxies,SG,HK,JP,US,TW,other\n'
    proxyGroup += 'Final = select,Proxies,DIRECT\n'
    
    SG = 'select,'
    HK = 'select,'
    JP = 'select,'
    US = 'select,'
    TW = 'select,'
    other = 'select,'

    for remark in nodeList:
        if "深台" in remark  or "彰化" in remark  or "新北" in remark or "台" in remark :
            TW += remark + ','
        if "美" in remark  or "圣克拉拉" in remark  or "波特兰" in remark  or "洛杉矶" in remark  or "费利蒙" in remark  or "圣何塞" in remark or "达拉斯" in remark or "芝加哥" in remark or "凤凰城" in remark or "西雅图" in remark or "硅谷" in remark: 
            US += remark + ','
        if "狮城"  in remark or "新加坡" in remark  or "深新" in remark  or "沪新" in remark or "京新" in remark  or "singapore" in remark :
            SG += remark + ','
        if "港" in remark :
            HK += remark + ','
        if "日本" in remark  or "埼玉" in remark   or "东京" in remark or "大阪" in remark or "沪日" in remark or "深日" in remark or "川日" in remark :
            JP += remark + ','
        if "港" not in remark  and "深台" not in remark  and "彰化" not in remark  and "新北" not in remark and "台" not in remark and "狮城"  not in remark and "新加坡" not in remark and "深新" not in remark  and "沪新" not in remark and "京新" not in remark  and "singapore" not in remark and "美" not in remark  and "圣克拉拉" not in remark  and "波特兰" not in remark  and "洛杉矶" not in remark  and "费利蒙" not in remark  and "圣何塞" not in remark and "达拉斯" not in remark and "芝加哥" not in remark and "凤凰城" not in remark and "西雅图" not in remark and "硅谷" not in remark and "日本" not in remark  and "埼玉" not in remark   and "东京" not in remark and "大阪" not in remark and "沪日" not in remark and "深日" not in remark and "川日" not in remark :
            other += remark + ','

    proxyGroup += 'SG = ' + SG[:-1] + '\n'
    proxyGroup += 'HK = ' + HK[:-1] + '\n'
    proxyGroup += 'JP = ' + JP[:-1] + '\n'
    proxyGroup += 'US = ' + US[:-1] + '\n'
    proxyGroup += 'TW = ' + TW[:-1] + '\n'
    proxyGroup += 'other = ' + other[:-1] + '\n'
    
    with io.open(rootDir + '/snippets/rule.conf', 'r', encoding='utf8') as ruleConf:
        ruleConfData = ruleConf.read()
        surgeConf = io.open(home + surgePath + '/surge_ssr.conf', 'a', encoding='utf8')
        surgeConf.write(proxyGroup + '\n' + ruleConfData)
        surgeConf.close()

def configToExternal():
    rootdir = home + surgePath
    # f = open(home + surgePath + '/external.txt', 'w+')
    # rootdir = surgePath
    sysHome = expanduser("~")
    surgeSSRConfigPath = "/Documents/Surge/config"

    # 节点信息
    proxyNode = ''

    f = io.open(home + surgePath + '/external.txt', 'w+', encoding='utf8')
    f.truncate()
    f.close()
    for root, dirs, files in os.walk(rootdir + '/SSRJson'):  # 当前路径、子文件夹名称、文件列表
        for filename in files:
            if filename.endswith(".json"):
                fn = filename.replace('.json','')
#                print(fn)
                with io.open(rootdir + '/SSRJson' + '/' + filename, 'r', encoding='utf8') as f:
                    tmp = json.loads(f.read())
                    lp = tmp['local_port']
                    se = tmp['server']
                    serverIP = getIP(se)
#                    print(lp)
                    print(fn.replace('#', '*') + ' = external, exec = \"' + home + surgePath + '/ss-local\", args = \"-c\", args = \"' + rootdir + '/SSRJson' + '/' + filename + '\",' + 'local-port = ' + str(lp) + ', addresses = ' + serverIP)
                    proxyNode += fn.replace('#', '*') + ' = external, exec = \"' + home + surgePath + '/ss-local\", args = \"-c\", args = \"' + rootdir + '/SSRJson' + '/' + filename + '\",' + 'local-port = ' + str(lp) + ', addresses = ' + serverIP + '\n'
                    
                    f = io.open(rootdir + '/external.txt', 'a', encoding='utf8')
                    f.write(fn.replace('#', '*') + ' = external, exec = \"' + home + surgePath + '/ss-local\", args = \"-c\", args = \"' + rootdir + '/SSRJson' + '/' + filename + '\",' + 'local-port = ' + str(lp) + ', addresses = ' + serverIP + '\n')
                    f.close()
        nodeListStr = ''
        nodeList = []
        for filename in files:
            if filename.endswith(".json"):
                fn = filename.replace('.json','')
                nodeListStr = (nodeListStr + fn.replace('#', '*') + ',')
                nodeList.append(fn.replace('#', '*'))
        print(nodeListStr)
        genSurgeConfig(proxyNode, nodeList)
        f = io.open(rootdir + '/external.txt', 'a', encoding='utf8')
        f.write(nodeListStr)
        f.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", help="this is the ssr subscribe address")
    parser.add_argument("-p", help="this is the destined port number")
    # parser.add_argument("-p","--port",help="this is the destined port number")
    args = parser.parse_args()
#    print('________打印参数________')
#    print(args)
    if args.s:
        #        print(8,args.s)
        url = args.s
    if args.p:
        port = args.p

#    url = input("ssr subscrible link: ")
    # del_files(home + surgePath + '/SSRJson')
    del_files(home + surgePath + '/SSRJson')
    save_config(url, port)
    configToExternal()
#    print("successful!")
