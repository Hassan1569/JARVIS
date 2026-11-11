# Product Requirements Document — JARVIS

## 1. Overview
JARVIS is a private, modular AI desktop assistant for Windows 10/11 that accepts voice and text commands, reasons over natural-language requests via an LLM, and executes approved actions through a controlled Python tool layer. It is not a chatbot wrapper; it is an agentic command center.

## 2. Problem Statement
Existing desktop assistants are either cloud-locked (privacy loss), script-bound (no reasoning), or LLM-only (no safe execution). Users need a local-first, extensible assistant that can reason, act, and remember — without surrendering control.

## 3. Product Vision
A professional AI productivity tool where the user speaks or types naturally, and JARVIS plans, selects tools, executes, and reports — with strict safety boundaries and full transparency.

## 4. Target Users
- Power users / developers on Windows who want automation.
- Privacy-conscious users preferring local LLMs.
- Researchers building on an open, modular assistant foundation.

## 5. Core Features (summary)
| Module | Capability |
|---|---|
| Voice | Wake-word, STT, TTS, interruptible speech |
| AI Brain | Intent, planning, tool selection, context, recovery |
| Windows Automation | Launch apps, files, system control |
| Memory | SQLite-backed persistent memory, user-controlled |
| Web Research | Search, retrieve, summarize, cite |
| Productivity | Notes, tasks, reminders, timers |
| Document Intelligence | PDF/DOCX read + QA |
| System Intelligence | CPU/RAM/disk/battery monitoring |

## 6. Functional Requirements
- FR-1: Accept text input and return LLM-reasoned responses.
- FR-2: Accept voice input gated by wake word "Hey Jarvis".
- FR-3: Route user intent to a registered tool when applicable.
- FR-4: Require confirmation for destructive/irreversible actions.
- FR-5: Persist user-approved memories and conversation history.
- FR-6: Support provider-swappable LLMs (Ollama + OpenAI-compatible API).
- FR-7: Show live execution status (planning / executing / done / failed).
- FR-8: Expose a memory inspector UI (list, search, delete).
- FR-9: Log all tool invocations with timestamps.
- FR-10: Allow voice interruption of TTS output.

## 7. Non-Functional Requirements
- NFR-1: Startup < 3s on 16GB RAM / no GPU.
- NFR-2: Text response latency dominated by LLM, not UI (<100ms UI overhead).
- NFR-3: Modular — every module independently testable.
- NFR-4: Type-hinted, PEP 8 compliant.
- NFR-5: Runs offline for non-LLM features.
- NFR-6: Cross-provider LLM abstraction (< 30 LOC to add a provider).

## 8. Security Requirements
- SR-1: LLM output is never `exec()`'d.
- SR-2: All actions go through a tool registry with typed schemas.
- SR-3: Secrets via `.env` only; never logged.
- SR-4: Destructive actions require explicit UI confirmation.
- SR-5: Memory records are user-inspectable and deletable.
- SR-6: Microphone state visible whenever listening.

## 9. MVP Scope (Phase 1)
- PySide6 window, dark navy UI.
- Text conversation with LLM (Ollama or API).
- Conversation display + input box.
- Config via `.env`.
- Basic logging.

## 10. Future Scope
Voice (P2), tools (P3), memory (P4), productivity + docs + web (P5), advanced agent (P6).

## 11. Acceptance Criteria (MVP)
- App launches without error.
- User types a message → LLM responds correctly.
- Provider switchable via `.env` without code changes.
- No hardcoded responses; all replies originate from the configured LLM.
- Errors are surfaced to the user, not silently swallowed.