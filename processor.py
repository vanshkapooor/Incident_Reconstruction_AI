from llm import call_llm
from prompts import MERGE_PROMPT, TIMELINE_PROMPT, NARRATIVE_PROMPT

def merge_context(inputs):
    combined = "\n\n".join(inputs)
    prompt = MERGE_PROMPT.format(input_data=combined)
    return call_llm(prompt)

def build_timeline(merged_events):
    prompt = TIMELINE_PROMPT.format(events=merged_events)
    return call_llm(prompt)

def generate_narrative(timeline):
    prompt = NARRATIVE_PROMPT.format(timeline=timeline)
    return call_llm(prompt)

def reconstruct_incident(inputs):
    print("🔄 Merging context...")
    merged = merge_context(inputs)

    print("🕒 Building timeline...")
    timeline = build_timeline(merged)

    print("📝 Generating narrative...")
    narrative = generate_narrative(timeline)

    return {
        "merged_events": merged,
        "timeline": timeline,
        "narrative": narrative
    }