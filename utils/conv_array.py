import numpy as np


def conv_array(arr, window_size):
    window = np.ones(window_size) / window_size
    res = np.convolve(arr, window, mode='full')
    res = res[int(window_size/2)-1:int(res.size-int(window_size/2))]
    return res


def diff_array(arr):
    res = np.diff(arr)
    res = np.append(res, res[res.size-1])
    return res


def filter_np_array(arr, threshold=0.2):
    max_value = max(np.max(arr), abs(np.min(arr)))
    threshold = threshold * max_value
    arr[np.abs(arr) < threshold] = 0
    return arr


if __name__ == "__main__":
    b = np.array([1, 3, 2, 5, 7])
    print(diff(b))
