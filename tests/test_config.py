from app.config import Config

def test_config_loads():
    assert Config.LLM_PROVIDER is not None
    assert Config.USER_NAME is not None