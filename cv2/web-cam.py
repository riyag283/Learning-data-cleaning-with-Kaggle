import cv2
def show_webcam(mirror=False):
    i = 121
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if mirror: 
            img = cv2.flip(img, 1)
        cv2.imshow('my webcam', img)
        print('Press ESC to quit and s to save the video capture')
        k = cv2.waitKey(0)
        if k == 27: 
            print("Exited!")
            break  # esc to quit
        elif k == ord('s'):
            cv2.imwrite('videocap'+str(i)+'.jpg',img)
            print("Saved!")
            break
    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()