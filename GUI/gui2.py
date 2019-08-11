
import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Reddit Searcher')

    root.geometry("400x400")

    tk.Label(root, text="Reddit Searcher: ",
             fg='white', font=("Times", 20), bg='black').pack(fill=tk.BOTH)
    #########################################################################

    tk.Label(root, text="Words to search: ",
             font=("Times", 13)).place(x=20, y=90)
    tk.Entry(root, font=("Times", 13)).place(x=170, y=90)

    tk.Label(root, text="Subreddits to search: ",
             font=("Times", 13)).place(x=20, y=150)
    tk.Entry(root, font=("Times", 13)).place(x=170, y=150)

    tk. Button(root, text="Bye", fg='red').place(x=20, y=350)
    tk.Button(root, text="Search", fg='blue').place(x=320, y=350)

    root.mainloop()
