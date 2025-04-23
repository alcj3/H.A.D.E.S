from ultralytics import YOLO
import cv2
import time

def main():
    # load pretrained model
    model = YOLO('yolov8n.pt')

    # AVFoundation backend on macOS
    cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

    # 320x320 @ 30 FPS
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)
    cap.set(cv2.CAP_PROP_FPS, 30)

    if not cap.isOpened():
        print("camera failed to open")
        return

    prev_time = time.time()
    
        
    while True:
        ret, frame = cap.read()
        if not ret:
            print("frame grab failed, exiting")
            break

        results = model(frame, verbose=False)[0]    # run YOLO
        annotated = results.plot()                  # draw boxes

        # calculate fps count 
        curr_time = time.time()
        fps = 1.0 / (curr_time - prev_time)
        prev_time = curr_time

        # overlay fps count in top left

        cv2.putText(
            annotated,
            f"{fps:.1f} FPS",
            (10, 25),                             # position
            cv2.FONT_HERSHEY_SIMPLEX,             # font
            0.7,                                  # font scale
            (0, 255, 0),                          # color (BGR)
            2                                     # thickness
        )

        # display annotated frame
        cv2.imshow("YOLO Live", annotated)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()





