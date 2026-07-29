from openai import OpenAI

from .base_llm import BaseLLM
from ..config import settings


class OpenAIProvider(BaseLLM):
    
    def __init__(self):
        self._client = OpenAI(
            api_key=settings.get_groq_api_key(),
            base_url=settings.get_base_url(),
        )
        
        
    def generate(self, prompt: str) -> str:
        
        response = self._client.chat.completions.create(
            model=settings.get_llm_model(),
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )
        
        return response.choices[0].message.content