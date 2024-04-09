import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose

def detect_pose(frame, pose_detector):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Process the frame for pose detection
    results = pose_detector.process(frame_rgb)
    return results.pose_landmarks

def analyze_posture(keypoints):
    # This function should analyze the keypoints and return "Standing" or "Sitting"
    if keypoints:
        hip_y = keypoints.landmark[mp_pose.PoseLandmark.LEFT_HIP].y
        # Assume that if the hip landmark's y-coordinate is above a threshold, the person is standing
        if hip_y < 0.6:  # threshold value, may need to be adjusted based on your video
            return "Standing"
        else:
            return "Sitting"
    return "Unknown"

def annotate_frame(frame, posture):
    # Draw the posture text on the frame
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, posture, (50, 50), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
    return frame

def draw_pose_landmarks(frame, landmarks):
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_drawing.draw_landmarks(
        frame,
        landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style()
    )
    return frame

cap = cv2.VideoCapture(r'replace your video adress')

pose_detector = mp_pose.Pose()

# Check if the video capture is opened successfully
if not cap.isOpened():
    print("Error: Couldn't open the video file.")
    exit()

# Get the frame width and height
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Prepare to write the output video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_video.mp4', fourcc, 20.0, (frame_width, frame_height))

while True:
    ret, frame = cap.read()
    if not ret:
        break  

    keypoints = detect_pose(frame, pose_detector)

    posture = analyze_posture(keypoints)

    annotated_frame = annotate_frame(frame.copy(), posture)

    if keypoints:
        annotated_frame = draw_pose_landmarks(annotated_frame, keypoints)

    out.write(annotated_frame)

    cv2.imshow('Frame', annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
