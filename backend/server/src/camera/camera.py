import cv2
from camera.models import IPCamera
import datetime as dt


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




def gen_frames(pk,record = False):  # generate frame by frame from camera
    camObj = IPCamera.objects.get(pk=pk)
    camera = cv2.VideoCapture("rtsp://admin:TriTechBr0s@"+camObj.IP)
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    out = cv2.VideoWriter('/static/media/'+camObj.location+'/'+str(dt.date.today()),fourcc,20.0,(640,480))
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            if record:
                out.write(frame)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
