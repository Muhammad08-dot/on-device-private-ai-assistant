# Product Requirements Document (PRD): On-Device Private AI Assistant

## 1. Overview
The **On-Device Private AI Assistant** runs a local LLM (e.g., Llama‑3‑1B via Ollama) entirely offline, providing personal document RAG, task automation, and voice interaction without any internet connection. It is packaged as a lightweight desktop app (Tauri) that stores data in an encrypted SQLite vector DB.

## 2. Target Audience
- Privacy‑conscious users
- Professionals handling confidential data
- Developers needing an embeddable offline AI

## 3. Core Features
- **Local LLM Inference:** Runs via `ollama` or `llama.cpp` with a 1‑B/3‑B model.
- **Encrypted Vector Store:** SQLite + `sqlcipher` storing document embeddings locally.
- **RAG over Personal Docs:** Import PDFs/Word files, query via natural language.
- **Voice Interaction:** Whisper‑cpp for STT, Coqui TTS for offline synthesis.
- **Task Automation:** Simple python script execution based on user commands.
- **Cross‑Platform UI:** Tauri (HTML/CSS/JS) with a modern dark theme.

## 4. Technical Architecture
- **Backend:** Python service exposing a local HTTP API (FastAPI) to the Tauri frontend.
- **LLM Engine:** `llama.cpp` compiled with GGML for CPU‑only inference.
- **Embedding Model:** MiniLM‑v2 (onnx) for generating vectors.
- **Vector DB:** SQLite with `pgvector` extension (encrypted).
- **STT/TTS:** `whisper.cpp` and `coqui-tts` compiled for offline use.
- **Security:** End‑to‑end encryption of DB, optional password lock on app launch.

## 5. UI/UX Design
- Dark mode with teal accents.
- Sidebar: file import, settings, voice toggle.
- Main panel: chat interface showing user query, assistant response, and optional source snippets.
- Real‑time waveform visualizer for voice input.

## 6. Development Milestones
1. **M1:** Set up Tauri skeleton and integrate FastAPI backend.
2. **M2:** Implement local LLM inference wrapper.
3. **M3:** Add document import + embedding pipeline.
4. **M4:** Wire up Whisper‑cpp and Coqui TTS for voice.
5. **M5:** Build UI components and encryption flow.
6. **M6:** Final polish, README, and packaging.
