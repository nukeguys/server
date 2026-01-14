---
trigger: always_on
---

# Gravity Operational Standards

## 1. Context First
- **Golden Rule:** Before acting, **ALWAYS** read the `AGENTS.md` in the current directory and the root definitions. These files contain the specific technical constraints (networks, versions, log limits).
- **Precedence:** If this file conflicts with `AGENTS.md`, `AGENTS.md` is the source of truth.

## 2. Documentation Hygiene
- **Sync Documentation:** If you change the project structure, network configuration, or service settings, **immediately** update the relevant `AGENTS.md` file.
- **Traceability:** Maintain a specific "Change History" or audit trail as requested in the local context files.

## 3. Security Mindset
- **Secrets:** Never hardcode passwords, tokens, or keys. Always use `.env` files.
- **Verification:** After deploying or updating a service, actively verify the status (e.g., check logs, health status) instead of just assuming the command succeeded.

## 4. Directory & Path Discipline
- **Containment:** Keep service configurations managed within their independent subdirectories.
- **Portability:** Use relative paths (e.g., `./data`) in configurations to ensure the project remains portable.