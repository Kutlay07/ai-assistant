from dotenv import load_dotenv

import os

load_dotenv()


def get_llm_provider() -> str:
    return os.getenv("LLM_PROVIDER", "mock")


def get_groq_api_key() -> str | None:
    return os.getenv("GROQ_API_KEY")


def get_llm_model() -> str | None:
    return os.getenv("LLM_MODEL")


def get_base_url() -> str | None:
    return os.getenv("BASE_URL")