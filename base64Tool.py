# coding= utf-8  
# encoding= utf-8
# By: ShellV www.linux.dog 
# From AcgBagSecurityTeam (security.moe)
# Github https://github.com/ShellV-Pro/PythonToolkit
import base64
def enc():
	list = []
	global c
	for line in open(c):
		line = base64.b64encode(line)
		list.append(line)
		list.append("\n")
	wf = raw_input("请输入要创建文件的名字:")
	wf = str(wf)
	m = open(wf, 'w+')
	m.writelines(list)
	m.close()
	print "[+]输出完成"
def dec():
	list = []
	global c
	for line in open(c):
		line = base64.b64decode(line)
		list.append(line)
		list.append("\n")
	wf = raw_input("请输入要创建文件的名字:")
	wf = str(wf)
	m = open(wf, 'w+')
	m.writelines(list)
	m.close()
	print "[+]输出完成"
#全局变量
rom_list = []
print "base64\n"
print " a Base64 加密\n b Base64 解密"
print "逐行读取加载的文件\n"
f = raw_input("请选择方式(a/b)")
f = str(f)
c = raw_input("请输入文件名(同目录下):")
c = str(c)
if(f == "a"):
	enc()
if(f == "b"):
	dec()