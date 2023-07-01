import numpy as np


# 卷积神经网络计算公式: N = (输入大小F - 卷积核大小 + 2 padding)/ 步长大小 + 1

# IOU
def bb_IOU(boxA, boxB):
	boxA = [int(x) for x in boxA]
	boxB = [int(x) for x in boxB]
	xA = max(boxA[0], boxB[0])
	yA = max(boxA[1], boxB[1])
	xB = min(boxA[2], boxB[2])
	yB = min(boxA[3], boxB[3])

	interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
	boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
	boxBArea = (boxB[2] - box[0] + 1) * (boxB[3] - boxB[1] + 1)
	iou = interArea / float(boxAArea + boxBArea - interArea)
	return iou



	
