# Development Log — JARVIS

## Current Project Status
Initialization complete. Documentation being finalized. No application code exists yet.

## Current Development Phase
Phase 0 — Initialization & Documentation (STEP 2).

## Completed Features
- Folder structure created via PowerShell script.
- .gitignore, .env.example, README.md, requirements.txt stub.
- Six documentation files populated (this step).

## Current Implementation
None. No Python source files exist.

## Important Technical Decisions
- LLM provider abstraction from day one (ABC in core/llm.py) — allows Ollama + OpenAI-compatible without refactor.
- No code generation from LLM — tool registry + schema validation only.
- SQLite-first memory; ChromaDB deferred to Phase 4 optional.
- Provider default = Ollama but OpenAI/DeepSeek ready via env.
- PySide6 chosen (native Windows, LGPL, mature).
- Phase ordering — voice deferred to P2 because P1 proves the loop first (cheapest validation).
- No FastAPI in MVP — not needed until/unless remote control is required.

## Known Issues
- None yet.

## Dependencies Installed
- None (requirements.txt is placeholder).

## Next Immediate Task
Complete STEP 3 — cross-validate the six documents for consistency, then request approval to begin Phase 1.