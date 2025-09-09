from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Example: control HTTP timeout, default API base, etc.
    http_timeout: int = 15
    api_base_url: str = "https://httpbin.org"
    model_config = SettingsConfigDict(env_file=".env", env_prefix="PYTOOL_")
