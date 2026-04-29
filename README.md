# Incident_Reconstruction_AI
Investigators struggle to piece together events from fragmented reports. Build a GenAI system that takes multiple inputs (statements, logs, notes) and generates a coherent, time-ordered incident narrative.

This project builds a Generative AI system that:

1. Accepts multiple input sources (text files, logs, notes, statements)
2. Merges context intelligently
3. Generates a coherent, time-ordered incident narrative

   
<h2>🚀 Features</h2>
📂 Upload multiple input files (logs, notes, statements)<br>
🧠 Context merging using Large Language Models (LLMs)<br>
🕒 Automatic timeline generation<br>
📝 Narrative generation (human-readable report)<br>
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
│── app.py      <br>       
│── processor.py   <br>     
│── prompts.py   <br>       
│── llm.py     <br>         
│── data/       <br>        
│── requirements.txt<br>

<h2>⚙️ Setup Instructions (Local)</h2>
1. Install Ollama<br>
2. Once Ollama is installed, pull the Phi3 model from Ollama<br>
3. Change directory to incident_reconstruction<br>
4. Run Application:<br>

   streamlit run app.py

Open in browser:

http://localhost:8501

<h2>🔄 How It Works</h2>
User uploads input files (logs, statements, notes)<br>
All inputs are merged into a unified context<br>
LLM processes the data:<br>

   1. Extracts events<br>
   2. Builds timeline<br>
   3. Generates narrative<br>

<h2>📊 Example Use Cases</h2>
Cybersecurity incident analysis<br>
IT system failure investigation<br>
Fraud detection reports<br>
Operational incident tracking<br>

<h2>⚠️ Limitations</h2>
Free LLM APIs may be slow or rate-limited<br>
Smaller models may produce less accurate timelines<br>
OCR may struggle with low-quality images<br>
Large inputs can slow down processing<br>

<h2>🔥 Future Improvements</h2>
Multi-agent architecture<br>
Better timeline visualization (interactive graphs)<br>
Confidence scoring for events<br>
Real-time log streaming<br>
Integration with vector databases (RAG)<br>

<h2>🧠 Key Learning Outcomes</h2>
Working with Large Language Models (LLMs)<br>
Context merging & prompt engineering<br>
Building end-to-end GenAI applications<br>
Streamlit UI development<br>
Handling multi-modal inputs (text + images)<br>
