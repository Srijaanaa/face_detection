import cv2
import sys
try:
    from screeninfo import get_monitors
except ImportError:
    get_monitors = None

def get_screen_size():
    """Get the screen size using screeninfo or fallback to default values."""
    if get_monitors:
        try:
            monitor = get_monitors()[0]  # Use primary monitor
            return monitor.width, monitor.height
        except Exception as e:
            print(f"Warning: Could not get screen size: {e}")
    # Fallback to default size if screeninfo fails or is not installed
    return 1280, 720

def check_opencv_version():
    """Check OpenCV version and ensure it's installed."""
    try:
        return cv2.__version__
    except ImportError:
        return None

def main():
    # Verify OpenCV installation
    opencv_version = check_opencv_version()
    if opencv_version is None:
        print("Error: OpenCV is not installed. Please install it using 'pip install opencv-python'.")
        sys.exit(1)
    print(f"Using OpenCV version: {opencv_version}")

    # Get screen size
    screen_width, screen_height = get_screen_size()
    # Calculate webcam resolution (80% of screen size to avoid overflow)
    frame_width = int(screen_width * 0.8)
    frame_height = int(screen_height * 0.8)
    # Ensure aspect ratio (e.g., 4:3 or 16:9, using 4:3 for compatibility)
    frame_height = int(frame_width * 3 / 4)
    print(f"Setting frame size to {frame_width}x{frame_height}")

    # Load the pre-trained Haar Cascade classifier for face detection
    cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade_path)
    
    # Check if the cascade classifier loaded successfully
    if face_cascade.empty():
        print(f"Error: Could not load Haar Cascade classifier from {cascade_path}.")
        sys.exit(1)

    # Initialize video capture from the default webcam
    cap = cv2.VideoCapture(0)

    # Set webcam resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

    # Check if the webcam opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam. Ensure it's connected and not in use by another application.")
        print("Try changing the camera index (e.g., 0 to 1) in cv2.VideoCapture(1).")
        sys.exit(1)

    # Create a resizable window
    cv2.namedWindow('Face Detection', cv2.WINDOW_NORMAL)
    # Set initial window size to match frame
    cv2.resizeWindow('Face Detection', frame_width, frame_height)

    try:
        while True:
            # Read a frame from the webcam
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame from webcam.")
                break

            # Convert the frame to grayscale for face detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the grayscale frame
            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )

            # Draw rectangles around detected faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            # Display the frame with detected faces
            cv2.imshow('Face Detection', frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        print("Stopped by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Release the webcam and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()