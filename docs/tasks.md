# Development Roadmap — JARVIS

Legend — Priority: P0 (blocker), P1 (must), P2 (should), P3 (nice).
Status: todo | in-progress | done | blocked.

## Phase 0 — Initialization & Documentation
| ID | Task | Priority | Depends | Status | Acceptance |
|---|---|---|---|---|---|
| P0-1 | Create folder structure | P0 | — | done | Structure matches architecture.md |
| P0-2 | Populate 6 docs | P0 | P0-1 | in-progress | All six populated, cross-consistent |
| P0-3 | Validate doc consistency | P0 | P0-2 | todo | No contradictions |

## Phase 1 — Basic JARVIS (MVP)
| ID | Task | Priority | Depends | Status | Acceptance |
|---|---|---|---|---|---|
| P1-1 | config.py loading .env | P0 | P0-3 | todo | Typed settings; missing keys handled |
| P1-2 | core/llm.py provider ABC + Ollama + OpenAI-compat | P0 | P1-1 | todo | Both providers callable; switch via env |
| P1-3 | desktop/window.py basic window (chat + input) | P0 | P1-1 | todo | Launches, styled per design.md |
| P1-4 | core/orchestrator.py text-only loop | P0 | P1-2, P1-3 | todo | User msg → LLM reply displayed |
| P1-5 | main.py wiring + logging | P0 | P1-4 | todo | Runs from python -m app.main |
| P1-6 | Unit tests for config + LLM (mocked) | P1 | P1-2 | todo | pytest green |
| P1-7 | Update memory.md + commit | P0 | P1-6 | todo | Phase report delivered |

## Phase 2 — Voice
| ID | Task | Priority | Depends |
|---|---|---|---|
| P2-1 | Audio capture (audio_manager.py) | P1 | P1-7 |
| P2-2 | STT via Faster-Whisper | P1 | P2-1 |
| P2-3 | TTS via Piper (interruptible) | P1 | P2-1 |
| P2-4 | Wake word via openWakeWord | P1 | P2-1 |
| P2-5 | Wire voice ↔ orchestrator | P1 | P2-2, P2-3, P2-4 |
| P2-6 | Mic status UI indicator | P1 | P2-5 |

## Phase 3 — Tool Execution
| ID | Task | Priority | Depends |
|---|---|---|---|
| P3-1 | tool_registry.py + schema validation | P0 | P1-7 |
| P3-2 | permissions.py confirmation gate | P0 | P3-1 |
| P3-3 | application_tools.py (launch apps) | P1 | P3-1 |
| P3-4 | file_tools.py (search, create, list) | P1 | P3-1 |
| P3-5 | system_tools.py (CPU, RAM, battery) | P1 | P3-1 |
| P3-6 | Orchestrator tool-call loop | P0 | P3-1, P3-2 |
| P3-7 | Tests for each tool | P1 | P3-3..5 |

## Phase 4 — Persistent Memory
| ID | Task | Priority | Depends |
|---|---|---|---|
| P4-1 | DB engine + models | P0 | P3-6 |
| P4-2 | conversation_store.py | P1 | P4-1 |
| P4-3 | memory_manager.py (save/recall/delete) | P1 | P4-1 |
| P4-4 | Memory inspector UI | P2 | P4-3 |
| P4-5 | Optional: ChromaDB vector recall | P3 | P4-3 |

## Phase 5 — Productivity & Intelligence
| ID | Task | Priority |
|---|---|---|
| P5-1 | Notes | P2 |
| P5-2 | Tasks | P2 |
| P5-3 | Reminders + timers | P2 |
| P5-4 | Document reader (PDF/DOCX) | P1 |
| P5-5 | Document QA | P1 |
| P5-6 | Web search + summarize + cite | P1 |

## Phase 6 — Advanced Agent
| ID | Task | Priority |
|---|---|---|
| P6-1 | Multi-step planning with retry | P1 |
| P6-2 | Local LLM (Ollama) tuning | P2 |
| P6-3 | Error recovery heuristics | P1 |
| P6-4 | Self-evaluation / verification | P2 |
| P6-5 | Performance profiling | P2 |