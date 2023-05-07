from typing import Tuple

import cv2
import numpy as np


def draw_rect_frame(frame: np.ndarray, rect: object, color: Tuple[int, int, int]) -> None:
    x = rect.left()
    y = rect.top()
    w = rect.width()
    h = rect.height()

    # set lenght of cornor lines
    corner = int(min(w, h) * 0.15)

    # top left
    cv2.line(frame, (x, y), (x + corner, y), color, 2)
    cv2.line(frame, (x, y), (x, y + corner), color, 2)

    # top right
    cv2.line(frame, (x + w, y), (x + w - corner, y), color, 2)
    cv2.line(frame, (x + w, y), (x + w, y + corner), color, 2)

    # bottom left
    cv2.line(frame, (x, y + h), (x + corner, y + h), color, 2)
    cv2.line(frame, (x, y + h), (x, y + h - corner), color, 2)

    # bottom right
    cv2.line(frame, (x + w, y + h), (x + w, y + h - corner), color, 2)
    cv2.line(frame, (x + w, y + h), (x + w - corner, y + h), color, 2)