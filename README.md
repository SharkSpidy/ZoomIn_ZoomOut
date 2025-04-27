# ZoomIn_ZoomOut

### Project Description
This project uses hand gestures detected through a webcam to dynamically zoom in and zoom out an image on the screen.
By using two hands, the distance between their centers controls the scaling of an image, providing an interactive zooming experience.
It uses OpenCV, MediaPipe (via cvzone) for hand tracking, and numpy for image transformations.

## Technical Details
### Technologies/Components Used
##### For Software:
    Languages: Python
    Frameworks: OpenCV, MediaPipe, numpy
    Libraries: cvzone, numpy
    Tools: Visual Studio Code, Python virtual environments

##### For Hardware:
    Main Component: Webcam (internal/external)
    Specs: 720p or better for best results


### Implementation
##### Installation
```bash
# Create a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate      # On Windows: .venv\Scripts\activate

# Install dependencies
pip install cvzone mediapipe numpy
```
##### Run  
```bash
python main.py
```


### Project Documentation
For Software:
- `main.py` — Main program for hand tracking and volume control  
- `HandTrackingModule.py` — Custom wrapper around MediaPipe for easier hand landmark detection  
- `.venv/` — Python virtual environment (not required to be pushed to GitHub)  



# Screenshots
![Screenshot1](https://github.com/SharkSpidy/ZoomIn_ZoomOut/blob/main/Media/sc1.png)

![Screenshot2](https://github.com/SharkSpidy/ZoomIn_ZoomOut/blob/main/Media/sc2.png)

![Screenshot3](https://github.com/SharkSpidy/ZoomIn_ZoomOut/blob/main/Media/sc3.png)

### Project Demo
# Video
[Video](https://github.com/SharkSpidy/ZoomIn_ZoomOut/blob/main/Media/Recording%202025-04-27%20210849.mp4)

---
Made with ❤️ by [Joe](https://github.com/SharkSpidy)
