from picamera2 import Picamera2
from ultralytics import YOLO
import cv2
import time

def main():
    model = YOLO("yolov8n.pt")

    picam2 = Picamera2()
    picam2.configure(picam2.create_preview_configuration(main={"size": (320, 320)}))
    picam2.start()

    time.sleep(2)  # let camera warm up
    prev_time = time.time()

    while True:
        frame = picam2.capture_array()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

        results = model(frame, verbose=False)[0]
        annotated = results.plot()

        # calculate FPS
        curr_time = time.time()
        fps = 1.0 / (curr_time - prev_time)
        prev_time = curr_time

        cv2.putText(
            annotated,
            f"{fps:.1f} FPS",
            (10, 25),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

        cv2.imshow("YOLO Live", annotated)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
