# Incident_Reconstruction_AI
Investigators struggle to piece together events from fragmented reports. Build a GenAI system that takes multiple inputs (statements, logs, notes) and generates a coherent, time-ordered incident narrative.

This project builds a Generative AI system that:

1. Accepts multiple input sources (text files, logs, notes, statements, images)
2. Merges context intelligently
3. Generates a coherent, time-ordered incident narrative

   
<h2>🚀 Features</h2>
📂 Upload multiple input files (logs, notes, statements)<br>
🖼️ Extract text from images (OCR support)<br>
🧠 Context merging using Large Language Models (LLMs)<br>
🕒 Automatic timeline generation<br>
📝 Narrative generation (human-readable report)<br>
📊 Timeline visualization (chart + table)<br>
📥 Download final incident report<br>
🌐 Supports local (Ollama)<br>

<h2>🏗️ Tech Stack</h2>

1. Frontend/UI: Streamlit<br>
2. LLM Integration: Ollama (local)<br>
3. Language: Python<br>
4. Libraries:<br>
     i. streamlit<br>
     ii. requests<br>
     iii. pandas<br>
     iv. Altair<br>
     v. Pillow<br>

<h2>📁 Project Structure</h2>
incident_reconstruction/<br>
│── app.py              # Streamlit UI<br>
│── processor.py        # Pipeline logic<br>
│── prompts.py          # LLM prompts<br>
│── llm.py              # LLM API integration<br>
│── data/               # Sample inputs<br>
│── requirements.txt<br>

<h2>⚙️ Setup Instructions (Local)</h2>
1. Clone Repository
git clone <https://github.com/vanshkapooor/Incident_Reconstruction_AI.git>

2. Install Dependencies
pip install -r requirements.txt

3. Run Application
streamlit run app.py

Open in browser:

http://localhost:8501

<h2>🔄 How It Works</h2>
User uploads input files (logs, statements, notes, images)
All inputs are merged into a unified context
LLM processes the data:
    1. Extracts events
    2. Builds timeline
    3. Generates narrative
Results are displayed and visualized

<h2>📊 Example Use Cases</h2>
Cybersecurity incident analysis
IT system failure investigation
Fraud detection reports
Operational incident tracking

<h2>⚠️ Limitations</h2>
Free LLM APIs may be slow or rate-limited
Smaller models may produce less accurate timelines
OCR may struggle with low-quality images
Large inputs can slow down processing

<h2>🔥 Future Improvements</h2>
Multi-agent architecture
Better timeline visualization (interactive graphs)
Confidence scoring for events
Real-time log streaming
Integration with vector databases (RAG)

<h2>🧠 Key Learning Outcomes</h2>
Working with Large Language Models (LLMs)
Context merging & prompt engineering
Building end-to-end GenAI applications
Streamlit UI development
Handling multi-modal inputs (text + images)

<h2>👨‍💻 Author</h2>

Vansh Kapoor
