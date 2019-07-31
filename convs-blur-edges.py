import numpy as np
import cv2


def conv1D(inSignal: np.ndarray, kernel1: np.ndarray) -> np.ndarray:
    flippedKernel = np.copy(kernel1)
    signalCopy = np.copy(inSignal)
    flippedKernel = flippedKernel[::-1]  # convolution with flipped kernel

    for i in range(flippedKernel.size - 1):  # zero padding
        signalCopy = np.insert(signalCopy, 0, 0)
        signalCopy = np.append(signalCopy, [0])
    # print("zero padding: " + str(signalCopy))
    outSignal = np.array([])  # building convolved signal into this array.
    # print(np.dot(signalCopy[0:flippedKernel.size], flippedKernel))
    for i in range(signalCopy.size - flippedKernel.size + 1):
        outSignal = np.append(outSignal, np.dot(signalCopy[i:i + flippedKernel.size], flippedKernel))
    outSignal = outSignal.astype(int)  # optional. array might be doubles (images with values 0 to 1).

    return outSignal


def conv2D(inImage: np.ndarray, kernel2: np.ndarray) -> np.ndarray:
    inImageCopy = np.copy(inImage)
    kernel2Copy = np.copy(kernel2)

    outImage = kernel2Copy
    return outImage


#  main:
try:
    # Convolve 1d test:
    array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    kernel = np.array([1, 2, 3, 4])
    print(np.convolve(array, kernel))
    print(conv1D(array, kernel))  # should be the same output printed as np.convolve()
    print("Are they same? " + str((conv1D(array, kernel) == np.convolve(array, kernel)).all()))
    # Convolve 2d test:
    # img = cv2.imread("./pics/toyota.jpg", 0)
    #
    # kernel = np.array([[1, 2, 1],
    #                    [3, 4, 0],
    #                    [0, 1, 3]], np.int32)
    #
    # imgFiltered = cv2.filter2D(img, -1, kernel)
    # print(imgFiltered)

    # Show image:
    # img = cv2.imread("./pics/toyota.jpg", 0)
    # cv2.imshow("Original image", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    pass
except ValueError as err:
    print(err.args)
