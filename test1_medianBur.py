import cv2, copy

import util_select_corners

img = cv2.imread("./example_dir/cropped/example_frame_0.png")
# cornors = util_select_cornor.select_cornor(img)
# print(cornors)

orig_img = copy.deepcopy(img)
output2 = cv2.medianBlur(img, 41)  # 模糊程度為 25
cv2.imshow('oxxostudio1', orig_img)
cv2.imshow('oxxostudio2', output2)
cv2.imwrite("bur_example0.png", output2)
cv2.waitKey(0)
cv2.destroyAllWindows()
