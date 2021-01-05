from tkinter import *

root = Tk()
root.geometry("500x80")
num1 = Entry(root, width = 20)
num2 = Entry(root, width = 20)
label1 = Label(root, width = 10, text = "Number 1: ")
label2 = Label(root, width = 10, text = 'Number 2: ')
num1.grid(row = 0, column = 1)
label1.grid(row = 0, column = 0)
label2.grid(row = 0, column = 2)
num2.grid(row = 0, column = 3)
global errLabel
def addNum():
	a = num1.get()
	if a == "":
		a = 0
	a = float(a)
	b = num2.get()
	if b == "":
		b= 0
	b = float(b)
	num2.delete(0, END)
	num1.delete(0, END)
	ans = a+b
	if int(ans) == float(ans):
		ans = int(ans)
	num1.insert(0, str(ans))

def subNum():
	a = num1.get()
	if a == "":
		a = 0
	a = float(a)
	b = num2.get()
	if b == "":
		b= 0
	b = float(b)
	num2.delete(0, END)
	num1.delete(0, END)
	ans = a-b
	if int(ans) == float(ans):
		ans = int(ans)
	num1.insert(0, str(ans))

def mulNum():
	a = num1.get()
	if a == "":
		a = 0
	a = float(a)
	b = num2.get()
	if b == "":
		b= 0
	b = float(b)
	num2.delete(0, END)
	num1.delete(0, END)
	ans = a*b
	if int(ans) == float(ans):
		ans = int(ans)
	num1.insert(0, str(ans))

def divNum():
	a = num1.get()
	if a == "":
		a = 0
	a = float(a)
	b = num2.get()
	if b == "":
		b= 0
	b = float(b)
	num2.delete(0, END)
	num1.delete(0, END)

	try:
		ans = a/b
		if int(ans) == float(ans):
			ans = int(ans)
		num1.insert(0, str(ans))
	except:
		errLabel = Label(root, fg = 'red', text= 'ERROR: DIVIDE BY ZERO')
		errLabel.grid(row = 2, column = 0, columnspan = 2)
def clrd():
	num1.delete(0,END)
	num2.delete(0,END)
	try:
		errLabel.destroy()
		errLabel = Label(root, fg = 'red', text= ' ')
		errLabel.grid(row = 2, column = 0, columnspan = 2)
	except:
		errLabel = Label(root, fg = 'red', text= '                                                       ')
		errLabel.grid(row = 2, column = 0, columnspan = 2)


def main():

	addButton = Button(root, text = '+', width = 9, bg = 'lightblue', command = addNum)
	addButton.grid(row = 1, column = 0, padx = 4, pady = 5)
	subButton = Button(root, text = '-', width = 9, bg = 'lightblue', command = subNum)
	subButton.grid(row = 1, column = 1, padx = 4, pady = 5)
	mulButton = Button(root, text = '*', width = 9, bg = 'lightblue', command = mulNum)
	mulButton.grid(row = 1, column = 2, padx = 4, pady = 5)
	divButton = Button(root, text = '/', width = 9, bg = 'lightblue', command = divNum)
	divButton.grid(row = 1, column = 3, padx = 4, pady = 5)
	clrButton = Button(root, text = 'Clear', width = 9, bg = '#FFCCCB', command = clrd)
	clrButton.grid(row = 1, column = 4, padx = 4, pady = 5)

	root.mainloop()

if __name__ == '__main__':
	main()