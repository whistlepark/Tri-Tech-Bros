import cv2


# # dirname = videos
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     cv2.imshow('frame', frame)
#     # cv2.imwrite(os.path.join(dirname,name), frame)
#     if cv2.waitKey(20) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()
record = False




def gen_frames(record = False):  # generate frame by frame from camera
    camera = cv2.VideoCapture("rtsp://admin:TriTechBr0s@209.65.187.212")
    # i=0
    while True:
        # i +=1
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            # print(i)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result