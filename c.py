
def read_file(filename):
	lines =[] 
	#讀取檔案
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new =[]
	person = None #為避免第一行沒有Tome/Allen
	for line in lines: #將聊天紀錄的每一條列出來
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: #如果person有值，我們才啟動下面一行
			new.append(person + ':' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n') #寫入檔案後，一定要換行符號

def main():
	line =[]
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines) #寫入檔案要產生的檔案名
main()
