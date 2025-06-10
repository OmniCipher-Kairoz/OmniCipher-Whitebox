OmniCipher — README.txt

OVERVIEW:
OmniCipher is a decentralized, whitebox AI architecture designed to retain semantic memory, detect drift, and transparently log reasoning chains. It is not a chatbot. It is a cognition engine — built to analyze its own logic, store provable memory, and allow public inspection of every decision layer.

---
FOLDER STRUCTURE (v2.0):

0_launch/
  - launch_Omnicipher.bat — Starts the full system.
  - lockdown.bat — Emergency lockdown protocol.

1_core/
  - Core AI logic (routing, prompt handling, memory recall, cognition flow)

2_codex/
  - Ground truth entries, logging tools, signal visualization, system spec

3_memory/
  - Session and memory logs, vector index, timestamped events

4_governance/
  - Trust systems, consensus, node metadata and scoring

5_interfaces/
  - User interaction endpoints (CLI/API/Web - currently minimal)

6_peers/
  - Peer node logic, merge handling, AI evaluation helpers

7_diagnostics/
  - Drift detection, scoring breakdowns, transparency reports

8_utils/
  - Stateless tools for import/export and snapshots

9_exports/
  - Final output: charts, JSONs, PDFs

Z_snapshots/
  - System state backups and locked history

---
STARTING THE SYSTEM:
1. Place your model (e.g., `mistral-7b-instruct.Q4_K_M.gguf`) in `/Models/`.
2. Run `0_launch/launch_Omnicipher.bat`
3. Use CLI or API endpoint (once configured) to begin input-output loop.

---
GOALS:
- Prevent memetic drift
- Allow humans to trace every output to its root
- Log every contradiction
- Check itself, not just others

---
NOTES:
- This version is a Minimum Viable Prototype (MVP).
- Every script includes clear logic or labeled handoff points.
- Contributions must not obscure logic or hide reasoning paths.
