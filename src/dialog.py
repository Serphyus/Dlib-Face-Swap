from typing import Union

from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror as _err_msg


def error_msg(msg: str) -> None:
    _err_msg(f"Error!", msg)


def ask_file(title: str) -> Union[str, None]:
    return askopenfilename(title=title)