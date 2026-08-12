<div align="center">
  <h1>🔒 On-Device Private AI Assistant</h1>
  <p><strong>100% Offline, Privacy-First AI Sandbox Powered by Local LLMs & Encrypted Vector Storage.</strong></p>
</div>

## 🚀 Overview
The **On-Device Private AI Assistant** is engineered for privacy-conscious users, enterprise legal teams, and developers handling sensitive code or confidential documents. It runs local LLMs (Llama 3, Mistral, Phi-3) completely air-gapped, ensuring zero telemetry and zero cloud data leaks.

![Dashboard Demo](/C:/Users/hp/.gemini/antigravity-ide/brain/fdf49048-b37f-4711-af04-f256131d4933/on_device_ai_dashboard_1786424208335.png)

## ✨ Features
- **100% Offline Inference:** Runs locally via Ollama / llama.cpp on CPU or GPU with 4-bit/8-bit quantization.
- **Encrypted Local RAG Vault:** Vectorizes PDFs, DOCX, and code files using local ONNX embeddings into an encrypted SQLite / ChromaDB store.
- **Air-Gap Security Verification:** Built-in hardware monitor to verify zero outbound network traffic.
- **Performance Diagnostics:** Real-time monitoring of tokens per second, VRAM, and RAM utilization.

## 🛠️ Tech Stack
- **Frontend/UI:** [Streamlit](https://streamlit.io/) with custom dark slate styling
- **LLM Core:** Llama 3 / Mistral / Ollama / llama.cpp
- **Vector DB:** SQLite + SQLCipher / ChromaDB (Local)
- **Visualization:** Plotly

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Muhammad08-dot/on-device-private-ai-assistant.git
   cd on-device-private-ai-assistant
   ```

2. **Install dependencies:**
   ```bash
   pip install streamlit pandas plotly
   ```

3. **Run the application:**
   ```bash
   streamlit run streamlit_app.py
   ```

## 📄 License
This project is licensed under the MIT License.
