import face_recognition
import cv2
import numpy as np

original_face_img = "images/man.png"


def find_face_part(face_part_name):
    face_image = face_recognition.load_image_file(original_face_img)
    face_landmarks_list = face_recognition.face_landmarks(face_image)
    return face_landmarks_list[0][face_part_name]


face_part_name = "right_eye"
face_part_name2 = "left_eye"
print(find_face_part(face_part_name))

face_img = cv2.imread(original_face_img)


# for coordinate in find_face_part(face_part_name):
#     cv2.drawMarker(
#         face_img,
#         coordinate,
#         color=(255, 0, 0),
#         makerType=cv2.MARKER_CROSS,
#         thickness=1
#     )

# このfillConvexPolyで塗りつぶし範囲と塗りつぶしの色を指定する
cv2.fillConvexPoly(face_img, np.array(find_face_part(face_part_name)), color=(0, 0, 0))
# find_face_partはnumpyの形式じゃないとだめ
cv2.fillConvexPoly(face_img, np.array(find_face_part(face_part_name2)), color=(0, 0, 0))

cv2.imshow("Image", face_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
