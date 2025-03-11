import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

# Function to load and display the image
def load_image():
    global image, resized_image, image_rgb, image_pil, image_tk
    file_path = filedialog.askopenfilename()  # Open file dialog to choose an image
    if file_path:
        image = cv2.imread(file_path)

        # Convert image to grayscale for face detection
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Load Haar Cascade for face detection
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Detect faces in the image
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=2,  # Adjust the scale factor for more accurate results
            minNeighbors=6,   # Increase the number of neighbors to reduce false positives
            minSize=(30, 30)  # Minimum size of faces to detect
        )

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Resize the image to fit the Tkinter window, maintaining the aspect ratio
        resize_image()

# Function to resize the image
def resize_image():
    global resized_image, image_rgb, image_pil, image_tk

    max_width = 600  # Maximum width of the image in the window
    max_height = 400  # Maximum height of the image in the window

    img_height, img_width = image.shape[:2]

    # Calculate scale ratio and resize
    scale_ratio = min(max_width / img_width, max_height / img_height)
    new_width = int(img_width * scale_ratio)
    new_height = int(img_height * scale_ratio)

    resized_image = cv2.resize(image, (new_width, new_height))

    # Convert the image for display in Tkinter
    image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
    image_pil = Image.fromarray(image_rgb)
    image_tk = ImageTk.PhotoImage(image_pil)

    # Display the image in the Tkinter window
    panel.config(image=image_tk)
    panel.image = image_tk

# Function to save the image with faces
def save_image():
    global resized_image
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
    if file_path:
        cv2.imwrite(file_path, resized_image)
        messagebox.showinfo("Saved", "Image saved successfully!")

# Create the main window
window = tk.Tk()
window.title("Face Detection")
window.geometry("700x600")  # Adjust window size for better layout

# Style for buttons
style = ttk.Style()
style.configure("TButton",
                font=("Arial", 12),
                padding=10,
                relief="solid",
                width=15)

# Create a button to load an image
button_open = ttk.Button(window, text="Open Image", command=load_image)
button_open.pack(pady=10)

# Create a button to save the image
button_save = ttk.Button(window, text="Save Image", command=save_image)
button_save.pack(pady=10)

# Create a label to display the image
panel = tk.Label(window)
panel.pack(pady=20)

# Run the Tkinter event loop
window.mainloop()
