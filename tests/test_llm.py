from app.core.llm import get_llm_provider, LLMProvider

def test_get_llm_provider():
    provider = get_llm_provider()
    assert isinstance(provider, LLMProvider)