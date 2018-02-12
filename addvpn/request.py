#!/use/bin/env python
#coding=utf-8
import urllib2
import urllib


#构造文件头   -_-!!主要是cookie不太熟悉
def headerbuild(cookie):
	headers= {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
		'Cookie': cookie,
		'X-Requested-With': 'XMLHttpRequest',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'Referer': 'http://*****/zh_cn/web_content.html?js=local-user',
		'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
		'Accept': '*/*',
	}
	return headers


#发出请求
def StartRequest(method,url,post_values,cookies=None):
	#headers = dict()
	#get请求
	headers= headerbuild(cookies);
	if method.lower() == 'get':
		req = urllib2.Request(url = url,headers= headers)

	#post请求
	if method.lower()=='post':
		values = dict()
		if post_values:
			values_list = post_values.strip().split('&')
			for val in values_list:
				values[val.split('=')[0]] = val.split('=')[1]
		data = urllib.urlencode(values)
		req = urllib2.Request(url = url,data = data,headers = headers)
		response = urllib2.urlopen(req)
		message = response.read()
		print message


####################----------------------####################


#需要替换的内容
#cookie
cookies = '****'
#保存账号密码的文件
docname = 'user_pass.txt'
#时间注意格式
timeout = '****'


####################----------------------####################
#原始数据格式
realdata1 = 'isLocalUserNew=1&pwd={{pwd}}&pwd2={{pwd}}&userName={{username}}&pwdname={{pwd}}&pwd2name={{pwd}}&txtCellPhoneNum=请输入手机号&hidCellPhoneNum=&desc=&seledGroups=****&ike=none&timeOutEnable=1&timeOut={{timeout}}&groups='
realdata2 = 'userName={{username}}&addGroups=****&delGroups=&aaaServer=local'
#打开文件
with open(docname,'r') as user_pass:
	for line in user_pass:
		#注意分割符
		username = line.strip().split('/')[0]
		password = line.strip().split('/')[1]
		#替换
		data1 = realdata1.replace('{{timeout}}',timeout)
		data1 = data1.replace('{{username}}',username)
		data2 = realdata2.replace('{{username}}',username)
		data1 = data1.replace('{{pwd}}',password)
		#第一次请求添加用户，第二次添加用户组
		print '正在添加用户'+username
		StartRequest('post','http://****/zh_cn/user_ajax.html?s1=localUserCfg&t1=set&aaaServer=local',data1,cookies=cookies)
		print '正在将'+username+'添加进****用户组'
		StartRequest('post','http://****/zh_cn/user_ajax.html?s1=groupsForUser&t1=set',data2,cookies=cookies)