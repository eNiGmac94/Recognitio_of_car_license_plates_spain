import cv2
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
placa = []
patron=('[0-9]{4}[\s](?!.*(LL|CH))[BCDFGHJKLMNPRSTVWXYZ]{3}')
matricula = re.compile(patron)

image = cv2.imread('Imgs/coche3.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#gray = cv2.blur(gray, (3, 3))
canny = cv2.Canny(gray, 150, 200)
#canny = cv2.dilate(canny, None, iterations=1)
cv2.imshow('Image2', canny)

# _,cnts,_ = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cnts, _ = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(image,cnts,-1,(0,255,0),2)

for c in cnts:
    area = cv2.contourArea(c)

    x, y, w, h = cv2.boundingRect(c)
    epsilon = 0.09 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)

    if area > 1000:
        aspect_ratio = float(w) / h
        if aspect_ratio > 2.4:
            placa = gray[y:y + h, x:x + w]
            text = pytesseract.image_to_string(placa, config='--psm 8')

            if matricula.search(text):
                    if (len(text) > 9):
                        text1 = text[1 : 9]
                        if (len(text1) < 9):
                            text = text[0: 9]
                            #print('PLACA1:', text)
                            #print('area=', area)
                            # cv2.drawContours(image,[approx],0,(0,255,0),3)

                            #cv2.imshow('PLACA', placa)
                            #cv2.moveWindow('PLACA', 780, 10)
                            #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
                            #cv2.putText(image, text, (x - 20, y - 10), 1, 2.2, (0, 255, 0), 3)
                        print('PLACA11:', text1)
                        print('area=', area)
                        # cv2.drawContours(image,[approx],0,(0,255,0),3)

                        cv2.imshow('PLACA', placa)
                        cv2.moveWindow('PLACA', 780, 10)
                        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
                        cv2.putText(image, text1, (x - 20, y - 10), 1, 2.2, (0, 255, 0), 3)
                    else:

                        print('longitud text:', len(text))
                        print('PLACA111:', text)
                        print('area=', area)
                        # cv2.drawContours(image,[approx],0,(0,255,0),3)

                        #cv2.imshow('PLACA', placa)
                        cv2.moveWindow('PLACA', 780, 10)
                        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
                        cv2.putText(image, text, (x - 20, y - 10), 1, 2.2, (0, 255, 0), 3)
            else:
                if len(text)==9:
                    text = text[0: 9]
                    print('PLACA:', text)
                    print('area=', area)
                    # cv2.drawContours(image,[approx],0,(0,255,0),3)

                    cv2.imshow('PLACA', placa)
                    cv2.moveWindow('PLACA', 780, 10)
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    cv2.putText(image, text, (x - 20, y - 10), 1, 2.2, (0, 255, 0), 3)


cv2.imshow('Image', image)
cv2.moveWindow('Image', 45, 10)
cv2.waitKey(0)