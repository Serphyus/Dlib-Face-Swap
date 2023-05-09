<h1 align="center">
	Dlib-Face-Swap
</h1>

This project is an ai project that uses dlib's frontal_face_detector and
a 68 face landmark shape predictor model. The detector discovers faces
in a live feed provided from a chosen capture device. When discovering
the faces the program uses the landmark predictor model to create a set
of landmark coordinates. These then get used to create generate dealunay
triangulations which are used to warp the triangulations created on the
image given to use as the face mask using an affine transformation.
Finally the triangles of the face mask is applied to the capture feed's
frame.

## FaceMask Demo
<div align="center">
    <img src="/media/tom_cruise.jpg" height="200">
	<img width="50px">
	<img src="/media/right-arrow.png" height="200">
	<img width="50px">
	<img src="/media/demo.gif" height="200">
</div>

## Pip Requirements
- opencv-python
- numpy
- dlib
- Pillow
- windows-capture-device-list

## Setup
clone the main repo and install requirements
```
git clone https://github.com/Serphyus/Dlib-Face-Swap.git
cd Dlib-Face-Swap
pip install requirements.txt
```

## Usage
run the main python file
```
python src/main.py
```