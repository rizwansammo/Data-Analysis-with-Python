#pip install face_recognition

import face_recognition

# Load the image
image_path = 'path_to_your_image.jpg'  # Replace with the actual path of your image
image = face_recognition.load_image_file(image_path)

# Find all face locations in the image
face_locations = face_recognition.face_locations(image)

# If no faces are found, exit
if len(face_locations) == 0:
    print("No faces found in the image.")
    exit()

# Load face landmarks for age and gender prediction
face_landmarks_list = face_recognition.face_landmarks(image)

# For each face, estimate age and gender
for (top, right, bottom, left), face_landmarks in zip(face_locations, face_landmarks_list):
    # Extract the face region
    face_image = image[top:bottom, left:right]

    # Use face landmarks for age and gender estimation
    # Note: You may need additional data (like a labeled dataset) for more accurate predictions
    # This example provides a basic illustration using landmarks
    # You can use more sophisticated models for better accuracy
    age = 30  # Placeholder for age estimation
    gender = "Male"  # Placeholder for gender estimation

    # Print the results
    print(f"Age: {age} years old")
    print(f"Gender: {gender}")

# Display the image with face rectangles (optional)
import cv2
for (top, right, bottom, left) in face_locations:
    cv2.rectangle(image, (left, top
