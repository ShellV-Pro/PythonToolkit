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
	wf = raw_input("������Ҫ�����ļ�������:")
	wf = str(wf)
	m = open(wf, 'w+')
	m.writelines(list)
	m.close()
	print "[+]������"
def dec():
	list = []
	global c
	for line in open(c):
		line = base64.b64decode(line)
		list.append(line)
		list.append("\n")
	wf = raw_input("������Ҫ�����ļ�������:")
	wf = str(wf)
	m = open(wf, 'w+')
	m.writelines(list)
	m.close()
	print "[+]������"
#ȫ�ֱ���
rom_list = []
print "base64\n"
print " a Base64 ����\n b Base64 ����"
print "���ж�ȡ���ص��ļ�\n"
f = raw_input("��ѡ��ʽ(a/b)")
f = str(f)
c = raw_input("�������ļ���(ͬĿ¼��):")
c = str(c)
if(f == "a"):
	enc()
if(f == "b"):
	dec()