# Incident_Reconstruction_AI
Investigators struggle to piece together events from fragmented reports. Build a GenAI system that takes multiple inputs (statements, logs, notes) and generates a coherent, time-ordered incident narrative.

This project builds a Generative AI system that:

1. Accepts multiple input sources (text files, logs, notes, statements, images)
2. Merges context intelligently
3. Generates a coherent, time-ordered incident narrative

   
<h2>🚀 Features</h2>
📂 Upload multiple input files (logs, notes, statements)
🖼️ Extract text from images (OCR support)
🧠 Context merging using Large Language Models (LLMs)
🕒 Automatic timeline generation
📝 Narrative generation (human-readable report)
📊 Timeline visualization (chart + table)
📥 Download final incident report
🌐 Supports both local (Ollama) and cloud (Hugging Face) models

#🏗️ Tech Stack

1. Frontend/UI: Streamlit
2. LLM Integration: Ollama (local)
3. Language: Python
4. Libraries:
     i. streamlit
     ii. requests
     iii. pandas
     iv. Altair
     v. Pillow

#📁 Project Structure
incident_reconstruction/
│── app.py              # Streamlit UI
│── processor.py        # Pipeline logic
│── prompts.py          # LLM prompts
│── llm.py              # LLM API integration
│── data/               # Sample inputs
│── requirements.txt

#⚙️ Setup Instructions (Local)
1. Clone Repository
git clone <https://github.com/vanshkapooor/Incident_Reconstruction_AI.git>

2. Install Dependencies
pip install -r requirements.txt

3. Run Application
streamlit run app.py

Open in browser:

http://localhost:8501

🔄 How It Works
User uploads input files (logs, statements, notes, images)
All inputs are merged into a unified context
LLM processes the data:
    1. Extracts events
    2. Builds timeline
    3. Generates narrative
Results are displayed and visualized

#📊 Example Use Cases
Cybersecurity incident analysis
IT system failure investigation
Fraud detection reports
Operational incident tracking

#⚠️ Limitations
Free LLM APIs may be slow or rate-limited
Smaller models may produce less accurate timelines
OCR may struggle with low-quality images
Large inputs can slow down processing

#🔥 Future Improvements
Multi-agent architecture
Better timeline visualization (interactive graphs)
Confidence scoring for events
Real-time log streaming
Integration with vector databases (RAG)

#🧠 Key Learning Outcomes
Working with Large Language Models (LLMs)
Context merging & prompt engineering
Building end-to-end GenAI applications
Streamlit UI development
Handling multi-modal inputs (text + images)

#👨‍💻 Author

Vansh Kapoor
