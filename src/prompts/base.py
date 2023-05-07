import tkinter as tk


class Prompt:
	WIDTH  = None
	HEIGHT = None

	def __init__(self) -> None:
		self._create_window()
		self._create_ui()
		

	def _on_close_hook(self) -> None: ...

	
	def _on_close(self) -> None:
		self._on_close_hook()
		self._root.destroy()


	def _create_window(self) -> None:
		self._root = tk.Tk()
		self._root.title("Choose Image")
		self._root.minsize(self.WIDTH, self.HEIGHT)
		self._root.maxsize(self.WIDTH, self.HEIGHT)

		screen_w = self._root.winfo_screenwidth()
		screen_h = self._root.winfo_screenheight()

		x = int((screen_w/2) - (self.WIDTH/2))
		y = int((screen_h/2) - (self.HEIGHT/2))

		self._root.geometry(f"{self.WIDTH}x{self.HEIGHT}+{x}+{y}")

		self._root.protocol("WM_DELETE_WINDOW", self._on_close)
	

	def _create_ui(self) -> None: ...
	

	def _close(self) -> None:
		self._root.destroy()


	def _handle(self) -> None:
		self._root.mainloop()