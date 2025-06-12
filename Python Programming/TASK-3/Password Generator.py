import tkinter as tk
from tkinter import messagebox
import random
import string
def generate_password():
    try:
            length1=int(length.get())
            if length1<5:
                messagebox.showwarning("Warning", "Length should be at least 5.")
                return
            ch=string.ascii_letters+string.digits+string.punctuation+string.ascii_uppercase
            password=[random.choice(string.ascii_lowercase),random.choice(string.ascii_uppercase),random.choice(string.digits),random.choice(string.punctuation)]
            password+=random.choices(ch,k=length1-4)
            password_str=''.join(password)
            result_entry.delete(0,tk.END)
            result_entry.insert(0,password_str)

    except ValueError:
              messagebox.showerror("Error", "Please enter a valid number.")
def quit_():
    root.destroy()
 
root=tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

label=tk.Label(root,fg='blue',text="Enter Password Length:")
label.pack()

length=tk.Entry(root,fg='red',justify='center')
length.pack()

generate_btn=tk.Button(root,text="Generate Password",fg='white',bg='green',command=generate_password)
generate_btn.pack()

label2=tk.Label(root,fg='blue',text="Generated Password:")
label2.pack()

result_entry = tk.Entry(root,width=40, justify='center')
result_entry.pack()

done_bt=tk.Button(root,text='Done',fg='white',bg='orange',command=quit_)
done_bt.pack()

root.mainloop()
