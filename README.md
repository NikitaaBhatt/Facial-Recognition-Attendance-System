# 🎯 Face Recognition Attendance System

![Python](https://img.shields.io/badge/python-v3.6.8+-blue.svg)
![OpenCV](https://img.shields.io/badge/opencv-4.x-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

An intelligent attendance management system that uses facial recognition technology to automatically track and record attendance. Built with Python, OpenCV, and the face_recognition library, this system provides a seamless, contactless solution for attendance management in educational institutions and workplaces.

## ✨ Features

- **Real-time Face Detection**: Instantly detects and recognizes faces from live video feed
- **Automated Attendance Logging**: Automatically records attendance with timestamp
- **CSV Data Management**: Stores and manages attendance data in CSV format
- **Multi-person Recognition**: Supports multiple individuals in the database
- **User-friendly Interface**: Simple and intuitive system operation
- **Duplicate Prevention**: Prevents multiple attendance entries for the same person
- **High Accuracy**: Uses state-of-the-art face recognition algorithms

## 🏗️ System Architecture

```
Face Recognition Attendance System
├── Images/                 # Training images directory
├── EncodeFile.p           # Encoded face data (pickle file)
├── students.csv           # Attendance records
├── main.py               # Main application file
├── encode_generator.py   # Face encoding generator
├── requirements.txt      # Project dependencies
└── README.md            # Project documentation
```

## 🚀 Quick Start

### Prerequisites

- Python 3.6.8 or higher
- Webcam/Camera
- C++ Desktop Development Tools ([Download here](https://code.visualstudio.com/docs/languages/cpp))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/NikitaaBhatt/Facial-Recognition-Attendance-System.git
   cd Facial-Recognition-Attendance-System
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare training data**
   - Create an `Images` folder in the root directory
   - Add face images of individuals (format: `PersonName.jpg`)
   - Ensure clear, front-facing photos for better accuracy

4. **Generate face encodings**
   ```bash
   python encode_generator.py
   ```

5. **Run the system**
   ```bash
   python main.py
   ```

## 📋 Requirements

```
opencv-python==4.5.1.48
face-recognition==1.3.0
dlib==19.22.0
pandas==1.2.3
numpy==1.20.1
cvzone==1.5.6
```

**⚠️ Important**: Use Python 3.6.8 and exact library versions as specified to avoid compatibility issues.

## 🎮 Usage

1. **Adding New Users**:
   - Place clear face images in the `Images` folder
   - Name files as `StudentID_Name.jpg` (e.g., `001_JohnDoe.jpg`)
   - Run the encoding generator to update the database

2. **Taking Attendance**:
   - Launch the main application
   - Position yourself in front of the camera
   - The system will automatically detect and record attendance
   - Check `students.csv` for attendance records

3. **Viewing Records**:
   - Open `students.csv` to view attendance data
   - Data includes: Student ID, Last Attendance Time, Total Attendance Count

## 🧠 How It Works

### 1. **Training Phase**
```python
# Load and process training images
folderPath = 'Images'
pathList = os.listdir(folderPath)
imgList = []
studentIds = []

for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])
```

### 2. **Face Encoding Generation**
```python
def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
```

### 3. **Real-time Recognition**
```python
# Capture and process video frames
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    
    # Detect faces and compare with known encodings
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)
    
    # Match faces and record attendance
    matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
```

## 🎯 Key Technologies

- **OpenCV**: Computer vision and image processing
- **Dlib**: Facial landmark detection and face alignment
- **face_recognition**: High-level face recognition operations
- **Pandas**: Data manipulation and CSV handling
- **NumPy**: Numerical computations
- **CVzone**: Enhanced OpenCV functionality

## ⚠️ Challenges & Limitations

| Challenge | Impact | Solution |
|-----------|---------|----------|
| **Lighting Conditions** | Affects recognition accuracy | Use consistent, well-lit environment |
| **Face Angles/Poses** | May cause recognition failure | Train with multiple angle images |
| **Facial Expressions** | Can impact matching | Include varied expression images |
| **Image Resolution** | Low quality reduces accuracy | Use high-resolution training images |
| **Aging Effects** | Features change over time | Periodically update training data |

## 🔧 Configuration

### Camera Settings
```python
cap = cv2.VideoCapture(0)  # Use default camera
cap.set(3, 640)           # Set width
cap.set(4, 480)           # Set height
```

### Recognition Threshold
Adjust face distance threshold for recognition sensitivity:
```python
# Lower values = stricter matching
tolerance = 0.6  # Default: 0.6
```

## 📊 Performance Optimization

- **Image Preprocessing**: Resize images to 25% for faster processing
- **Encoding Caching**: Store face encodings in pickle files
- **Frame Rate Control**: Process every nth frame for better performance
- **Memory Management**: Optimize image loading and processing

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🙋‍♀️ Author

**Nikita Bhatt**
- GitHub: [@NikitaaBhatt](https://github.com/NikitaaBhatt)
- Email: nikkitabhatt1020@gmail.com

## 🙏 Acknowledgments

- OpenCV community for excellent computer vision tools
- face_recognition library developers
- Dlib contributors for facial recognition algorithms
- Python community for comprehensive libraries

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/NikitaaBhatt/Facial-Recognition-Attendance-System/issues) section
2. Create a new issue with detailed description
3. Contact: nikkitabhatt1020@gmail.com

## 🚀 Future Enhancements

- [ ] Web-based dashboard for attendance management
- [ ] Mobile app integration
- [ ] Database integration (MySQL/PostgreSQL)
- [ ] Real-time notifications
- [ ] Advanced analytics and reporting
- [ ] Multi-camera support
- [ ] Cloud deployment options

---

⭐ **Star this repository if you found it helpful!**

*Built with ❤️ by Nikita Bhatt*
