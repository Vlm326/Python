import cv2
from PySimpleGUI import popup_get_file


def getPhoto():
    img = cv2.imread(popup_get_file('choose photo', no_window=True), cv2.IMREAD_GRAYSCALE)
    cv2.imshow('car',img)
    cv2.waitKey(0)
    cv2.imwrite('car',img)

def main():
    getPhoto()

if __name__ == "__main__":
    main()