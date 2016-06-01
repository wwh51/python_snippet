import cv2
import cv2.cv as cv
import time
import datetime
import winsound
from PIL import Image, ImageDraw, ImageFont
 
# Camera 0 is the integrated web cam on my netbook
camera_port = 0
 
#Number of frames to throw away while the camera adjusts to light levels, just when it start
ramp_frames = 20
 
# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.

 
# Captures a single image from the camera and returns it in PIL format
def get_image(cam):
 # read is the easiest way to get a full image out of a VideoCapture object.
 retval, im = cam.read()
 return im

def add_num(file_jpg):
    img = Image.open(file_jpg)
    draw = ImageDraw.Draw(img)
    # myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    # fillcolor = "#ff0000"
    width, height = img.size
    draw.text((40, 40), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    img.save(file_jpg, "jpeg")
    del draw
# Ramp the camera - these frames will be discarded and are only used to allow v4l2
# to adjust light levels, if necessary

print("Taking image...")
# Take the actual image we want to keep
file_index = 0
while file_index < 1:
    for i in xrange(1):
        winsound.PlaySound('bell.wav', winsound.SND_FILENAME)
    camera = cv2.VideoCapture(0)
    camera.set(3,640);
    camera.set(4,480);
    for i in xrange(ramp_frames):
        temp = get_image(camera)
    camera_capture = get_image(camera)        
    #file = r'\\MEL-STORAGE1\share\dwang\pre\test_1.png'
    file_jpg = r'c:\wwh\{0}.jpg'.format(file_index)
    file_index = file_index + 1    
    cv2.imwrite(file_jpg, camera_capture)
    add_num(file_jpg)
    del(camera)
    im = Image.open(file_jpg, "jpeg")
    im.show()
    time.sleep(10) 


    # cv.NamedWindow("camera", 1)
    # capture = cv.CaptureFromCAM(0)
    # for i in xrange(30):
    #     img = cv.QueryFrame(capture)
    #     cv.ShowImage("camera", img)
           
    # cv.DestroyAllWindows()
    
 
# You'll want to release the camera, otherwise you won't be able to create a new
# capture object until your script exits
