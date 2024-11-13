import cv2 as cv

# img=cv.imread("Photos/cat.jpg")
# cv.imshow('Macja', img)
# cv.waitKey(0)

capture=cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame=capture.read()
    cv.imshow('VIdeo', frame)

    if cv.waitKey(20) & 0xFF==ord('q'):
        break

capture.release()
cv.destroyAllWindows()