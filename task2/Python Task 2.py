import re

text = """
Alice (25 years old) rated 4 stars. Feedback: Loved the app!
Bob is 30 and gave 5. Comment: Very useful, thanks!
Charlie, 22 yrs, score=3. Said: Needs improvement in UI.
Diana gave it a 4 but didn’t provide age. Comment: Works fine.
"""

def extract_survey_results(text: str) -> list:
    responses = text.strip().split("\n")
    structured = []

    for r in responses:
        useful_data = {}

        name = re.search(r"[A-Z][a-z]+", r)
        if name:
            useful_data["Name"] = name.group()

        age = re.search(r"(\d+)\s?(years|yrs|year)?", r)
        if age:
            useful_data["Age"] = int(age.group(1))
        
        rating = re.search(r"(rated|given|gave|score=)\s?(\d)", r)
        if rating:
            useful_data["Rating"] = int(rating.group(2))

        feedback = re.search(r"(Feedback|Comment|Said|Felt):\s?(.*)", r)
        if feedback:
            useful_data["Feedback"] = feedback.group(2)

        structured.append(useful_data)

    return structured

print("Output:", extract_survey_results(text), sep="\n")    

"""
Alice (25 years old) rated 4 stars. Feedback: Loved the app!
Bob is 30 and gave 5. Comment: Very useful, thanks!
Charlie, 22 yrs, score=3. Said: Needs improvement in UI.
Diana gave it a 4 but didn’t provide age. Comment: Works fine.
"""