# coding: utf-8

import hashlib

# 空クラス
class Hum():
	#def __init__(self,no,name,addr):
	#	#インスタンス変数
	#	self.no = 0
	#	self.name = ""
	#	self.addr = ""
	pass

def get_info(txt):
	man = []
	with open(txt, 'r') as f:
		line = f.readlines()
		#print(line)
	for i in range(len(line)):
		man.append(Hum())
		info = line[i].split(',')
		#print(info)
		man[i].no = int(info[0])
		man[i].name = info[1]
		man[i].addr = info[2]
	return man

def get_info_hash(txt):
	man = []
	for i in range(61):
		man.append("n")
	with open(txt, 'r') as f:
		line = f.readlines()
	for i in range(len(line)):
		info = line[i].split(',')
		index = get_index(info[1])
		man[index] = Hum()
		man[index].no = int(info[0])
		man[index].name = info[1]
		man[index].addr = info[2]
		#print(index)
	return man


# リニアサーチ
def linear_search(list,target):

	print("演習３")
	count = 0
	for i in range(len(list)):
		print("番号:{0} 名前:{1} 住所:{2}".format(list[i].no,list[i].name,list[i].addr[:-1]))

	for i in range(len(list)):
		count += 1
		if list[i].no == target:
			#print("検索回数:{0}".format(count))
			return [list[i].name,list[i].addr,count]

# バイナリサーチ
def binary_search(list,target):

	print("演習４")
	for i in range(len(list)):
		print("番号:{0} 名前:{1} 住所:{2}".format(list[i].no,list[i].name,list[i].addr[:-1]))

	count = 0
	low = 0
	high = len(list)-1

	while low <= high:
		count += 1
		center = (low + high) // 2
		if list[center].no == target:
			result = center
			return [list[center].name,list[center].addr,count]
			break
		elif list[center].no > target:
			high = center - 1
		else:
			low = center + 1

def get_index(e):
	index = hashlib.md5(e.encode('utf-8')).hexdigest()
	index =  int(index,16) % 61
	return index

def hash_search(list,target):
	index = get_index(target)
	if list[index] == "n":
		print("見つかりませんでした")
	else:
		print("番号:{0} 名前:{1} 住所:{2}".format(list[index].no,list[index].name,list[index].addr))


def exe2():
	man = get_info("info.txt")
	print("演習２")
	print(man[1].name)
	print("----------------------")

def exe3():
	man = get_info("data.txt")
	name,addr,count = linear_search(man,4)
	print("名前:{0} 住所:{1}   検索回数{2}".format(name,addr,count))
	print("----------------------")

def exe4():
	man = get_info("data2.txt")
	name,addr,count = binary_search(man,4)
	print("名前:{0} 住所:{1}   検索回数{2}".format(name,addr,count))

def exe7():
	man = get_info_hash("data.txt")
	hash_search(man,"山田 一郎")
	hash_search(man,"山田 太郎")


# 演習２
exe2()

# 演習３
exe3()

# 演習４
exe4()

# 演習７
exe7()
