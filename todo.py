from tkinter import *
from tkinter.ttk import *

root = Tk()

todo_list = []
btn_list = []


placement = 130
def display_tasks():
    global placement
    for i in range(len(todo_list)):
        btn_list.append(Button(root, text =todo_list[i], style = 'W.TButton', command=lambda: btn_list[i].destroy()))
        btn_list[i].place(x=50, y = placement)   
        placement+= 40



#todo
def add_task():
    global placement
    new_task = Entry(root)
    new_task.place(x = 170, y = 50, height = 25, width = 200)
    
    def sub():
        global placement
        todo_list.append(new_task.get())
        print (todo_list)
        btn = Button(root, text =new_task.get(), style = 'W.TButton',  command=lambda: btn.destroy())
        btn.place(x=50, y=placement)
        placement +=40
        
    submit = Button(root, text = "Submit", command = sub)
    submit.place(x=170, y=80)


# This will create style object
style = Style()
style.configure('W.TButton', font = ('Times New Roman', 12), foreground = 'black')

#defining button and placing it
add = Button(root, text ="Add Task", style = 'W.TButton', command = add_task)
add.place(x=50,y=50)

display_tasks()
root.geometry("500x300")
root.mainloop()

