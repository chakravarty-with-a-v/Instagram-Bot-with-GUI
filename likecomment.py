from tkinter import *


class LikeComment:
    def __init__(self, window, BOT):
        self.comment_window = window
        self.comment_window.title('COMMENTS')
        self.comment_window.geometry('400x100')
        self.BOT = BOT
        # COMMENT AND NUMBER OF POSTS LABEL
        comment_label = Label(self.comment_window, text='Comment :')
        comment_label.grid(row=0, column=0)
        post_number = Label(self.comment_window, text='Enter Number of Posts you want to interact with')
        post_number.grid(row=1, column=0)
        # ENTRY LABELS FOR COMMENTS AND LIKE
        self.comment_entry = Entry(self.comment_window, width=20)
        self.number_entry = Entry(self.comment_window, width=20)
        self.comment_entry.grid(row=0, column=1)
        self.number_entry.grid(row=1, column=1)
        button = Button(self.comment_window, text='START LIKING', command=self.comment_input)
        button.grid(row=2, column=0)
        self.comment_window.mainloop()

    def comment_input(self):
        self.BOT.comment = self.comment_entry.get()
        self.BOT.number = self.number_entry.get()
        self.comment_entry.delete(0, END)
        self.number_entry.delete(0, END)
        self.BOT.like_comment()
