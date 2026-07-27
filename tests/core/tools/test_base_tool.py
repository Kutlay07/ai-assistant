import pytest

from ai_assistant.core.tools import BaseTool


def test_base_tool_cannot_be_instantiated():
    with pytest.raises(TypeError):
        BaseTool()