from tkinter.messagebox import showerror as _err_msg


def error_msg(msg: str) -> None:
	_err_msg(f"Error!", msg)