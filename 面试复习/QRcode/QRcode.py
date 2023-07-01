import os.path
import cv2
import qrcode

data = 'http://www.baidu.com'
image = qrcode.make(data=data)
image.show()
image.save("baidu.png")

def plotQR(box_size, border, fill_color, back_color):
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    data = 'https://www.baidu.com/'
    qr.add_data(data)
    qr.make(fit=True)
    image = qr.make_image(fill_color=fill_color, back_color=back_color)
    fn = f"baidu_{box_size}_{border}_{fill_color}_{back_color}.png"
    image.save(fn)
    return fn
exampleList = [
    (15, 3, 'blue', 'white'),
    (15, 3, 'red', 'green'),
    (10, 2, 'yellow', 'grey'),
    (5, 1, 'pink', 'black'),
]
[plotQR(*arg) for arg in exampleList]

def detectQR(img):
    img = cv2.imread(img)
    det = cv2.QRCodeDetector()
    val, pts, st_code = det.detectAndDecode(img)
    print(val)

detectQR("baidu.png")
