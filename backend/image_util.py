# Base64 encoding is a general utility, may be used beyond Ollama model...
# So separated from model file: model_RAG_response.py

# Base64 encoding import to prep for "def..." function in this file
import base64

# Base64 encoding function to a new file (image_utils.py). 
# connect them by importing the function from image_utils.py
from image_util import convert_image_to_base64

# The Base64 encoding must be done before calling ollama.chat, as the encoded string 
# needs to be prepared and passed in the images parameter of the API call.
image_path = 'images_preUpload/AnimalWaterBranches.png'  # Relative path to the image file
base64_string = convert_image_to_base64(image_path)  # Convert the image to a Base64 string
print(base64_string)  # Print the Base64 string to verify it was created correctly

# Base64 encoding function to a new file (image_utils.py). You can connect them by importing the function from image_utils.py
def convert_to_base64(image_path):
    """Convert an image to a Base64-encoded string.
    """
    with open(image_path,"rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')