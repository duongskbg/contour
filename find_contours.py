import cv2,glob,shutil
import numpy as np

# img = cv2.imread('D:/original.png', cv2.IMREAD_UNCHANGED)

#load data train
list_path_ok = glob.glob(r'D:\IVIS\test7\7-OK\crop\*.jpg')
list_path_NG = glob.glob(r'D:\IVIS\test7\7-NG\crop\*.jpg')

def find_contour (list_path):   
    # list_path = glob.glob(r'C:\Users\V1032437\Desktop\New folder\8\fail2\*.jpg')
    list_contour = []    
    for path in list_path:   
        img = cv2.imread(path)
        # #crop image
        # crop_img = img[0:180,70:110]
        #convert img to grey
        img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
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




'''============== Test====================================== '''
list_test = glob.glob(r'D:\IVIS\test7\7-OK\crop\*.jpg')
def find_pre ( list_img ):
    list_path_fail =[]
    list_path_ok =[]
    for path in list_img:     
        img = cv2.imread(path)
        #convert img to grey
        img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #set a thresh
        thresh = 100
        #get threshold image
        ret,thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)
        #find contours
        contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) >= (TB-1):
                list_path_ok.append(path)   
        else :
                list_path_fail.append(path)
    return list_path_ok , list_path_fail
#
pre_ok , pre_fail = find_pre(list_test)

print('So luong phan loai dung ' , len(pre_ok))
print('So luong phan loai sai ' , len(pre_fail))  

#move image
for path_ok in pre_ok:
    shutil.copy2(path_ok,'D:/IVIS/test7/7-OK/crop/PL_OK')
for path_NG in pre_fail:
    shutil.copy2(path_NG,'D:/IVIS/test7/7-OK/crop/PL_NG')

# # cv2.imshow('anh fail',cv2.imread(pre_ok[2]))
# # cv2.waitKey()












# #save image
# cv2.imwrite('D:/contours.png',img_contours) 

# cv2.imshow('goc',cv2.imread(list_path[0]))
# cv2.waitKey()

# #show
# img_sh = cv2.imread(list_path_fail[0], cv2.IMREAD_UNCHANGED)

# #convert img to grey
# img_grey = cv2.cvtColor(img_sh,cv2.COLOR_BGR2GRAY)
# #set a thresh
# thresh = 100
# #get threshold image
# ret,thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)
# #find contours
# contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# #create an empty image for contours
# img_contours = np.zeros(img_sh.shape)
# # draw the contours on the empty image
# cv2.drawContours(img_contours, contours, -1, (0,255,0), 3)
# #save image
# cv2.imshow('D:/contours.png',img_contours) 
# cv2.imshow('goc',img_sh)
# cv2.waitKey()
