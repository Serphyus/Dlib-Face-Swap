# Dlib-Face-Swap

This project is an ai project that uses Dlib's face_detector and
68 face landmark shape predictor model. The program uses the detector
and predictor to discover faces in a live feed from on of the capture
devices. When discovering faces in the capture device feed the program
uses opencv to create a delaunay triangulation of it's face landmarks.
These triangles then warps the face landmarks in an image provided by
the user using an affine transformation. After having warped all the
triangles in the mask to fit the users current face landmark positions
it applies the newly warped face mask on top.

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
```
git clone https://github.com/Serphyus/Dlib-Face-Swap.git
cd Dlib-Face-Swap
pip install requirements.txt
```

## Usage
```
python src/main
```