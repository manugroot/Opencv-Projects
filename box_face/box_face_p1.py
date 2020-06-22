import cv2
img = cv2.imread("C:\\Users\\Akhila reddy\\Desktop\\New folder\\DSCN0025.JPG")
face_cascade = cv2.CascadeClassifier("C:\\Users\\Akhila reddy\\AppData\\Roaming\\Python\\Python37\\site-packages\\cv2\\haar-cascade-files-master\\haarcascade_frontalface_default.xml")
img = cv2.resize(img,(600,600))
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("cvbn",gray_img)

faces = face_cascade.detectMultiScale(img,scaleFactor = 1.05,minNeighbors=5)

for x,y,w,h in faces:
    img = cv2.rectangle(img , (x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow("sd",img)
cv2.waitKey(0)
cv2.destroyAllWindows()