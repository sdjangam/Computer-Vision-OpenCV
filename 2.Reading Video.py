import cv2 as cv
capture = cv.VideoCapture('demo2.mp4')
while True:
    isTrue, frame = capture.read()
    if isTrue:    
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break
capture.release()
cv.destroyAllWindows()