# Pose Detection and Posture Analysis

This project utilizes the Mediapipe library along with OpenCV to detect human poses in a video stream and analyze whether the person is standing or sitting based on the detected pose.

## Dependencies
- Python 3.x
- OpenCV (`pip install opencv-python`)
- Mediapipe (`pip install mediapipe`)

## Description
The script `pose_detection.py` performs the following tasks:

1. Initializes a video capture object.
2. Utilizes the Mediapipe Pose model to detect human poses in each frame.
3. Analyzes the detected pose to determine whether the person is standing or sitting.
4. Annotates the frame with the analyzed posture.
5. Draws the detected pose landmarks on the frame.
6. Writes the annotated frames to an output video file.

## Code Explanation
- `detect_pose(frame, pose_detector)`: Detects pose landmarks in a given frame using the specified pose detector.
- `analyze_posture(keypoints)`: Analyzes the detected keypoints to determine whether the person is standing or sitting.
- `annotate_frame(frame, posture)`: Annotates the frame with the analyzed posture.
- `draw_pose_landmarks(frame, landmarks)`: Draws the detected pose landmarks on the frame.
- Video input is read from a specified file path.
- Output video is written to `output_video.mp4`.
- The script continues to process frames until the user interrupts by pressing 'q'.

## Customization
- You can adjust the threshold value in the `analyze_posture` function to better differentiate between standing and sitting postures based on your video characteristics.
- Modify the input video file path (`cap = cv2.VideoCapture('your_video.mp4')`) to use your own video file.

## Acknowledgments
- This project uses the Mediapipe library for pose detection.
