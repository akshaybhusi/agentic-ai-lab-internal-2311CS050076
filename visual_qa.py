import os
from google import genai

# Create Gemini client
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# =====================================================
# IMAGE RETRIEVAL / VISUAL QA SYSTEM
# =====================================================

image_path = "image.jpg"

# Read image
with open(image_path, "rb") as f:
    image_data = f.read()

# Question about the image
question = """
Describe what is visible in this image.
Identify the main objects and explain what is happening.
"""

# Send image + question to Gemini
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=[
        {
            "inline_data": {
                "mime_type": "image/jpeg",
                "data": image_data
            }
        },
        question
    ]
)

# Display answer
print("\n========================================")
print("VISUAL QA SYSTEM")
print("========================================")

print("\nQuestion:")
print(question)

print("\nAnswer:")
print(response.text)

print("\n========================================")
print("MULTIMODAL PIPELINE COMPLETED")
print("========================================")
