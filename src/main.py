import sys
from pathlib import Path

import cv2
from tkinter import messagebox
from tkinter import filedialog as fd

from faces_mask import FacesMask
from dialog import error_msg
from prompts.image import ImagePrompt
from prompts.camera import CameraPrompt


def main() -> None:
    try:
        asset_dir = Path(Path(__file__).resolve().parent.parent, "assets")

        predictor = Path(asset_dir, "shape_predictor_68_face_landmarks.dat")
        if not predictor.is_file():
            raise RuntimeError("unable to locate predictor dat file")

        img_prompt = ImagePrompt(asset_dir)
        face_mask_file = img_prompt.run()

        if face_mask_file is None:
            exit()

        camera_prompt = CameraPrompt()
        capture_index = camera_prompt.run()

        if capture_index is None:
            exit()

        if sys.platform == "win32":
            cap = cv2.VideoCapture(capture_index, cv2.CAP_DSHOW)
            ret, _ = cap.read()
            
            if not ret:
                cap.release()
                cap = cv2.VideoCapture(capture_index)
        else:
            cap = cv2.VideoCapture(index)

        dlib_handler = FacesMask(predictor)
        dlib_handler.set_mask(face_mask_file)
        
        window_res = (640, 480)
        cv2.namedWindow("FaceMask", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("FaceMask", *window_res)

        while cv2.getWindowProperty("FaceMask", cv2.WND_PROP_VISIBLE) >= 1:
            ret, frame = cap.read()

            if ret:
                frame = cv2.flip(frame, 1)
                new_frame = dlib_handler.process_frame(frame)

                if new_frame is not None:
                    frame = new_frame

                cv2.imshow("FaceMask", frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

        cap.release()
        cv2.destroyAllWindows()

    except RuntimeError as err:
        error_msg(str(err))


if __name__ == "__main__":
    main()