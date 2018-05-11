# coding: utf-8

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

# リニアサーチ
def linear_search(list,target):

	print("演習３")
	count = 0
	for i in range(len(list)):
		print("番号:{0} 名前:{1} 住所:{2}".format(list[i].no,list[i].name,list[i].addr))
	
	for i in range(len(list)):
		count += 1
		if list[i].no == target:
			#print("検索回数:{0}".format(count))
			return [list[i].name,list[i].addr,count]

# バイナリサーチ
def binary_search(list,target):
	
	print("演習４")
	for i in range(len(list)):
		print("番号:{0} 名前:{1} 住所:{2}".format(list[i].no,list[i].name,list[i].addr))
	
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
	
# 演習２
exe2()

# 演習３
exe3()

# 演習４
exe4()

