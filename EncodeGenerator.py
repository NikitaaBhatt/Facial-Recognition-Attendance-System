import cv2
import face_recognition
import pickle
import os
from openpyxl import Workbook

# Importing the employee images
folderPath = 'Images'
pathList = os.listdir(folderPath)
imgList = []
employeeIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    employeeIds.append(os.path.splitext(path)[0])

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

print("Encoding...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, employeeIds]
print("Encoding Completed...")

# Save the encoding file
file = open("EncodeFile.p", "wb")
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("Encode File Saved")