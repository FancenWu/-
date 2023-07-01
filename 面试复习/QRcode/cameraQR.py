import cv2
import csv
import pyzbar.pyzbar as pyzbar


def decodeDisplay(image):
    barcodes = pyzbar.decode(image)

    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (225, 225, 225), 2)

        barcodeData = barcode.data.decode('utf-8')
        barcodeType = barcode.type

        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255), 2)

        print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
    return image

def detect():
    camera = cv2.VideoCapture(0)

    while True:
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        im = decodeDisplay(gray)

        cv2.waitKey(5)
        cv2.imshow("camera", im)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyWindow()

if __name__ == '__main__':
    detect()