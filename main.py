import tkinter as tk

def melo10():
    verify = input("Enter the passcode: ")
    infos = '''
    1-Instagram: xxx - aaa
    2-Facebook: xxx - bbb
    3-Google: vvv - yzs
    '''
    if verify == '1278melo':
        window = tk.Tk()
        window.geometry("500x400")
        window.title("Info")
        window.config(padx=10, pady=10)
        title = tk.Label(window, text=infos)
        title.config(font=("Arial", 18))
        title.pack(padx=10, pady=30)
    else:
        print('ACCESS DENIED')

pencere = tk.Tk()
pencere.geometry("700x500")
pencere.title("PSP")
pencere.config(padx=10, pady=10)

title_label = tk.Label(pencere, text="Password Security Program")
title_label.config(font=("Arial", 32))
title_label.pack(padx=10, pady=30)

label_passcode = tk.Label(pencere, text="Enter the Passcode")
label_passcode.config(font=("Arial",20))
label_passcode.pack(padx=100, pady=60)

text_pass = tk.Text(pencere, height=1)
text_pass.config(font=("Arial",20))
text_pass.pack(padx=100, pady=10)

btn_load = tk.Button(pencere, text="Login", command=melo10)
btn_load.config(font=("Arial",20))
btn_load.pack(padx=10, pady=10)

pencere.mainloop()