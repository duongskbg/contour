import cv2,glob,shutil
import numpy as np

#load img
list_path_ok = glob.glob(r'D:\IVIS\test7\7-OK\*.jpg')
list_path_NG = glob.glob(r'D:\IVIS\test7\7-NG\*.jpg')
#tim gia tri contour
def find_contour (list_path):   
    # list_path = glob.glob(r'C:\Users\V1032437\Desktop\New folder\8\fail2\*.jpg')
    list_contour = []    
    for path in list_path:   
        img = cv2.imread(path)
        #crop image
        crop_img = img[0:180,70:110]
        #convert img to grey
        img_grey = cv2.cvtColor(crop_img,cv2.COLOR_BGR2GRAY)
        #set a thresh
        thresh = 100
        #get threshold image
        ret,thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)
        #find contours
        contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        list_contour.append(len(contours))           
        # #create an empty image for contours
        # img_contours = np.zeros(img.shape)
        # # draw the contours on the empty image
        # cv2.drawContours(img_contours, contours, -1, (0,255,0), 3)
    TB_contour = sum(list_contour)/len(list_contour)
    return TB_contour
TB = (find_contour(list_path_ok) + find_contour(list_path_NG)) / 2
print('gia tri so sanh',TB)

#du doan
def predict (img):
    crop_img = img[0:180,70:110]
    #convert img to grey
    img_grey = cv2.cvtColor(crop_img,cv2.COLOR_BGR2GRAY)
    #set a thresh
    thresh = 100
    #get threshold image
    ret,thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)
    #find contours
    contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) >= ( TB-1 ):
        pre = 2          
    else :
        pre = 8
    return pre    

#tesst img
img = cv2.imread(r'C:\Users\V1032437\Desktop\New folder\7\10.220.40.215-None-1659673942.0497108.jpg')
pre = predict(img)
print(pre)
