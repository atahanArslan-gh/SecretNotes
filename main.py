from tkinter import *
from tkinter import messagebox
import base64

#encode and decode functions
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

#buttons functions
def save_encrypt_button_click():
    user_title = title_entry.get()
    user_text = secret_text.get('1.0', END)
    user_master_key = master_key_entry.get()

    if len(user_title) == 0 or len(user_text) == 0 or len(user_master_key) == 0:
        messagebox.showinfo(title='Information', message='Please enter all information')
    else:
        message_encrypted = encode(user_master_key, user_text)
        file_name = str('C:\\Users\\user\\OneDrive\\Masaüstü\\Secrets\\' + user_title + '.txt')
        try:
            with open(file_name, 'a') as note_file:
                note_file.write(message_encrypted)
        except FileNotFoundError:
            with open(file_name, 'w') as note_file:
                note_file.write(message_encrypted)
        finally:
            title_entry.delete(0, END)
            secret_text.delete(1.0, END)
            master_key_entry.delete(0, END)

def decrypt_button_click():
    encrypted_message = secret_text.get('1.0', END)
    user_master_key = master_key_entry.get()
    if len(encrypted_message) == 0 or len(user_master_key) == 0:
        messagebox.showinfo(title='Information', message='Please enter all information')
    else:
        try:
            decrypted_message = decode(user_master_key, encrypted_message)
            secret_text.delete('1.0', END)
            secret_text.insert('1.0', decrypted_message)
        except:
            messagebox.showwarning('Warning', 'You entered invalid text!')


#user interface
window = Tk()
window.title('Secret Notes')
window.config(padx=30, pady=30)
FONT = ('Verdana', 20, 'normal')

photo = PhotoImage(file='topsecret.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=photo)
canvas.pack()

title_label = Label(text='Enter your title', font=FONT)
title_label.pack()

title_entry = Entry(width=30)
title_entry.pack()

secret_label = Label(text='Enter your secret', font=FONT)
secret_label.pack()

secret_text = Text(width=40, height=20)
secret_text.pack()

master_key_label = Label(text='Enter your master key', font=FONT)
master_key_label.pack()

master_key_entry = Entry(width=15)
master_key_entry.pack()

save_button = Button(text='Save & Encrypt', command=save_encrypt_button_click, font=('Arial', 12, 'normal'))
save_button.pack()

decrypt_button = Button(text='Decrypt', font=('Arial', 12, 'normal'), command=decrypt_button_click)
decrypt_button.pack()

window.mainloop()