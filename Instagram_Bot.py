from bot import Bot
from tkinter import *
from tkinter import messagebox
from likecomment import LikeComment


def like():
    instabot.target = target_account_entry.get()
    if len(instabot.target) == 0:
        messagebox.showerror('ERROR', 'NO USERNAME SUPPLIED')
        return
    target_account_entry.delete(0, END)
    comment_window = Tk()
    comment_obj = LikeComment(comment_window, instabot)


def follow():
    instabot.target = target_account_entry.get()
    if len(instabot.target) == 0:
        messagebox.showerror('ERROR', 'NO USERNAME SUPPLIED')
        return
    instabot.follow()


def unfollow():
    instabot.target = target_account_entry.get()
    if len(instabot.target) == 0:
        messagebox.showerror('ERROR', 'NO USERNAME SUPPLIED')
        return
    instabot.unfollow()


# USER INPUTS:
username = 'yyy'
password = 'xxx'
# CREATING THE BOT
instabot = Bot(username, password)
# CREATING GUI
window = Tk()
window.title('Instagram Bot')
window.config(padx=30, pady=30)
# CREATING CANVAS
canvas = Canvas(height=300, width=250)
BotImage = PhotoImage(file='instabot.png')
canvas.create_image(150, 125, image=BotImage)
canvas.grid(row=0, column=1)
# CREATING LABELS
target_account_label = Label(text='Enter Target User ID')
target_account_label.grid(row=1, column=0)
# CREATING ENTRY
target_account_entry = Entry(width=20)
target_account_entry.focus()
target_account_entry.grid(row=1, column=1)
# CREATING BUTTON
like_button = Button(window, text='LIKE AND COMMENT', command=like)
like_button.grid(row=2, column=1)
follow_button = Button(window, text='FOLLOW', command=follow)
follow_button.grid(row=3, column=1)
unfollow_button = Button(window, text='UNFOLLOW', command=unfollow)
unfollow_button.grid(row=4, column=1)
window.mainloop()
