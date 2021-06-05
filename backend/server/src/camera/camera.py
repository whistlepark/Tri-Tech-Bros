import cv2
from camera.models import IPCamera
import datetime as dt
import multiprocessing as Thread
import logging
logger = logging.getLogger(__name__)


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

logging.basicConfig( level=logging.DEBUG)
logging.debug('Watch out!')

def gen_frames(pk,record = False):  # generate frame by frame from camera
    camObj = IPCamera.objects.get(pk=pk)
    camera = cv2.VideoCapture("rtsp://admin:TriTechBr0s@"+camObj.IP)
    #camera = cv2.VideoCapture("rtsp://admin:TriTechBr0s@209.65.187.212:551", cv2.CAP_FFMPEG)
    #logging.debug(cv2.getBuildInformation())

    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    out = cv2.VideoWriter('/static/camera/media/'+camObj.location+'/'+str(dt.date.today()),fourcc,20.0,(640,480))
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            if camObj.record:
                out.write(frame)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


# List of active recording videos
camera_threads = {}

def start_thread(pk):
    camObj = IPCamera.objects.get(pk=pk)
    video_stream_widget = RTSPVideoWriterObject(camObj)
    camera_threads[pk] = video_stream_widget

def stop_record(pk):
    camera_threads[pk].record = False

def start_record(pk):
    camera_threads[pk].record = True

def stop_thread(pk):
    #camera_threads[pk].run = False
    #logger.info('------------- we made it ---------------')
    del camera_threads[pk]

class RTSPVideoWriterObject(object):
    def __init__(self, camObj, record):
        # Allows thread to be stopped
        self.run = True

        # Sets recording to False initially
        self.record = False

        # Create a VideoCapture object
        self.capture = cv2.VideoCapture("rtsp://admin:TriTechBr0s@"+camObj.IP)

        # Default resolutions of the frame are obtained (system dependent)
        self.frame_width = int(self.capture.get(3))
        self.frame_height = int(self.capture.get(4))

        # Set up codec and output video settings
        self.codec = cv2.VideoWriter_fourcc(*'mp4v')
        self.output_video = cv2.VideoWriter(str(dt.date.today())+'.avi',self.codec,20.0,(self.frame_width, self.frame_height))

        # Start the thread to read frames from the video stream
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        # Read the next frame from the stream in a different thread
        while self.run:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()
                # Record
                if self.record:
                    self.save_frame()
                # Post to website
                ret, buffer = cv2.imencode('.jpg', self.frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
        return

    def show_frame(self):
        # Display frames in main program
        if self.status:
            cv2.imshow('frame', self.frame)

        # Press Q on keyboard to stop recording
        key = cv2.waitKey(1)
        if key == ord('q'):
            self.capture.release()
            self.output_video.release()
            cv2.destroyAllWindows()
            exit(1)

    def save_frame(self):
        # Save obtained frame into video output file
        self.output_video.write(self.frame)
