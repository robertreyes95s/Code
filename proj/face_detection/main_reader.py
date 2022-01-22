import cv2 
import sys

cascPath = sys.argv[0]
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture

while true: 
    #Caprture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frane, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5, 
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE

    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces: 
        cv2.rectangle(frame, (x, y), (x+W, y+h),  (0, 255, 0), 2)
    
    # Display the resulting  frame
    cv2.imshow('Video', frame)

    if cv2.waitkey(1) & 0xFF == ord('q'):
        break
    
    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()


