from dotenv import load_dotenv
from pathlib import Path

import os

load_dotenv()


def get_llm_provider() -> str:
    return os.getenv("LLM_PROVIDER", "mock")


def get_llm_api_key() -> str | None:
    return os.getenv("LLM_API_KEY")


def get_llm_model() -> str | None:
    return os.getenv("LLM_MODEL")


def get_llm_base_url() -> str | None:
    return os.getenv("LLM_BASE_URL")


def get_memory_path() -> Path:
    return Path(
        os.getenv(
            "MEMORY_PATH",
            "conversation.json",
        )
    )