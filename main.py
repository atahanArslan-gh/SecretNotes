from tkinter import *
from tkinter import messagebox

def save_button_click():
    user_title = title_entry.get()
    user_text = secret_text.get('1.0', END)
    user_master_key = master_key_entry.get()
    file_name = str('C:\\Users\\user\\OneDrive\\Masaüstü\\Secrets\\' + user_title + '.txt')
    text_file = open(file_name, 'w')
    if user_title == '' or user_master_key == '':
        messagebox.showinfo(title='Information', message='Please enter all information')
    else:
        pass


#user interface
window = Tk()
window.title('Secret Notes')
window.config(padx=30, pady=30)

title_label = Label(text='Enter your title')
title_label.pack()

title_entry = Entry(width=20)
title_entry.pack()

secret_label = Label(text='Enter your secret')
secret_label.pack()

secret_text = Text(width=40, height=20)
secret_text.pack()

master_key_label = Label(text='Enter your master key')
master_key_label.pack()

master_key_entry = Entry(width=20)
master_key_entry.pack()

save_button = Button(text='Save and Encrypt', command=save_button_click)
save_button.pack()

decrypt_button = Button(text='Decrypt')
decrypt_button.pack()





#messagebox.showwarning("showinfo", "Information")


window.mainloop()