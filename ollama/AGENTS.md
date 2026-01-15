# Module Context
**Role:** Local LLM Inference Engine (Native).
**Dependencies:** High RAM usage, Metal (GPU) acceleration.

# Tech Stack & Constraints
- **Core:** Ollama (macOS Native App).
- **Service Management:** `launchd` via `LaunchAgents`.
- **Config:** Environment variables injected via plist.

# Operational Commands
- **Start/Restart:** `pkill Ollama && open -a Ollama` (or via plist reload).
- **Reload Config:** `launchctl unload ~/Library/LaunchAgents/com.ollama.startup.plist && launchctl load ~/Library/LaunchAgents/com.ollama.startup.plist`.
- **Logs:** `/tmp/ollama.log` and `/tmp/ollama.err`.

# Implementation Patterns
- **Native Execution:** Runs directly on host for maximum Metal performance.
- **Env Injection:** Uses `com.ollama.startup.plist` to set `HOST`, `ORIGINS`, etc.

# Local Golden Rules
## Do's & Don'ts
- **DO** use the hybrid plist approach (Env var injection + App Auto-restart).
- **DO** restart the app manually if environment variables don't seem to apply.
- **DON'T** run Ollama via Docker on this machine (Metal performance penalty).
- **DON'T** rely on macOS "Login Items" for startup; use the plist.
