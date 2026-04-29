MERGE_PROMPT = """
You are given fragmented incident data from multiple sources.

Merge them into structured events.

Input:
{input_data}

Output format:
- Timestamp (if available)
- Event description
- Source
"""

TIMELINE_PROMPT = """
Convert the following merged events into a strictly time-ordered timeline.

Events:
{events}

Rules:
- Sort chronologically
- Infer missing timestamps if possible
- Keep logical consistency
"""

NARRATIVE_PROMPT = """
You are an incident reconstruction AI.

Using the timeline below, generate a clear and professional narrative.

Timeline:
{timeline}

Requirements:
- Chronological story
- Mention uncertainties
- No unnecessary assumptions
"""