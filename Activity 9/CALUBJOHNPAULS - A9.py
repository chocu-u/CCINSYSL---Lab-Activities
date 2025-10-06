import piexif
from PIL import Image
import os

def extract_exif_data(image_path):
    """
    Extract EXIF metadata from an image file
    """
    try:
        # Load the image
        img = Image.open(image_path)
        
        # Get EXIF data
        exif_dict = piexif.load(img.info.get('exif', b''))
        
        # Extract specific metadata
        camera_make = "Unknown"
        camera_model = "Unknown"
        date_time_original = "Unknown"
        
        # Get camera make
        if piexif.ImageIFD.Make in exif_dict['0th']:
            camera_make = exif_dict['0th'][piexif.ImageIFD.Make].decode('utf-8')
        
        # Get camera model
        if piexif.ImageIFD.Model in exif_dict['0th']:
            camera_model = exif_dict['0th'][piexif.ImageIFD.Model].decode('utf-8')
        
        # Get original date/time
        if piexif.ExifIFD.DateTimeOriginal in exif_dict['Exif']:
            date_time_original = exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal].decode('utf-8')
        
        return camera_make, camera_model, date_time_original
        
    except Exception as e:
        print(f"Error reading EXIF data: {e}")
        return None, None, None

def main():
    # Path to the image file - updated to include folder path
    image_path = os.path.join("Activity 9", "Canon_DIGITAL_IXUS_400.jpg")
    
    # Check if file exists
    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' not found!")
        return
    
    print("EXIF Metadata Analysis:")
    print("-" * 30)
    
    # Extract EXIF data
    make, model, date_time = extract_exif_data(image_path)
    
    if make or model or date_time:
        print(f"Camera Make: {make}")
        print(f"Camera Model: {model}")
        print(f"Date/Time Original: {date_time}")
    else:
        print("No EXIF data found or error occurred during extraction.")

if __name__ == "__main__":
    main()