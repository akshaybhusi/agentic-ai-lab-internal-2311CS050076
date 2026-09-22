import os
import time
from google import genai

# Create Gemini client
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

MODEL = "gemini-3.6-flash"


# =====================================================
# FUNCTION TO CALL GEMINI WITH RETRY
# =====================================================

def generate_response(prompt):
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=prompt
            )
            return response.text

        except Exception as e:
            print(f"\nAPI error. Attempt {attempt + 1}/3")
            print(e)

            if attempt < 2:
                print("Retrying in 5 seconds...")
                time.sleep(5)
            else:
                raise


# =====================================================
# INPUT TEXT
# =====================================================

text = """
Artificial Intelligence is a branch of computer science that focuses on
creating systems capable of performing tasks that normally require human
intelligence. AI is used in healthcare, education, finance, transportation,
agriculture and many other industries. Machine learning is a major part of
AI that allows systems to learn patterns from data. Deep learning uses neural
networks with multiple layers to solve complex problems. Generative AI can
create text, images, audio and code. As AI continues to develop, organizations
need to consider issues such as privacy, security, bias and responsible use.
"""


# =====================================================
# STEP 1: EXTRACT IMPORTANT INFORMATION
# =====================================================

prompt1 = f"""
Read the following text and extract the most important information.

Text:
{text}

Give the important facts and concepts as bullet points.
"""

key_points = generate_response(prompt1)

print("\n========================================")
print("STEP 1: KEY POINTS")
print("========================================")
print(key_points)


# =====================================================
# STEP 2: ORGANIZE INFORMATION
# =====================================================

prompt2 = f"""
Organize the following information into logical categories.

Information:
{key_points}

Create 3 to 5 categories and place the relevant points under each category.
"""

organized_points = generate_response(prompt2)

print("\n========================================")
print("STEP 2: ORGANIZED INFORMATION")
print("========================================")
print(organized_points)


# =====================================================
# STEP 3: GENERATE SUMMARY
# =====================================================

prompt3 = f"""
Using the organized information below, write a concise summary.

Information:
{organized_points}

Requirements:
- Use simple English
- Include the major concepts
- Do not add information that is not present
- Keep the summary between 100 and 150 words
"""

summary = generate_response(prompt3)

print("\n========================================")
print("STEP 3: SUMMARY")
print("========================================")
print(summary)


# =====================================================
# STEP 4: IMPROVE THE SUMMARY
# =====================================================

prompt4 = f"""
Improve the following summary.

Summary:
{summary}

Requirements:
- Correct grammar
- Remove unnecessary repetition
- Keep important information
- Use clear and simple language
- Keep it below 100 words
"""

final_summary = generate_response(prompt4)

print("\n========================================")
print("STEP 4: FINAL SUMMARY")
print("========================================")
print(final_summary)


# =====================================================
# EXPERIMENT COMPLETED
# =====================================================

print("\n========================================")
print("PROMPT CHAINING EXPERIMENT COMPLETED")
print("========================================")
