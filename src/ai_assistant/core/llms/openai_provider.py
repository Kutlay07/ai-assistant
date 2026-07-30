from openai import OpenAI

from .base_llm import BaseLLM
from ..config import settings


class OpenAIProvider(BaseLLM):
    
    def __init__(self):
        api_key = settings.get_llm_api_key()
        base_url = settings.get_llm_base_url()
        model = settings.get_llm_model()

        if not api_key:
            raise ValueError("LLM_API_KEY is not configured.")

        if not base_url:
            raise ValueError("LLM_BASE_URL is not configured.")

        if not model:
            raise ValueError("LLM_MODEL is not configured.")

        self._model = model

        self._client = OpenAI(
            api_key=api_key,
            base_url=base_url,
        )
        
        
    def generate(self, prompt: str) -> str:
        
        response = self._client.chat.completions.create(
            model=self._model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )
        
        return response.choices[0].message.content
    
    def stream(self, prompt):
        yield self.generate(prompt)