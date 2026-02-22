import customtkinter as ctk


class LemonadeTycoon:
	def __init__(self) -> None:
		self.root = ctk.CTk()
		self.root.title("tycoon")
		self.root.geometry("1000x1000")

		self.limonade = 10
		self.limonade_skill = 1
		self.is_anim = False
		self.is_anim_create = False
		self.clickPower = 10
		self.money = 100
		self.setupUi()

		ctk.set_appearance_mode('dark')
		ctk.set_default_color_theme('blue')
		ctk.set_widget_scaling(2)

	def add_limon(self):
		if not self.is_anim_create:
			self.is_anim_create = True
			self.btn_create_limon.configure(state='disabled')
			self.btn_create_limon.configure(text='creating...')
			self.add_limon_anim(0)


	def add_limon_anim(self, current_value2):
		if current_value2 < 1:
			self.progress_limon.set(current_value2 + 0.1)
			self.root.after(500, lambda: self.add_limon_anim(current_value2 + 0.1))
		else:
			self.progress_limon.set(0)
			self.btn_create_limon.configure(state='normal')
			self.btn_create_limon.configure(text='add lemonade')
			self.is_anim_create = False
			self.limonade += self.limonade_skill
			self.lab_limonade.configure(text=f'Lemonade: {self.limonade}')


	def sell(self):
		if not self.is_anim and self.limonade > 0:
			self.is_anim = True
			self.btnSell.configure(state='disabled')
			self.anim_prog(0)

	def anim_prog(self, current_value):
		if current_value < 1:
			self.progress.set(current_value + 0.1)
			self.root.after(100, lambda: self.anim_prog(current_value + 0.1))
		else:
			self.progress.set(0)
			self.is_anim = 0
			self.btnSell.configure(state="normal")
			self.add_money()
			self.limonade -= 1
			self.lab_limonade.configure(text=f'Lemonade: {self.limonade}')

	def add_money(self):
		self.money += self.clickPower
		self.lblMoney.configure(text=f'Balance: {self.money}')
	
	def buy(self, store):
		if self.money >= 50 and store == 0:
			self.money -= 50
			self.clickPower += 5
			self.lblMoney.configure(text=f'Balance: {self.money}')
		elif self.money >= 300 and store == 1:
			self.money -= 300
			self.limonade_skill += 1
			self.lblMoney.configure(text=f'Balance: {self.money}')

	#main GUI
	def setupUi(self):
		
		#label lemonade count
		self.lab_limonade = ctk.CTkLabel(self.root, 
			text=f'Lemonade: {self.limonade}',
			font=('Arial', 20)
		)
		self.lab_limonade.pack(anchor='nw', pady=10, padx=10)
		#button sell lemonade
		self.btnSell = ctk.CTkButton(self.root, 
			text='Sell lemonade', 
			command=self.sell)
		self.btnSell.pack(pady=10)

		#progress sell lemonade
		self.progress = ctk.CTkProgressBar(self.root,
			width=200)
		self.progress.set(0)
		self.progress.pack(pady=10)
		#Money!!!
		self.lblMoney = ctk.CTkLabel(self.root,
			text=f'Balance: {self.money}',
			font=('Arial', 20)
		)
		self.lblMoney.pack(pady=10)

		self.frm = ctk.CTkFrame(self.root)
		self.frm.pack(pady=10)
#buy pitcher
		self.btn_pit = ctk.CTkButton(self.frm,
			text='Buy pitcher 50$', 
			command=lambda: self.buy(0))
		self.btn_pit.pack()

		#up skill button
		self.btn_skill = ctk.CTkButton(self.frm, text='Up skill', command=lambda: self.buy(1))
		self.btn_skill.pack(pady=5)

		#progres create lemonade
		self.progress_limon = ctk.CTkProgressBar(self.root, 
			width=300)
		self.progress_limon.set(0)
		self.progress_limon.pack(pady=50)

		#button create lemonade
		self.btn_create_limon = ctk.CTkButton(self.root,
			text="Create lemonade",
			command=self.add_limon
		  )
		self.btn_create_limon.pack(pady=10)

		#start system
	def run(self):
		self.root.mainloop()

game = LemonadeTycoon()
game.run()