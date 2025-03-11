# 🧑‍💻 Face Detection with OpenCV and DNN 📸

This is a Python application that detects faces in an image using OpenCV's DNN-based face detection model. The program uses TensorFlow's pre-trained model for better accuracy (75%+ confidence). A simple GUI built with Tkinter allows you to select an image, detect faces, and display the result.

## 🚀 Features

- 👁️ Accurate face detection using DNN (Deep Neural Networks).
- 🖼️ Simple GUI built with Tkinter to load and display images.
- 🔍 Face detection with confidence threshold of 75% or higher.
- 🔄 Resizes the image to fit the window while maintaining aspect ratio.

## ⚙️ Requirements

- Python 3.x
- OpenCV
- Pillow
- NumPy
- Tkinter (usually comes pre-installed with Python)

## 🛠️ Installation

1. Open CMD 🖥️


| **Operating System** | **Steps**                                                                                                                   |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------|
| **Windows** 💻        | 1. Press `Windows + R` to open the "Run" dialog box. <br> 2. Type `cmd` and hit `Enter`. <br> 3. The Command Prompt (CMD) will open. <br> Alternatively, you can search for "Command Prompt" in the Start menu and click to open it. 🔍 <br> 4. To navigate to the Desktop, type `cd %USERPROFILE%\Desktop` and hit `Enter`. 📂        |
| **Linux** 🐧          | 1. Press `Ctrl + Alt + T` to open the terminal. <br> 2. Alternatively, search for "Terminal" in your applications menu. 💨 <br> 3. To navigate to the Desktop, type `cd ~/Desktop` and hit `Enter`. 📂        |


2. Clone the repository:
```bash
git clone https://github.com/LaithALhaware/Fast-Face-Detection-with-OpenCV.git
cd face-detection-opencv
```

3. Install the required dependencies :
```bash
pip install -r requirements.txt
```

## 🚀 Usage 
1- Run the script:
```bash
python face_detection.py
```
2- Click the **Open Image** button to load an image.

3- The application will detect faces in the image and display them with rectangles.

4- You can adjust the confidence threshold in the code if needed (default is 75%).

## 📝 Code Explanation
- **DNN Model**: We use OpenCV's DNN module with a pre-trained TensorFlow face detection model for more accurate face detection.
- **GUI**: Tkinter is used to create a simple interface for opening and displaying images.
- **Confidence Filtering**: The program only detects faces with confidence greater than 75%.



## 📝 License
[[License](LICENSE)] ⚖️


## ❤️ Support This Project
If you find this project useful, consider supporting its development:

💰 Via PayPal: [[PayPal Link](https://www.paypal.com/ncp/payment/KC9EETJDVZQHG)]

Your support helps keep this project alive! 🚀🔥
