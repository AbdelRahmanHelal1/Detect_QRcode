import cv2
import numpy as np

qr=cv2.QRCodeDetector()

# تحديد ملف الفيديو وفتحه باستخدام OpenCV
cap = cv2.VideoCapture(0)

# تعريف BarCodeReader

new = []
# حلقة لمعالجة الإطارات الفردية من الفيديو والكشف عن رمز الاستجابة السريعة
while True:
    # قراءة الإطار التالي من الفيديو
    ret, frame = cap.read()

    # التحقق من وجود إطار جديد
    if not ret:
        break

    # تحويل الإطار إلى grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    x, y, z = qr.detectAndDecode(frame)
    if x :
        point = np.array(y, dtype=int)
        if  x not in new:


            cv2.polylines(frame, [point], True, (0, 255, 0), 10)
            new.append(x)
        else:
            cv2.polylines(frame, [point], True, (0, 0, 255), 5)

    cv2.imshow("image",frame)

    if cv2.waitKey(1)==ord("s"):
        print(set(new))
        break

# إفراغ الموارد
cap.release()
cv2.destroyAllWindows()