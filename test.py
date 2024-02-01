import cv2
import copy
import math


img = cv2.imread('./example.png')
orig_img = copy.deepcopy(img)

# 要畫的點座標
points_list = []
points_color = [(0,0,255),(0,0,255),(0,0,255),(0,0,255)]

def dist(coord1, coord2):
    return ((coord1[0]-coord2[0])**2+(coord1[1]-coord2[1])**2)**0.5

state = 0
def show_xy(event,x,y,flags,userdata):
    global state
    global points_color
    # print(event,x,y,flags)
    '''
    state:
    0->hover
    1->click
    2->drag
    3->release
    '''
    state_mapping = {0:"hover", 1:"click", 2:"drag", 3:"release"}
    is_clicked = False

    if event == 1:
        is_clicked=True
    elif event ==4:
        is_clicked=False
        state=3

    if is_clicked and state==0:
        state=1

    if is_clicked and state==3:
        state=1
    
    if state==1 and event==0:
        state=2

    if state==3 and event==0:
        state=0






    if state == 1:
        for i in range(len(points_list)):
            if dist((x,y), points_list[i]) < 20:
                print("hi"*10, i)
                points_color = [(0,0,255),(0,0,255),(0,0,255),(0,0,255)]
                points_color[i] = (255, 0, 0)
                img = copy.deepcopy(orig_img)
                print(points_color)
                cv2.imshow('Select ROI', render(img, False))
                
    

    


    print(state_mapping[state], event)
    # 印出相關參數的數值，userdata 可透過 setMouseCallback 第三個參數垂遞給函式


def render(img, defualt_points=True):
    global points_list
    
    point_size = 5
    point_color = (0, 0, 255) # red
    thickness = -1
    
    # draw center 4 points
    if defualt_points:
        (height, width, _) = img.shape
        # print(height,width)
        points_list = []
        for ratio in [(3/4, 1/4), (1/4, 1/4), (1/4, 3/4), (3/4, 3/4)]:
            points_list.append((int(width*ratio[0]),int(height*ratio[1])))

    # print(points_list)

    # draw lines
    for i in range(len(points_list)):
        # last line
        if i == len(points_list)-1:
            img = cv2.line(img, points_list[0], points_list[i], (255,255,255), 2)
        # other lines
        else:
            img = cv2.line(img, points_list[i], points_list[i+1], (255,255,255), 2)
            pass
        
    # draw dots
    for index, point in enumerate(points_list):
        cv2.circle(img, point, point_size, points_color[index], thickness)
    

    return img

if __name__ == "__main__":

    img = render(img)

    cv2.imshow('Select ROI', img)
    cv2.setMouseCallback('Select ROI', show_xy)  # 設定偵測事件的函式與視窗

    cv2.waitKey(0)     # 按下任意鍵停止
    cv2.destroyAllWindows()
