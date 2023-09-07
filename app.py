import sys
sys.path.insert(0, './src')

from tkinter import Tk

from image_viewer import ImageViewer

root = Tk()
root.title("Intelligent Scissor")
root.geometry("1920x1080")
ImageViewer(root)
root.mainloop()