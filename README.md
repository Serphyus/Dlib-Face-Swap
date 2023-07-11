<h1 align="center">
	Dlib-Face-Swap
</h1>

This project is an AI project that uses dlib for face detection and shape
prediction and some geometric triangulation and transformation for warping
a face mask on top of it. The detector discovers faces in a live feed
provided from a chosen capture device. For each face discovered in the
live feed the program uses the landmark predictor model to create a set
of face landmark coordinates. These then get used to calculate a dealunay
triangulation. The same process happens on the image given as the face
mask and for each frame the triangulations of the face mask are warped to
the shape of the face triangulations in the live feed using an affine
transformation and then rendered on top of them.

## FaceMask Demo
<div align="center">
    <img src="./media/tom_cruise.jpg" height="200">
	<img src="./media/right-arrow.png" height="200">
	<img src="./media/demo.gif" height="200">
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
