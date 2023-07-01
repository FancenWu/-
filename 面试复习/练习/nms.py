import numpy as np


def nms(dets, thresh):
    """
    :param dets: [[x1, y1, x2, y2, score], []]
    :param thresh: 0.0 - 1.0
    :return: keep dets
    """

    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    scores = dets[:, 4]

    areas = (x2 - x1 + 1) * (y2 - y1 + 1)  # why add 1 ?

    order = scores.argsort()[::-1]
    keep = []

    while order.size > 0:
        i = order[0]
        keep.append(i)

        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])

        # they could be negative number when two boxes have no intersection
        w = np.maximum(0.0, xx2 - xx1 + 1)
        h = np.maximum(0.0, yy2 - yy1 + 1)
        inter = w * h
        over = inter / (areas[i] + areas[order[1:]] - inter)
        # Find the IoU that is not higher than threshold
        index = np.where(over <= thresh)[0]

        order = order[index + 1]

    return keep


if __name__ == "__main__":
    dets = np.array([[310, 30, 420, 5, 0.6],
                     [20, 20, 240, 210, 1],
                     [70, 50, 260, 220, 0.8],
                     [400, 280, 560, 360, 0.7]])
    # 设置阈值
    thresh = 0.4
    keep_dets = nms(dets, thresh)
    # 打印留下的框的索引
    print(keep_dets)
    # 打印留下的框的信息
    print(dets[keep_dets])
