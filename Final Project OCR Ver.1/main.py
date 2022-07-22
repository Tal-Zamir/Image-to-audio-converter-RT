import cv2
import pytesseract
from gtts import gTTS
from playsound import playsound

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

video = cv2.VideoCapture("http://192.168.1.116:8080/video")
video.set(3, 640)
video.set(4, 480)

img1 = cv2.imread('pic2.png')
h1Img, w1Img, _ = img1.shape

#getting the w&h of each char. on the picture
box1 = pytesseract.image_to_boxes(img1)

data1 = pytesseract.image_to_data(img1)

#used to play the image text
filewrite = open("string.txt", "w")
for z, a in enumerate(data1.splitlines()):
        if z!= 0:
            a = a.split()
            if len(a) == 12:
                x, y = int(a[6]), int(a[7])
                w, h = int(a[8]), int(a[9])
                cv2.rectangle(img1, (x, y), (x + w,y + h), (255, 0, 0), 1)
                cv2.putText(img1, a[11], (x, y + 25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
                filewrite.write(a[11] + " ")
filewrite.close()
fileread = open("string.txt", "r")
lang = 'en'
line = fileread.read()
if line != ' ':
    speech = gTTS(text = line, lang=lang, slow = False)
    speech.save("test.mp3")
cv2.imshow('gtts', img1)
cv2.waitKey(0)
playsound("test.mp3")


# while True:
#     check, frame = video.read()
#     data2 = pytesseract.image_to_data(frame)
#     for z, a in enumerate(data2.splitlines()):
#         if z!= 0:
#             a = a.split()
#             if len(a) == 12:
#                 x, y = int(a[6]), int(a[7])
#                 w, h = int(a[8]), int(a[9])
#                 cv2.rectangle(frame, (x, y), (x + w,y + h), (255, 0, 0), 1)
#                 cv2.putText(frame, a[11], (x, y + 25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
#     cv2.imshow('video capture', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         video.release()
#         cv2.destroyAllWindows()
