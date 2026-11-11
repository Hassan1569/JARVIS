# Project Rules — JARVIS Constitution

These rules are mandatory. Any code that violates them is rejected.

## 1. Code Quality
- Python 3.12+, PEP 8, 4-space indent, max line 100.
- Type hints on all public functions.
- No print() in application code — use logging.
- No wildcard imports (from x import *).
- No dead code, no commented-out blocks committed.
- Functions do one thing; keep under ~50 lines when reasonable.

## 2. Folder Organization
- Respect the structure in architecture.md.
- New modules must live in the correct package.
- No new top-level folders without updating architecture.md.
- __init__.py in every Python package.

## 3. Naming
- Files/modules: snake_case.py.
- Classes: PascalCase. Functions/vars: snake_case. Constants: UPPER_SNAKE.
- Private: leading _.
- Tool names: verb_noun (e.g. open_app, list_files).

## 4. Security
- NEVER exec(), eval(), or compile() LLM output.
- NEVER commit .env, API keys, tokens, DB dumps, user data.
- ALWAYS route actions through ToolRegistry.
- ALWAYS validate tool args.
- ALWAYS require confirmation for: delete, move, install, send, shutdown.
- ALWAYS log tool invocation with sanitized args (no secrets).

## 5. API Integration
- All external calls go through app/core/llm.py (LLM) or a dedicated *_client.py.
- Never call HTTP directly from UI or tools.
- Timeouts on every network call (default 30s).
- Retry once on transient network error; then surface.
- No hardcoded endpoints — use config.py.

## 6. Error Handling
- No bare except:.
- Catch specific exceptions; log with context; return structured result.
- Tool errors never crash the orchestrator; they become messages to the LLM.
- UI shows a user-friendly error; logs show the technical detail.

## 7. Logging
- logging module only; configured in app/main.py.
- Log level from JARVIS_LOG_LEVEL.
- Logs to logs/jarvis.log with rotation.
- Never log API keys, full user messages in DEBUG unless explicitly enabled.

## 8. Testing
- pytest for all non-UI logic.
- Every tool has a test for happy path + argument rejection.
- LLM provider tested with a mock (no live API in unit tests).
- UI tested manually; keep UI logic thin.

## 9. Dependencies
- Add to requirements.txt only when the phase needs it.
- Pin versions (==) in requirements.txt.
- Prefer stdlib when sufficient.
- No heavy model downloads at install time.

## 10. Documentation
- Update tasks.md when tasks move status.
- Update memory.md at end of every phase.
- Public functions have docstrings (1–3 lines).
- No stale docs.

## 11. Git
- Conventional commits: feat:, fix:, docs:, chore:, refactor:, test:.
- One logical change per commit.
- Never commit data/, logs/, .env, __pycache__.
- Commit only at phase completion.

## 12. Token-Efficient Development
- Never regenerate files that are correct.
- Target minimal diffs.
- No exploratory boilerplate.
- Ask before expanding scope.