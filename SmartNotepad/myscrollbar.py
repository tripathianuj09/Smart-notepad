import tkinter
import tkinter.ttk
def show(event=None):
    print("Close Clicked")

root=tkinter.Tk()
root.geometry('400x300')
my_text=tkinter.Text(root)
my_text.config(wrap='word',relief=tkinter.FLAT)
my_scroll_bar=tkinter.ttk.Scrollbar(root)
my_scroll_bar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
my_text.pack(fill=tkinter.BOTH,expand=True)
my_scroll_bar.config(command=my_text.yview)
my_text.config(yscrollcommand=my_scroll_bar.set)
root.protocol("WM_DELETE_WINDOW",show)
root.mainloop()
