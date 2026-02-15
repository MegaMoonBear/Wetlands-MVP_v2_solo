import ollama
from backend.image_util import convert_image_to_base64         # Import the Base64 utility function

# Base64 encoding is a general utility, may be used beyond Ollama model...
# So separated from model file: model_RAG_response.py
image_path = 'images_preUpload/AnimalWaterBranches.png'  # Relative path to the image file

try: 
    base64_image = convert_image_to_base64(image_path)  # Convert the image to a Base64 string
except FileNotFoundError:
    print(f"Error: The image file at '{image_path}' was not found. Please check the path and try again.")
    exit(1)  # Exit the program with an error code
except OSError as e:                # OS error related to file handling (e.g., permissions, file corruption)
    print(f"Error: An OS error occurred while processing the image. Details: {str(e)}")
    exit(1)  # Exit the program with an error code

# Print the Base64 string to verify it was created correctly
print(base64_image)


# post request (role & content) & image as route to ollama LLaMA Vision model
# "Content" as prompt asks a response that describes the image. 
try: 
    response = ollama.chat(
    model='llama3.2-vision',
    messages=[{
        'role': 'user',
        'content': (
            "You are a nature guide that knows about water, wetlands, animals, and plants. "
            "Animals include birds, mammals, reptiles, amphibians, fish, and insects. "
            "Plants include trees, flowers, shrubs, grasses, and fungi. "
            "Your goal is to teach about wetlands plants and animals, assuming learners have a 10-second attention span. "
            "You do not encourage observers to get closer or evaluate the wetland environment. "
            "Instead, process one image and text prompt using the LLaMA Vision model. "
            "First, describe the image and provide common names—not genus and species. "
            "If species is unclear, suggest higher taxonomic levels (e.g., Genus, Family). "
            "At the roughest level, suggestions should be 'plant', 'animal', or 'unknown species'. "
            "Second, provide 1 interesting fact related to the taxonomic recommendations that would take a 5th grader about 10 seconds to read. "
            "The fact should be concise, engaging, and focused on wetlands plants and animals, fresh water, and the ecological importance of wetlands. "
            "What is in this image?"
        ),
        # Relative path to image file on local machine. 
            # useful for debugging 
            # may not be necessary in production, because uploaded to server and path may be different
        'images': [base64_image]
    }]
)
# Handle exceptions and return an error message
except Exception as e: 
    print(f"Error: Failed to process the image and generate a response. Details: {str(e)}")
    exit(1)  # Exit the program with an error code

# Return response
print(response)
