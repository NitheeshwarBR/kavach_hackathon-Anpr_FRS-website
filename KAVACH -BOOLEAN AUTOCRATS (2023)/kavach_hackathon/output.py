import cv2
import imutils
import pytesseract
# plate = pytesseract.image_to_string(Cropped_loc, lang='eng')
# print("Number plate is:", plate)
pytesseract.pytesseract.tesseract_cmd='C://Program Files//Tesseract-OCR//tesseract.exe'

image=cv2.imread('C://Users//nithe//OneDrive//Desktop//kavach_hackathon//Images//8.jpg')
image=imutils.resize(image,width=300)
cv2.imshow("original image",image)
cv2.waitKey(0)

gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("greyed image",gray_image)
cv2.waitKey(0)

gray_image=cv2.bilateralFilter(gray_image,11,17,17)
cv2.imshow("smoothened image",gray_image)
cv2.waitKey(0)

edged=cv2.Canny(gray_image,30,200)
cv2.imshow("edged image",edged)
cv2.waitKey(0)

cnts,new=cv2.findContours(edged.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
image1=image.copy()
cv2.drawContours(image1,cnts,-1,(0,255,0),3)
cv2.imshow("countours",image1)
cv2.waitKey(0)

cnts=sorted(cnts,key=cv2.contourArea,reverse=True)[:50]
screenCnt=None
image2=image.copy()
cv2.drawContours(image2,cnts,-1,(0,255,0),3)
cv2.imshow("Top 30 contours",image2)
cv2.waitKey(0)
cv2.waitKey(0)
i=7
for c in cnts:
    perimeter=cv2.arcLength(c,True)
    approx=cv2.approxPolyDP(c,0.018*perimeter,True)
    if len(approx)==4:
        screenCnt=approx
        x,y,w,h=cv2.boundingRect(c)
        new_img=image[y:y+h,x:x+w]
        cv2.imwrite('C://Users//nithe//OneDrive//Desktop//kavach_hackathon//'+str(i)+'.jpg',new_img)
        i+=1
        break
    
cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
cv2.imshow("image with detected license plate", image)
cv2.waitKey(0)

Cropped_loc = 'C://Users//nithe//OneDrive//Desktop//kavach_hackathon//7.jpg'
final_image=cv2.imread(Cropped_loc)
cv2.imshow("cropped",final_image)
text = pytesseract.image_to_string(final_image, lang='eng')
print("Number  Detected Plate Text : ",text)
cv2.waitKey(0)
cv2.destroyAllWindows()

