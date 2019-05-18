import getopt
import time
import face_recognition
import cv2
from tkinter import *
from PIL import Image
import numpy as np
import os


DATA_FOLDER="./img/"

def usage():
    print("""
        Usage::
            python3  piSentinel.py -h shows this help()
            python3  piSentinel.py -t <face_name>  to make piSentinel learn your face
            python3  piSentinel.py -s              to make piSentinel search some known face
            
        Info:: 
            Press Key 'q' to exit camera frame and save data learning
    """)


def learn(name):
    video_capture = cv2.VideoCapture(0)
    face_counter = 0
    while True:
        ret, frame = video_capture.read()
        cv2.imshow("PiSentinel Learning your Face", frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            face_locations = face_recognition.face_locations(frame)
            print("Faces Found: ".format(len(face_locations)))
            for face_location in face_locations:

                top, right, bottom, left = face_location
                print("Face detected at Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
                face_image = frame[top:bottom, left:right]
                image_name = name + "_N"+str(face_counter) + str(time.strftime("_%Y%m%d%H%M")) + '.jpg'
                cv2.imwrite(DATA_FOLDER + image_name, face_image)
                face_counter += 1
                Image.fromarray(face_image).show(title=image_name)

            break

    video_capture.release()
    cv2.destroyAllWindows()


def search():
    known_face_encodings = []
    known_face_names = []

    directory = os.fsencode(DATA_FOLDER)

    if len(os.listdir(directory)) == 1: print("You have not teach me any faces yet!");usage();exit(0);


    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".jpg"):
            print("Loading and Learning: "+os.path.join(DATA_FOLDER, filename))
            input_image = face_recognition.load_image_file(os.path.join(DATA_FOLDER, filename))
            input_face_encoding = face_recognition.face_encodings(input_image)[0]
            known_face_encodings.append(input_face_encoding)
            known_face_names.append(filename.split(".")[0])

            continue
        else:
            print("NOT Supported input: "+os.path.join(DATA_FOLDER, filename))
            continue




    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    video_capture = cv2.VideoCapture(0)
    while True:

        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:

            # Find all the faces and face encodings in the current frame
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imshow("PiSentinel Searching for Faces", frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()

def main(argv):

    face_name = None
    try:
        opts, args = getopt.getopt(argv,"ht:s")
    except getopt.GetoptError:
        print ('python3 piSentinel.py -h')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt == "-t":
            face_name = arg
            if face_name is not None: learn(face_name)
            else:
                print("<face_name> required")
                usage()
        elif opt == "-s":
            search()
        else:
            usage()
            sys.exit()

if __name__ == "__main__":
   main(sys.argv[1:])





