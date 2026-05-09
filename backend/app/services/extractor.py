from groq import Groq
from app.services.models import ExtractResult 
import os
import json

client = Groq(api_key = os.getenv("GROQ_API_KEY"))

def extract_knowledge(text : str) -> ExtractResult:
    prompt = f"""
    Extract entities and relationships from the following text.
    Return ONLY valid JSON in this format:
    {{
        "entities": ["entity1", "entity2"],
        "triples": [
            {{
                "subject": "A",
                "relation": "RELATION",
                "target": "B"
            }}
        ]
    }}
    
    Text: {text}
    """

    chat_completion = client.chat.completions.parse(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="llama-3.3-70b-versatile",
        temperature = 0
    )
    content = chat_completion.choices[0].message.content
    data = json.loads(content)

    return ExtractResult(**data)