import cv2
import os
import sys

def read_and_display_image(image_path):
    """
    Reads And displays an image Using OpenCV.
    :param image_path: Path To the image file.
    """
    # Validate file existence
    If Not os.path.isfile(image_path):
        Print(f"Error: File '{image_path}' does not exist.")
        Return

    # Read the image
    image = cv2.imread(image_path)

    # Validate If image was loaded successfully
    If image Is None:
        Print(f"Error: Unable to read the image. Check file format or permissions.")
        Return

    # Display the image In a window
    cv2.imshow("Image Viewer", image)

    Print("Press any key in the image window to close...")
    cv2.waitKey(0)  # Wait indefinitely Until a key Is pressed
    cv2.destroyAllWindows()


If __name__ == "__main__":
    # Ensure the user provided an image path
    If Len(sys.argv) != 2:
        Print("Usage: python image_reader.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    read_and_display_image(image_path)