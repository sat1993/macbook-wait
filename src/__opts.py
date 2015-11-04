# -*- coding: utf-8 -*-
# coding=utf-8
import sys
import getopt
"""
    __opts模块，负责获取命令行参数，并将参数赋值到map中，格式为对应参数的--长串key与对应的value。
    已经对一些命令直接进行返回。如--help
"""
__author__ = 'lixiaozhu'



class __opts:
    #先看看这个usage，看一下需求。我规划一下模块之后再开始写。
    def usage(self):
        print("Usage:")
        print '-h,--help:显示帮助信息'
        print '-m,--mode:search打开查询模式，将会读取配置文件的所有内容，建议与-g,--grep一起使用,tail:打开跟踪模式，将会对配置文件进行跟踪读取内容'
        print '-g,--grep:对即将显示的内容使用-g,--grep的参数进行筛选'
        print '-o,--output:将控制台输出的信息打印至文件中,与-s,--search配合使用将不打印至控制台，直接打印到文件中'
        print '--host:打印指定host服务器的配置file信息，可以与-f一起使用，可以配置多个host,需要使用,分隔，如果没有则以默认配置为准'
        print '--user:指定host的username,可以配置多个username，需要与-h对应，可以配置一个username，也可以对应host配置多个，需要以,分隔，如果没有则以默认配置为准'
        print '--pkey:指定Host的私钥地址，应对多个host可以配置一个与多个私钥地址，需要以,分隔，如果没有则以默认配置为准'
        print '--password:指定Host的用户密码，应对多个Host可以配置一个与多个密码，需要以,分隔，如果没有则以默认配置为准'
        print '--port，指定host的端口，可以对应多个host配置一个或者多个端口号，需要以,分隔，如果没有则以默认配置为准'
        print '-f,--file:替换配置信息中的log_file，改换跟踪文件'
    def __init__(self, param):
        try:
            self.opts, args = getopt.getopt(param, "hm:g:f:o:",
                                                 ['mode=', 'help', 'grep=', 'file=', 'host=', 'user=', 'pkey=',
                                                  'password=', 'port=', 'output='])
        except getopt.GetoptError, err:
            print str(err)
            self.usage()
            sys.exit(2)
        print self.opts,args
        for opt,value in self.opts:
            print opt,value
            if opt in ('-h', '--help'):
                self.usage()
                sys.exit(2)
    def getLogLook(self,log_look,hosts_file):
        log_look._host=hosts_file
        def putvalue(host,key,value):
            value=value.split(',')
            if(len(value)>len(host)):
                pass
            #####
            #####
            for index,v in enumerate(value):
                host[index][key]=v
        for opt,value in self.opts:
            if opt in ('-m','--mode'):
                log_look._mode=value
                continue
            if opt in ('-g','--grep'):
                log_look.is_grep=True
                continue
            if opt in ('-o','--output'):
                log_look.o_file=value
                continue
            if opt == '--host':

                continue
            if opt == '--user':
                value=value.split(',')
                for index,v in enumerate(value):
                    log_look._host[index]['username']=v
                continue
            if opt == '--pkey':
                value=value.split(',')
                for index,v in enumerate(value):
                    log_look._host[index]['private_key']=v
                continue
            if opt == '--password':
                value=value.split(',')
                for index,v in enumerate(value):
                    log_look._host[index]['password']=v
                continue
            if opt =='--port':
                value=value.split(',')
                for index,v in enumerate(value):
                    log_look._host[index]['port']=v
                continue
            if opt in ('--file','f'):
                value=value.split(',')
                for index,v in enumerate(value):
                    log_look._host[index]['log_file']=v
                continue
        print log_look._host
