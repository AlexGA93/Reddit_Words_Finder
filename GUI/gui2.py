
import tkinter as tk

bg_app="#3700B3"
fg_app='white'

def close_window(): 
    root.destroy()

def methods():
    print(type(e1.get()))
    print(type(e2.get()))
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)

    


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Reddit Searcher')
    root.configure(bg= bg_app)
    root.geometry("400x350")
    root.resizable(False, False)

    tk.Label(root, text="Reddit Searcher: ",
             fg=fg_app, font=("Times", 20), bg='black').pack(fill=tk.BOTH)
    #########################################################################

    tk.Label(root, text="Words to search: ",
             font=("Times", 13),bg= bg_app, fg=fg_app).place(x=20, y=90)
    tk.Label(root, text="Subreddits to search: ",
             font=("Times", 13),bg= bg_app, fg=fg_app).place(x=20, y=150)

    e1=tk.Entry(root, font=("Times", 13))
    e1.place(x=170, y=90)

    e2=tk.Entry(root, font=("Times", 13))
    e2.place(x=170, y=150)

    tk.Button(root, text="Bye", fg='red',width='10',command=close_window).place(x=20, y=300)
    tk.Button(root, text="Search", fg='blue',width='10',command= methods).place(x=300, y=300)

    tk.Label(root, text="Copyright (C) 2019 Alejandro Gimeno Ataz", font=("Times",10),bg= bg_app, fg=fg_app).place(x=80, y=330)


    root.mainloop()
    tk.mainloop()
