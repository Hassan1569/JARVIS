# Architecture — JARVIS

## 1. High-Level System

flowchart TD
    U[User] -->|text/voice| UI[PySide6 UI]
    UI --> ORCH[Orchestrator]
    ORCH --> LLM[LLM Provider / Ollama or OpenAI-compatible]
    ORCH --> REG[Tool Registry]
    REG --> TOOLS[Approved Python Tools]
    TOOLS --> SYS[OS / FS / Network]
    ORCH --> MEM[Memory Manager]
    MEM --> DB[(SQLite)]
    VOICE[Voice Pipeline] --> ORCH
    ORCH --> VOICE
    ORCH --> PERM[Permission Gate]
    PERM --> UI

## 2. Component Responsibilities

| Component | Responsibility |
|---|---|
| desktop/window.py | PySide6 main window, chat panel, status, system panel |
| app/core/orchestrator.py | Runs the request to plan to tool-call to reply loop |
| app/core/llm.py | LLMProvider ABC + concrete providers (Ollama, OpenAI-compatible) |
| app/core/intent.py | Fast pre-classification (chat vs. tool-intent) - optional optimization |
| app/core/tool_registry.py | Registers tool schemas; validates args; dispatches execution |
| app/core/permissions.py | Confirmation prompts for destructive tools |
| app/voice/* | Wake-word, STT, TTS, audio routing (Phase 2) |
| app/tools/* | Concrete tool implementations (Phase 3+) |
| app/memory/* | SQLite conversation store + memory manager (Phase 4) |
| app/productivity/*, app/knowledge/* | Phase 5 |
| app/database/* | Engine/session, models |
| app/config.py | Loads .env, exposes typed settings |
| app/main.py | Entry point; wires dependencies; launches UI |

## 3. AI Orchestration Loop

1. User submits message to Orchestrator.handle(user_msg).
2. Orchestrator builds context (recent conversation + memory + tool schemas).
3. Sends to LLMProvider.chat(messages, tools=schemas).
4. LLM returns either a natural reply or a structured tool_call.
5. If tool_call: validate against schema, check permissions, execute, feed result back to LLM, loop (max N iterations).
6. Final reply returned to UI.

## 4. LLM Provider Abstraction

class LLMProvider(ABC):
    @abstractmethod
    def chat(self, messages: list[dict], tools: list[dict] | None = None) -> LLMResponse: ...
    @abstractmethod
    def stream(self, messages: list[dict], tools: list[dict] | None = None) -> Iterator[str]: ...

- OllamaProvider: HTTP to OLLAMA_BASE_URL.
- OpenAICompatProvider: OpenAI SDK pointed at any compatible base URL (covers OpenAI, DeepSeek, custom).
- Selection via config.llm_provider.

## 5. Tool Execution Workflow

LLM tool_call -> ToolRegistry.validate(name, args) -> Permissions.require(name, args) (if sensitive) -> tool.execute(**args) -> result back to LLM. NEVER eval/exec LLM text.

## 6. Memory Architecture (Phase 4)

- conversation_store: append-only messages (id, role, content, ts).
- memory_manager: user-approved facts (id, key, value, ts, source).
- Future: vector_store (ChromaDB) for semantic recall.

## 7. Database Schema (initial)

CREATE TABLE conversations (
  id INTEGER PRIMARY KEY,
  role TEXT NOT NULL,           -- 'user' | 'assistant' | 'tool'
  content TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE memories (
  id INTEGER PRIMARY KEY,
  key TEXT,
  value TEXT NOT NULL,
  source TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

## 8. Voice Pipeline (Phase 2)

Mic -> ring buffer -> openWakeWord ("hey jarvis") -> Faster-Whisper STT -> Orchestrator -> Piper TTS -> Speaker. Interrupt on new wake word or user input.

## 9. Security Boundaries

- LLM sees tool schemas, not code.
- All tool arguments validated by pydantic/explicit check.
- Permission gate for: file delete, software install, message send, system shutdown.
- Secrets: only config.py reads .env; nothing else touches raw env.

## 10. Error Handling

- Every tool wrapped in try/except -> returns structured ToolResult(ok, error).
- Orchestrator converts tool errors into LLM-visible messages (agent can recover).
- UI surfaces final errors; logs capture stack traces without secrets.

## 11. Technology Decisions

| Concern | Decision | Reason |
|---|---|---|
| UI | PySide6 | Native, mature, LGPL |
| LLM | Provider-agnostic | User choice + cost |
| STT | Faster-Whisper | CPU-friendly, accurate |
| TTS | Piper | Fast, offline |
| Wake | openWakeWord | Lightweight |
| DB | SQLite | Zero-config, local |
| System | psutil | Standard |
| Config | python-dotenv | Simple, standard |

Deferred: FastAPI (not needed until remote control phase), Playwright (Phase 5 web), ChromaDB (Phase 4+).