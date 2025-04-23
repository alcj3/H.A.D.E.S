import cv2

def main():

    # 0 is usually built in camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("could not open camera")
        return
    
    # 320x320 @ 30 FPS
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)
    cap.set(cv2.CAP_PROP_FPS, 30)

    w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv2.CAP_PROP_FPS)

    print(f"Capturing at {w:.0f}×{h:.0f} @ {fps:.0f} FPS")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("frame grab failed: returning")
            break
            
        cv2.imshow("camera test", frame)
        # exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


