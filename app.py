import cv2

face  = cv2.CascadeClassifier(r"OpenCV\Project\haarcascade_frontalface_default.xml")
eye   = cv2.CascadeClassifier(r"OpenCV\Project\haarcascade_eye.xml")
smile = cv2.CascadeClassifier(r"OpenCV\Project\haarcascade_smile.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frames = cap.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    faces = face.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2) 

        roi_gray  = gray[y:y+h, x:x+w]
        roi_color = frames[y:y+h, x:x+w]

        eyes = eye.detectMultiScale(roi_gray, 1.1, 10)
        if len(eyes) > 0:
            cv2.putText(frames, "Eyes Detected", (x, y-30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

        smiles = smile.detectMultiScale(roi_gray, 1.7, 20)
        if len(smiles) > 0:
            cv2.putText(frames, "Smiling", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    cv2.imshow("Smart Face Detector", frames)
    if cv2.waitKey(1) & 0xff == ord('q'):       
        break

cap.release()
cv2.destroyAllWindows()