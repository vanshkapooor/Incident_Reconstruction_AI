import streamlit as st
from processor import reconstruct_incident

st.set_page_config(page_title="Incident Reconstruction AI", layout="wide")

st.title("🕵️ Incident Narrative Reconstruction AI")
st.markdown("---")
st.info("Upload incident data files (logs, statements, notes) to reconstruct the event timeline.")

# --- FILE UPLOAD SECTION ---
st.header("📂 Upload Files")

uploaded_logs = st.file_uploader("📜 Upload Logs File", type=["txt"], accept_multiple_files=True)
uploaded_notes = st.file_uploader("📝 Upload Notes File", type=["txt"], accept_multiple_files=True)
uploaded_statements = st.file_uploader("🗣 Upload Statements File", type=["txt"], accept_multiple_files=True)


# --- FILE READER FUNCTION ---
def read_files(files):
    content = ""
    if files:
        for file in files:
            content += file.read().decode("utf-8") + "\n\n"
    return content


logs = read_files(uploaded_logs)
notes = read_files(uploaded_notes)
statements = read_files(uploaded_statements)

# --- OPTIONAL PREVIEW ---
with st.expander("👀 Preview Uploaded Data"):
    st.subheader("Logs")
    st.write(logs if logs else "No logs uploaded")
    
    st.subheader("Notes")
    st.write(notes if notes else "No notes uploaded")

    st.subheader("Statements")
    st.write(statements if statements else "No statements uploaded")


# --- PROCESS BUTTON ---
if st.button("🚀 Reconstruct Incident"):

    if not logs and not statements and not notes:
        st.warning("Please upload at least one file.")
    else:
        inputs = [logs, notes, statements]

        with st.spinner("Processing with AI..."):
            result = reconstruct_incident(inputs)

        st.success("✅ Reconstruction Complete!")

        # --- OUTPUT ---
        st.header("📊 Results")

        with st.expander("🔄 Merged Events"):
            st.write(result["merged_events"])

        with st.expander("🕒 Timeline"):
            st.write(result["timeline"])

        with st.expander("📝 Final Narrative"):
            st.write(result["narrative"])

        # --- DOWNLOAD BUTTON ---
        st.download_button(
            "📥 Download Final Report",
            result["narrative"],
            file_name="incident_report.txt"
        )