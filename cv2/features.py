import cv2
import imutils

def show_webcam(mirror,i):
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if mirror: 
            img = cv2.flip(img, 1)
        cv2.imshow('my webcam', img)
        print('Press ESC to save the video capture. Enter: ')
        k = cv2.waitKey(0)
        if k == 27: 
            cv2.imwrite('videocap'+str(i)+'.jpg',img)
            print("Saved!")
            break
    cv2.destroyAllWindows()

def resize(i):
    img = cv2.imread('videocap'+str(i)+'.jpg',1)
    cv2.imshow('image',img)
    cv2.waitKey(2000)
    cv2.destroyWindow('image')
    len = int(input('Enter length: '))
    wid = int(input('Enter width: '))
    bigger = cv2.resize(img, (len, wid))
    cv2.imshow('resizedimage',bigger)
    print('Press ESC to quit and s to save the video capture. Enter: ')
    k = cv2.waitKey(0)
    if k == 27: 
        print("Exited!")
    elif k == ord('s'):
        cv2.imwrite('videocapnew'+str(i)+'.jpg',bigger)
        print("Saved!")
    cv2.destroyAllWindows()
    return

def mirroring(i):
    img = cv2.imread('videocap'+str(i)+'.jpg',1)
    cv2.imshow('image',img)
    cv2.waitKey(2000)
    cv2.destroyWindow('image')
    img = cv2.flip(img, 1)
    cv2.imshow('mirroredimage',img)
    print('Press ESC to quit and s to save the video capture. Enter: ')
    k = cv2.waitKey(0)
    if k == 27: 
        print("Exited!")
    elif k == ord('s'):
        cv2.imwrite('videocapnew'+str(i)+'.jpg',img)
        print("Saved!")
    cv2.destroyAllWindows()
    return

def rotating(i):
    img = cv2.imread('videocap'+str(i)+'.jpg',1)
    cv2.imshow('image',img)
    cv2.waitKey(2000)
    cv2.destroyWindow('image')
    angle = int(input('Enter angle: '))
    img = imutils.rotate(img, angle)
    cv2.imshow('rotatededimage',img)
    print('Press ESC to quit and s to save the video capture. Enter: ')
    k = cv2.waitKey(0)
    if k == 27: 
        print("Exited!")
    elif k == ord('s'):
        cv2.imwrite('videocapnew'+str(i)+'.jpg',img)
        print("Saved!")
    cv2.destroyAllWindows()
    return