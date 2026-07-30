from ai_assistant.core.assistant import Assistant
from ai_assistant.core.workflows import ChatWorkflow
from ai_assistant.core.llms import MockLLM
from ai_assistant.core.prompts import PromptBuilder
from ai_assistant.core.memory import MockMemory


def get_assistant() -> Assistant:
    workflow = ChatWorkflow(
        llm=MockLLM(),
        prompt_builder=PromptBuilder(),
        memory=MockMemory(),
    )

    return Assistant(workflow)