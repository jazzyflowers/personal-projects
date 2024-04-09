# Ex.1
import cv2
import numpy as np

WIDTH = 240
HEIGHT = 160
cam = cv2.VideoCapture('Lane Detection Test Video-01.mp4')

while True:
    ret, frame = cam.read()
    if ret is False:
        break
    frame = cv2.resize(frame, (WIDTH, HEIGHT))  # Ex.2
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Ex.3
    # Ex.4
    frame2 = np.zeros((HEIGHT, WIDTH), np.uint8);
    # 4-A. Incercam mai multe numere
    # 4-a-i
    upper_left = (WIDTH * 0.45, HEIGHT * 0.77)
    upper_right = (WIDTH * 0.55, HEIGHT * 0.77)
    lower_left = (0, HEIGHT)
    lower_right = (WIDTH, HEIGHT)
    trapezoid_array = [upper_left, lower_left, lower_right, upper_right]  # [pt1, pt2, pt3, pt4]
    arr = np.array(trapezoid_array, dtype=np.int32)  # 4-a-ii
    frame2 = cv2.fillConvexPoly(frame2, arr, 1)  # 4-a-iii
    mask = frame_gray * frame2  # ! inmultim gray*gray

    # Ex.5
    # am reorganizat cadrul de la trapez in ordine trigonometrica
    trapezoid_array = [upper_right, upper_left, lower_left, lower_right]  # ordine trigonom
    frame_array = [[WIDTH, 0], [0, 0], [0, HEIGHT], [WIDTH, HEIGHT]]
    trapezoid_bounds = np.float32(trapezoid_array)  # convertim in float32
    frame_bounds = np.float32(frame_array)
    stretch_perspective = cv2.getPerspectiveTransform(trapezoid_bounds,
                                                      frame_bounds)  # muta punctele dintr-o parte in alta a imag
    stretched = cv2.warpPerspective(mask, stretch_perspective, (WIDTH, HEIGHT))  #

    # Ex. 6
    blurred = cv2.blur(stretched, (7, 7))

    # Ex.7 - a
    sobel_vertical = np.float32([[-1, -2, -1],
                                 [0, 0, 0],
                                 [1, 2, 1]]
                                )
    sobel_horizontal = np.transpose(sobel_vertical)

    # Ex.7 - b
    sv_frame = cv2.filter2D(np.float32(blurred), -1, sobel_vertical)
    sh_frame = cv2.filter2D(np.float32(blurred), -1, sobel_horizontal)

    # Ex.7 - c
    filtered_frame = np.sqrt(sv_frame ** 2 + sh_frame ** 2)
    filtered_frame = cv2.convertScaleAbs(filtered_frame)

    # Ex.8
    _, binarized_frame = cv2.threshold(filtered_frame, 44, 255, cv2.THRESH_BINARY)

    # Ex.9 - a
    edge_filtered_frame = binarized_frame.copy()
    edge_filtered_frame[0:HEIGHT, int(WIDTH * 0.85):WIDTH] = 0
    edge_filtered_frame[0:HEIGHT, 0:int(WIDTH * 0.05)] = 0
    left_img = edge_filtered_frame[:, :int(WIDTH / 2.5)]
    right_img = edge_filtered_frame[:, int(WIDTH / 2.5):]

    # Ex.9 - b
    left_xs = [i[1] for i in np.argwhere(left_img > 0)]
    left_ys = [i[0] for i in np.argwhere(left_img > 0)]
    right_xs = [i[1] + WIDTH // 2.5 for i in np.argwhere(right_img > 0)]
    right_ys = [i[0] for i in np.argwhere(right_img > 0)]

    # Ex.10 - a
    try:  # more value errors that are ignored

        lp = np.polynomial.polynomial.polyfit(left_xs, left_ys, deg=1)  # = [b a] din ecuatia dreptei y = ax +b
        rp = np.polynomial.polynomial.polyfit(right_xs, right_ys, deg=1)
        if abs(lp[0]) < 10 ** 8:  # ignore bad values - verificam modulul
            # Ex.10 - b
            left_top_y = 0
            left_top_x = int((left_top_y - lp[0]) / lp[1])  # astea fiind float-uri le convertim in int sa nu dea eroare
            left_bottom_y = HEIGHT
            left_bottom_x = int((left_bottom_y - lp[0]) / lp[1])
            # Ex.10 - c
            left_top = int(left_top_x), int(left_top_y)
            left_bottom = int(left_bottom_x), int(left_bottom_y)
        if abs(rp)[0] < 10 ** 8:
            # Ex.10 - b
            right_top_y = 0
            right_top_x = int((right_top_y - rp[0]) / rp[1])
            right_bottom_y = HEIGHT
            right_bottom_x = int((right_bottom_y - rp[0]) / rp[1])
            # Ex.10 - c
            right_top = int(right_top_x), int(right_top_y)
            right_bottom = int(right_bottom_x), int(right_bottom_y)
    except:
        pass
    # Ex.10 - d
    # cv2.line(frame, point1, point2, color, width)
    cv2.line(edge_filtered_frame, left_top, left_bottom, (100, 0, 0), 5)
    cv2.line(edge_filtered_frame, right_top, right_bottom, (200, 0, 0), 5)

    #Ex.11
    lanes_frame = np.zeros((HEIGHT, WIDTH), np.uint8)
    cv2.line(lanes_frame, left_top, left_bottom, (100, 0, 0), 5)
    cv2.line(lanes_frame, right_top, right_bottom, (200, 0, 0), 5)
    normal_perspective = cv2.getPerspectiveTransform(frame_bounds, trapezoid_bounds)
    lanes_frame = cv2.warpPerspective(lanes_frame, normal_perspective, (WIDTH, HEIGHT))

    # cv2.imshow('Original',frame)
    cv2.imshow('Grey', frame_gray)
    cv2.imshow('Trapezoid', frame2)
    cv2.imshow('Road', mask)
    cv2.imshow('Top-Down', stretched)
    cv2.imshow('Filtered', filtered_frame)
    cv2.imshow('Binarized', binarized_frame)
    cv2.imshow('Edge frame', edge_filtered_frame)
    cv2.imshow('Lanes shown', lanes_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    print("I can make changes!")
cam.release
# cv2.destroyAllWindows()
