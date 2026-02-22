
import customtkinter as ctk
import random


#generate mobil nomer
def mobil():
	reg = str(random.randint(1, 100))
	one = str(random.randint(1, 999)).zfill(3)
	two = str(random.randint(1, 999)).zfill(3)
	thee = str(random.randint(1, 99)).zfill(2)
	four = str(random.randint(1, 99)).zfill(2)

	nomer = f'+{reg} {one} {two} {thee} {four}'
	lbl.configure(text=nomer)
#info window
def info():
	inf = ctk.CTkToplevel(root)
	inf.title('info')
	inf.geometry('300x200')

	info_text = ctk.CTkLabel(inf, text='hi, this info')
	info_text0 = ctk.CTkLabel(inf, text='my telegram: @KRENDEL_PythonOrg')
	info_text.pack(pady=10)
	info_text0.pack(pady=10)
#main window
root = ctk.CTk()
root.title("mobil")
root.geometry("600x800")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

btn1 = ctk.CTkButton(root, text='info', command=info)
btn1.pack(anchor='nw', pady=10, padx=10)

lbl = ctk.CTkLabel(root, text="click button", font=("Arial", 50))
lbl.pack(pady=100)

btn = ctk.CTkButton(root, text="generate", command=mobil, height=200, width=400, font=('Arial', 50))
btn.pack(pady=100)

# I`M GOVNOKODER HELL YEEEEEAH

root.mainloop()