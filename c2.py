def read_file(filename):
	lines =[] 
	#讀取檔案
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	person = None #為避免第一行沒有Tom/Allen，所以利用python功能'None'
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_image_count = 0
	viki_image_count = 0
	for line in lines: #將聊天紀錄的每一條列出來
		 s = line.split(' ')#遇到空白鍵就切一刀，之後就會變成s清單裝東西
		 time = s[0]
		 name = s[1]
		 if name  == 'Allen':
		 	if s[2] == '貼圖':
		 		allen_sticker_count += 1
		 	elif s[2] == '圖片':
		 		allen_image_count += 1
		 	else:
		 		for m in s[2:] :
		 			allen_word_count += len(m) # len(m) 累加 allen_word_count
		 elif name == 'Viki':
		 	if s[2] == '貼圖':
		 		viki_sticker_count +=1
		 	elif s[2] == '圖片':
		 		viki_image_count += 1
		 	else:
		 		for m in s[2:]:
		 			viki_word_count += len(m)	
	print('Allen說了', allen_word_count,'個字')
	print('Allen傳了', allen_sticker_count,'個貼圖')
	print('Allen傳了',allen_image_count,'張圖片')

	print('Viki說了', viki_word_count)
	print('Viki傳了', viki_sticker_count,'個貼圖')
	print('Viki傳了',viki_image_count,'張圖片')

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n') #寫入檔案後，一定要換行符號

def main():
	line =[]
	lines = read_file('-LINE-Viki.txt')
	lines = convert(lines)
	# write_file('output.txt', lines) #寫入檔案要產生的檔案名

main()
