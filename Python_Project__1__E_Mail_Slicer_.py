
import tkinter as tk
window = tk.Tk()
window.geometry("1920x1080")
window.config(bg="#698B69")
window.resizable(width=False,height=False)
window.title('Simple E-mail Slicer')

def result():
    try:
        email=entry.get()
        inp_email = email_strip()
        username = inp_email[0:inp_email.index('@')]
        domain = inp_email[inp_email.index('@') + 1:]
        text_box.delete('1.0', tk.END)
        msg = 'Email entered was: {}/nYour email username is{}/nAnd your email domain server is {}'
        msg_formatted = msg.format(email,username,domain)
        text_box.insert(tk.END,msg_formatted)
        entry.delete(0, 'end')
    except:
        text_box.delete('1.0', tk.END)
        text_box.insert(tk.END, "ERROR!")

def reset_all():
    text_box.delete('1.0', tk.END)
    entry.delete(0, 'end')

# Labels
greeting = tk.Label(text="Welcome to a simple E-Mail Slicer!",font=(12),foreground= "white",background="black")
Info = tk. Label(foreground= "white", font=(10),background="#698B69",text="Enter your email ID and click the done button!/n the application will extract your username and domain name.")
entry_label = tk.Label(foreground= "white",font=(10),background="black",text="Enter your Email ID: ")
result_label = tk.Label(font=(10),foreground= "white",background="black",text="The results are as follows:")
empty_label0=tk.Label(background="#698B69")
empty_label1=tk.Label(background="#698B69")
empty_label2=tk.Label(background="#698B69")
empty_label3=tk.Label(background="#698B69")
empty_label4=tk.Label(background="#698B69")
empty_label5=tk.Label(background="#698B69")

# Entry
e1=tk.StringVar()  
entry = tk.Entry(font=(11),width=50,justify='center',textvariable=e1)

# Buttons
button = tk.Button(text="Done!",command=result,font=(11))
reset=tk.Button(text="Reset!",command=reset_all,font=(11))

# Result
text_box = tk.Text(height=5,width=50)

# Packing Everything Together
empty_label0.pack()
greeting.pack()
Info.pack()
empty_label1.pack()
entry_label.pack()
empty_label4.pack()
entry.pack()
empty_label2.pack()
button.pack()
empty_label5.pack()
reset.pack()
empty_label3.pack()
result_label.pack()
text_box.pack()

window.mainloop()

