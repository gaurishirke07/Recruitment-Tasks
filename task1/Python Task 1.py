import re
from datetime import datetime

text = input('Enter Text: ')

def add_suffix(day: int) -> str:
    if 11 <= day <= 13:
        return f"{day}th"
    elif day%10 == 1:
        return f"{day}st"
    elif day%10 == 2:
        return f"{day}nd"
    elif day%10 == 3:
        return f"{day}rd"
    else:
        return f"{day}th"

def transform_text(text: str) -> str:
    text = re.sub(r"\b\d{5}-\d{5}\b", "[REDACTED]", text)

    def format_date(match):
        date_obj = datetime.strptime(match.group(), "%Y-%m-%d")
        day = add_suffix(date_obj.day)
        return f"{day} {date_obj.strftime('%B %Y')}"
    text = re.sub(r"\b\d{4}-\d{2}-\d{2}\b", format_date, text)

    text = text.replace("Python","🐍")
    return text


print('Output:', transform_text(text), sep='\n')

"""input: Call me at 98123-45678 on 2025-08-23. I love Python more than Java."""