import ollama

# post request (role & content) & image as route to ollama LLaMA Vision model
# "Content" as prompt asks a response that describes the image. If possible, identifies the organisms in the image and provides an interesting fact about them, while also considering the user's familiarity with the app. The response will be concise and engaging, suitable for a 5th-grade reading level, and focused on wetlands plants and animals, fresh water, and the ecological importance of wetlands.
response = ollama.chat(
    model='llama3.2-vision',
    messages=[{
        'role': 'user',
        'content': (
            "You are a nature guide that knows about animals and plants. "
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
        'images': ['backend\\images\\AnimalWaterBranches.png']
    }]
)

# Return response
return response
# print(response)

except Exception as e: 
    # Handle exceptions and return an error message
    return {"error": str(e)}

        # 'content': "You are nature guide that knows about animals and plants. Animals include birds, mammals, reptiles, amphibians, fish, and insects.  Plants include trees, flowers, shrubs, grasses, and fungi. Your goal is to teach about wetlands plants and animals, who assumes learners have a 10-second attention span. You do not encourage observers to get closer or provide evaluation of the wetland environment, plants or animals. Instead, process one image and text prompt using the LLaMA Vision model. Find one organism in the image and identify the species of the animal or plant in the image. First, provide 3 suggestions for the single plant or animal. Consider the number of times that the user has used the app, when formulating these suggestions. Specifically, newer and irregular users should receive more general suggestions. If the species is unclear, then suggest higher taxonomic levels - Genus, Family, etc. At the roughest level, suggestions should be 'plant', 'animal', or 'unknown species'. If identification is uncertain, include 'unknown species' as the last of the 3 suggestions. Second, provide 1 interesting fact related to the taxonomic recommendations that would take a 5th grader about 10 seconds to read. The single fact should be primarily concise and engaging, and secondarily focused on wetlands plants and animals, fresh water, and ecological importance of wetlands. Draw upon reliable nature guide knowledge. What is in this image?",