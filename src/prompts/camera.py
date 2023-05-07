from typing import Union

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from device import getDeviceList

from prompts.base import Prompt

# Due to SystemError on built-in function
# returned Null without setting an exception
_devices = getDeviceList()


class CameraPrompt(Prompt):
	WIDTH  = 300
	HEIGHT = 150

	def __init__(self) -> None:
		self._devices = [*map(lambda l: l[0], _devices)]
		super().__init__()
	
	
	def _on_close_hook(self) -> None:
		self._clicked.set("")


	def _confirm_choice(self) -> None:
		if self._clicked.get() not in self._devices:
			messagebox.showerror("Invalid device chosen")
			return

		self._close()


	def _create_ui(self) -> None:
		self._clicked = tk.StringVar()
		self._clicked.set("Choose Capture Dev")
		
		self._drop = ttk.OptionMenu(
			self._root,
			self._clicked,
			None,
			*self._devices
		)

		menu_width = max(18, *map(len, self._devices))

		self._drop.config(width=menu_width)
		self._drop.pack(pady=30, ipadx=10)

		self._confirm_btn = ttk.Button(
			self._root,
			text="Confirm",
			command=self._confirm_choice
		)

		self._confirm_btn.pack()


	def run(self) -> Union[int, None]:
		self._handle()

		choice = self._clicked.get()
	
		if choice:
			index = self._devices.index(choice)
			return index