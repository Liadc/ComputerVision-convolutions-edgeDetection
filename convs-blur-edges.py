import numpy as np
import cv2


def conv1D(inSignal: np.ndarray, kernel1: np.ndarray) -> np.ndarray:
    flippedKernel = np.copy(kernel1)
    signalCopy = np.copy(inSignal)
    flippedKernel = flippedKernel[::-1]  # convolution with flipped kernel

    for i in range(flippedKernel.size-1):  # zero padding
        signalCopy = np.insert(signalCopy, 0, 0)
        signalCopy = np.append(signalCopy, [0])
    print("zero padding: " + str(signalCopy))
    signalConvolved = np.array([])  # building convolved signal into this array.
    # print(np.dot(signalCopy[0:flippedKernel.size], flippedKernel))
    for i in range(signalCopy.size-flippedKernel.size+1):
        signalConvolved = np.append(signalConvolved, np.dot(signalCopy[i:i+flippedKernel.size], flippedKernel))
    signalConvolved = signalConvolved.astype(int)  # optional. array might be doubles (images with values 0 to 1).

    return signalConvolved


#  main:
try:
    array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    kernel = np.array([1, 2, 3, 4])
    print(np.convolve(array, kernel))
    print(conv1D(array, kernel))
    # img = cv2.imread("./pics/toyota.jpg", 0)
    # cv2.imshow("Original image", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    pass
except ValueError as err:
    print(err.args)
