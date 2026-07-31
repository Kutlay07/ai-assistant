from ai_assistant.core.assistant import Assistant
from ai_assistant.core.workflows import ChatWorkflow
from ai_assistant.core.llms import create_llm
from ai_assistant.core.prompts import PromptBuilder
from ai_assistant.core.memory import MockMemory


def get_assistant() -> Assistant:
    workflow = ChatWorkflow(
        llm=create_llm(),
        prompt_builder=PromptBuilder(),
        memory=MockMemory(),
    )

    return Assistant(workflow)