from abc import ABC

from ai_assistant.core.embedders import BaseEmbedder


def test_base_embedder_is_abstract():

    assert issubclass(BaseEmbedder, ABC)