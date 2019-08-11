import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import StringVar, IntVar

# font variables
font_app = 'Times'

font_size_Label = 26
foreground_Label = '#ffffff'
background_Label = '#000000'
font_size_text = 15
foreground_text = 'black'


# background
bg_app = bg_label = '#304ffe'  # '#303F9F'  # 'gray26'


# words section dimmensions
ipad_x1 = 100
ipad_y1 = 20

# subreddits sections dimmensions
ipad_x2 = 20
ipad_y2 = 20

ipad_x3 = 1
ipad_x4 = 1
ipad_y3 = 1
ipad_y4 = 30


def componentLabel(root):
    # Label
    stylelabel = ttk.Style()
    stylelabel.configure(
        'BW.TLabel', foreground=foreground_Label, background=background_Label)

    label = ttk.Label(root, text='Reddit Searcher', font=(
        font_app, font_size_Label), anchor='center', style="BW.TLabel")
    label.pack(fill=tk.BOTH)


def componentWords(root):
    # input 1

    # Frame words
    # ---------------------------------------------------------------
    style_entryWords = ttk.Style()
    style_entryWords.configure("Frame_Words.TFrame",
                               background='red')

    frameWordsLabel = ttk.Frame(root, style='Frame_Words.TFrame')
    frameWordsLabel.pack(ipadx=ipad_x1, ipady=ipad_y1)

    # ---------------------------------------------------------------

    # words
    styleLabelWords = ttk.Style()
    styleLabelWords.configure(
        "Words.TLabel", foreground=foreground_text, background=bg_label)

    labelWords = ttk.Label(frameWordsLabel, text="Enter words here ...",
                           style="Words.TLabel", font=(font_app, font_size_text))
    labelWords.pack()

    text_entry = StringVar()
    text_entry.set('')

    entryW = ttk.Entry(frameWordsLabel, textvariable=text_entry)
    entryW.pack()
    # ---------------------------------------------------------------


def componentSubreddits(root):
    # input 2
    ##########################################################################################
    # Frame Subreddits
    # ---------------------------------------------------------------
    style_entry = ttk.Style()
    style_entry.configure("Frame_Subreddits.TFrame",
                          background='blue')

    frameInputs = ttk.Frame(root, style='Frame_Subreddits.TFrame')
    frameInputs.pack(ipadx=ipad_x2, ipady=ipad_y2)
    # ---------------------------------------------------------------
    # Subreddits
    styleLabelSubreddits = ttk.Style()
    styleLabelSubreddits.configure(
        "Subreddits.TLabel", foreground=foreground_text, background=bg_label)

    labelWords = ttk.Label(frameInputs, text="Enter subreddits here ...",
                           style="Subreddits.TLabel", font=(font_app, font_size_text))
    labelWords.pack(side="left")

    text_entry = StringVar()
    text_entry.set('')

    entryW = ttk.Entry(frameInputs, textvariable=text_entry)
    entryW.pack(side="left")


def gui_frames(root):

    componentLabel(root)
    componentWords(root)
    # componentSubreddits(root)


def main():
    root = tk.Tk()
    # giving window's size
    root.minsize(width=500, height=500)
    # Window Title
    root.title('Reddit Searcher')
    # background
    root.configure(bg=bg_app)
    # calling methods
    gui_frames(root)

    root.mainloop()


if __name__ == "__main__":
    main()
