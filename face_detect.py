# I've left some code in comments so that it can be easier if one wants to test and see output at various points. To make things simpler just remove the commented code !

def detect_face(img):
    import cv2
    camera = cv2.VideoCapture(0)

    # return_value, image= camera.read()
    # cv2.imwrite('opencv.png',image)
    # del(camera)

    cascPath = "haarcascade_frontalface_default.xml"

    # Create haar cascade

    faceCascade = cv2.CascadeClassifier(cascPath)

    # return_value, image = camera.read()
    image = img

    # input("Press ENTER looking at the camera to capture your image !")
    # cv2.imwrite('opencv.png', image)


    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30)
    )

    if len(faces) == 0:
        return None
    else:
        # print("Found {0} faces !".format(len(faces)))

        # Find the largest face
        largest_face_index = 0
        largest_face_size = 0

        for i, (x, y, w, h) in enumerate(faces):
            face_size = w * h
            if face_size > largest_face_size:
                largest_face_size = face_size
                largest_face_index = i

        x, y, w, h = faces[largest_face_index]

        cv2.rectangle(image, (x, y), (x+w, y+h), (255,255,255), 0)
        sub_face = image[y:y+h, x:x+w]

        cv2.imshow("Face crop", sub_face)
        camera.release
        cv2.imshow("Faces found", image)
        cv2.waitKey(0)
        del cv2
        return sub_face
