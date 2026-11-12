# Development Log — JARVIS

## Current Project Status
Phase 1 (Basic MVP) is complete. The app can hold text-based conversations with an LLM.

## Current Development Phase
Phase 1 Complete. Ready to start Phase 2 (Voice).

## Completed Features
- Phase 0: Project initialization, folder structure, documentation.
- Phase 1: PySide6 UI with dark theme, text input/output.
- Phase 1: LLM provider abstraction (Ollama + OpenAI-compatible).
- Phase 1: Local LLM integration tested successfully with `qwen3.5:4b`.

## Current Implementation
- `app/config.py`: Loads `.env` and manages settings.
- `app/core/llm.py`: `LLMProvider` ABC with `OllamaProvider` (using OpenAI compatible endpoint) and `OpenAICompatProvider`.
- `app/core/orchestrator.py`: Manages conversation history and sends requests to LLM.
- `desktop/window.py`: PySide6 UI with chat display and input field.
- `app/main.py`: Entry point and logging setup.

## Important Technical Decisions
- Switched `OllamaProvider` to use the OpenAI-compatible `/v1` endpoint instead of the legacy `/api/chat` endpoint for better stability.
- Used Python `threading` in the UI to prevent the app from freezing while waiting for the LLM response.

## Known Issues
- None for Phase 1.

## Dependencies Installed
- PySide6, python-dotenv, openai, requests, pytest.
- Local AI Model: `qwen3.5:4b` via Ollama.

## Next Immediate Task
Phase 2 — Add Voice capabilities (STT, TTS, Wake word).