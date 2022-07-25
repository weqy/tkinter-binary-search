import tkinter as tk
from tkinter import *

root = tk.Tk()

canvas1 = tk.Canvas(root, width=600, height=400)
canvas1.pack()


def binary_search(arr, low, high, x):
	if high >= low:
		mid = (high + low) // 2
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)
		else:
			return binary_search(arr, mid + 1, high, x)

	else:
		return -1
arr = [ 2, 3, 4, 10, 40 ]
x = 10
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
	binary = ("Element is present at index", str(result))
else:
	binary = ("Element is not present in array")

label1 = tk.Label(root, text=binary, font=("Courier", 15))
canvas1.create_window(300, 200, window=label1)

root.mainloop()
