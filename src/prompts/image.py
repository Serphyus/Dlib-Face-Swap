from pathlib import Path
from typing import Union

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import ImageTk, Image

from dialog import error_msg
from prompts.base import Prompt


class ImagePrompt(Prompt):
	WIDTH  = 300
	HEIGHT = 350

	def __init__(self, asset_dir: Path) -> None:
		self._asset_dir = asset_dir
		self._img_path = None

		super().__init__()


	def _on_close_hook(self) -> None:
		self._img_path = None


	def _load_img(self, path: Path) -> ImageTk.PhotoImage:
		img = Image.open(path)
		img = img.resize((252, 252))
		return ImageTk.PhotoImage(img)
	
	
	def _ask_for_image(self) -> None:
		image_file = fd.askopenfilename(title="choose image file")
		if not image_file:
			error_msg("No image was chosen")
			return
		
		try:
			new_img = self._load_img(image_file)
			
			self._canvas.itemconfig(
				self._img_container,
				image=new_img
			)
			
			self._img = new_img
			self._img_path = Path(image_file)

		except Exception:
			error_msg("Unable to load image")


	def _confirm_choice(self) -> None:
		if self._img_path is None:
			error_msg("No image selected")
			return
		
		self._close()


	def _create_ui(self) -> None:
		self._canvas = tk.Canvas(
			self._root,
			width=250,
			height=250,
			highlightbackground="gray"
		)
		self._canvas.pack()
		self._canvas.place(x=25, y=25)
		
		self._img = self._load_img(Path(self._asset_dir, "image.jpg"))
		self._img_container = self._canvas.create_image(
			0, 0,
			anchor=tk.NW,
			image=self._img
		)
		
		self._select_btn = ttk.Button(
			self._root,
			text="Select image",
			command=self._ask_for_image
		)
		self._select_btn.pack()
		self._select_btn.place(y=310, relx=0.35, anchor=tk.CENTER)

		self._ok_btn = ttk.Button(
			self._root,
			text="Ok",
			command=self._confirm_choice
		)
		self._ok_btn.pack()
		self._ok_btn.place(y=310, relx=0.65, anchor=tk.CENTER)


	def run(self) -> Union[Path, None]:
		self._handle()
		return self._img_path