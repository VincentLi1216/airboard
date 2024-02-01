import cv2
img = cv2.imread('./example.png')

# 要畫的點座標
points_list = [(80, 20), (20, 80)]

def show_xy(event,x,y,flags,userdata):
    print(event,x,y,flags)
    '''
    state:
    0->hover
    1->click
    2->drag
    3->release
    '''
    state = 0
    # 印出相關參數的數值，userdata 可透過 setMouseCallback 第三個參數垂遞給函式


def draw_points(img, points_list=[], defualt_points=True):
    
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
    for point in points_list:
        cv2.circle(img, point, point_size, point_color, thickness)
    

    return img

if __name__ == "__main__":

    img = draw_points(img,points_list)

    cv2.imshow('Select ROI', img)
    cv2.setMouseCallback('Select ROI', show_xy)  # 設定偵測事件的函式與視窗

    cv2.waitKey(0)     # 按下任意鍵停止
    cv2.destroyAllWindows()
