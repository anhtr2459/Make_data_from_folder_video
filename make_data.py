import cv2 
import os
path_video = 'Mọi người add folder mọi người tải các video ở đây'

Files = os.listdir(path_video)
i = 0

for File in Files:
    vPath = os.path.join(path_video,File)
    print(vPath)
    video = cv2.VideoCapture(vPath)
    while video.isOpened():
        ret,frame = video.read()
        if ret == False:
            break
        # cv2.imshow('Video',frame)
        if i % 5 == 0:
            path_img="Mọi người add folder mọi người lưu các hình ảnh extrac từ ở đây" + str(i) + ".png"
            cv2.imwrite(path_img,frame)
           
        i += 1
        if cv2.waitKey(1) & 0xFF== ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()