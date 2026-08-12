import streamlit as st
import time
import pandas as pd
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="On-Device Private AI Assistant",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
    .stApp { background-color: #0b0f19; color: #e2e8f0; }
    h1, h2, h3 { color: #38bdf8; font-family: 'Inter', sans-serif; }
    
    .privacy-badge {
        background-color: #064e3b;
        color: #34d399;
        border: 1px solid #059669;
        padding: 6px 12px;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 15px;
    }
    
    .resource-card {
        background-color: #1e293b;
        border-radius: 8px;
        border: 1px solid #334155;
        padding: 15px;
        text-align: center;
    }
    
    .doc-box {
        background-color: #0f172a;
        border-left: 4px solid #38bdf8;
        padding: 12px;
        margin-top: 10px;
        border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/shield.png", width=60)
    st.title("🔒 Private AI Vault")
    st.markdown("---")
    
    st.subheader("Model Configuration")
    model = st.selectbox("Local LLM Core", ["Llama-3-8B-Instruct (Local)", "Mistral-7B-v0.3 (Local)", "Phi-3-Mini-4K (Local)"])
    quant = st.selectbox("Quantization Level", ["Q4_K_M (4-bit)", "Q5_K_M (5-bit)", "Q8_0 (8-bit)"])
    vector_db = st.selectbox("Vector Database", ["SQLite + SQLCipher", "ChromaDB (Encrypted)", "Local FAISS"])
    
    st.markdown("---")
    st.subheader("Security Controls")
    st.toggle("Air-Gap Network Isolation", value=True)
    st.toggle("Memory Encryption", value=True)
    st.toggle("Zero Telemetry", value=True)

# --- MAIN APP ---
st.title("🔒 On-Device Private AI Assistant")
st.markdown('<div class="privacy-badge">🛡️ Air-Gapped Environment: 100% Offline & Local</div>', unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3 = st.tabs(["💬 Private Chat", "📁 Document RAG Vault", "📊 Hardware & Security Diagnostics"])

with tab1:
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.subheader("Local LLM Chat Session")
        
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {"role": "assistant", "content": "Welcome to your local AI sandbox. No data leaves your machine. Ask anything about your uploaded documents or private code."}
            ]
            
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])
                
        if prompt := st.chat_input("Enter prompt for local inference..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.write(prompt)
                
            with st.chat_message("assistant"):
                with st.spinner(f"Running inference locally via {model}..."):
                    time.sleep(1.2)
                    res = f"**[Local Response - Zero Cloud Leak]**\n\nAnalyzed query: '{prompt}'.\nAll calculations processed on local NPU/GPU using {model} ({quant}). Privacy status verified."
                    st.write(res)
                    st.session_state.messages.append({"role": "assistant", "content": res})

    with col2:
        st.subheader("Vault Status")
        st.metric("Encrypted Vectors", "12,450", delta="+150 new")
        st.metric("Local DB Size", "42.8 MB")
        st.metric("Tokens/Sec", "48.2 t/s")
        
        st.markdown("<div class='doc-box'><b>Active Context:</b><br>📄 Q3_Financials_Confidential.pdf<br>📄 Employee_Passwords_Policy.docx</div>", unsafe_allow_html=True)

with tab2:
    st.subheader("Local Document Ingestion (Offline RAG)")
    uploaded_files = st.file_uploader("Drop sensitive files to encrypt & vectorize locally", accept_multiple_files=True, type=["pdf", "txt", "docx", "py"])
    
    if uploaded_files:
        if st.button("🔒 Encrypt & Index Documents"):
            with st.spinner("Chunking & Embedding locally with ONNX MiniLM..."):
                time.sleep(1.5)
            st.success(f"Successfully processed {len(uploaded_files)} files into local encrypted vector store!")

with tab3:
    st.subheader("System Hardware & Telemetry Monitor")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("CPU Utilization", "32%", delta="-4%")
    with c2:
        st.metric("VRAM Used", "4.8 GB / 12 GB")
    with c3:
        st.metric("Outbound Traffic", "0 KB/s (Blocked)")
        
    df_usage = pd.DataFrame({
        "Time": ["00:00", "00:05", "00:10", "00:15", "00:20"],
        "VRAM_GB": [4.1, 4.2, 4.8, 4.6, 4.8],
        "System_RAM_GB": [8.2, 8.4, 9.1, 8.8, 9.0]
    })
    
    fig = px.line(df_usage, x="Time", y=["VRAM_GB", "System_RAM_GB"], title="Local Hardware Resource Allocation", color_discrete_sequence=["#38bdf8", "#34d399"])
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="white")
    st.plotly_chart(fig, use_container_width=True)
