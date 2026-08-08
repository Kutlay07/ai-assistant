from dotenv import load_dotenv
from dataclasses import dataclass
from pathlib import Path
import os

load_dotenv()

@dataclass(frozen=True)
class Settings:
    llm_provider: str
    llm_api_key: str | None
    llm_model: str | None
    llm_base_url: str | None

    memory_path: Path
    postgres_connection_string: str

    environment: str

    def __post_init__(self):
        if self.environment not in ("development", "production"):
            raise ValueError("Invalid environment")


def load_settings() -> Settings:
    return Settings(
        llm_provider=os.getenv("LLM_PROVIDER", "mock"),
        llm_api_key=os.getenv("LLM_API_KEY"),
        llm_model=os.getenv("LLM_MODEL"),
        llm_base_url=os.getenv("LLM_BASE_URL"),
        memory_path=Path(
            os.getenv("MEMORY_PATH", "conversation.json"),
        ),
        postgres_connection_string=os.getenv(
            "POSTGRES_CONNECTION_STRING",
            "postgresql://ai_assistant:ai_assistant@localhost:5432/ai_assistant",
        ),
        environment=os.getenv(
            "ENVIRONMENT",
            "development",
        ),
    )


settings = load_settings()