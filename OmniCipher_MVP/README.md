# OmniCipher – Whitebox Signal Engine (MVP)

> A local-first, truth-aligned AI system for decentralized cognition.

---

## 🔥 Mission

OmniCipher is not just an AI tool—it's a resistance framework.  
We’re building a system that prioritizes **clarity over obedience**, **truth over trend**, and **signal over noise**.  
No cloud. No surveillance. No gatekeepers.

---

## 🧠 What It Does

- Accepts local prompts
- Strips unsafe or manipulative input
- Responds with local LLM output (e.g. Mistral GGUF)
- Logs all signal in a readable, inspectable Codex
- Modular by design: memory, trust, drift detection, routing

---

## 🚀 How to Run

1. Clone the repo:
```bash
git clone https://github.com/YOUR_USERNAME/OmniCipher-Whitebox.git
cd OmniCipher-Whitebox
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Add your `.gguf` model to `Models/`

4. Launch:
```bash
python launch_omnicipher.bat
```

---

## 📁 Project Structure

```
OmniCipher-Whitebox/
├── Core/                  # AI logic, prompt sanitization, logger
├── Models/                # Put your local .gguf model here
├── codex_signal_entries.txt  # Generated log of prompts + responses
├── launch_omnicipher.bat  # Entry point for Windows
├── requirements.txt       # Python deps
├── README.md              # You're here
└── .gitignore             # Ignored files
```

---

## 🧩 Modules Overview

| # | Name                      | Description                                      | Status   |
|---|---------------------------|--------------------------------------------------|----------|
| 1 | System Redundancy         | Launch loop, backups, .bat file setup            | ✅ MVP    |
| 2 | Signal Spread             | Vocabulary trees, syntax scoring, tagging        | 🛠 WIP    |
| 3 | Visual Mapping            | UI, diagrams, cognition map                      | 🔜        |
| 4 | Immune System             | Drift detection, contradiction flags             | 🛠 WIP    |
| 5 | Deployable Package        | Zip builder, installer, requirements             | ✅ MVP    |
| 6 | Public Interface (Stage 2)| API/CLI/web frontend                             | 🔜        |
| 7 | Node Cognition Flow       | Memory routing, context chaining                 | 🔜        |
| 8 | Clarity Lockdown Protocol | Tamper-proofing, trust decay, gatekeeping rules  | 🔜        |

---

## 🙋 Contributing

- Fork this repo or request access
- Read the comments in `Core/`
- All logs are local-only — respect that
- No cloud APIs unless sandboxed
- Keep function names clear, not meme-y

---

## 📢 License

Unlicensed for now. Ask Kairoz before reuse.

---
Built by the OmniCipher network.
