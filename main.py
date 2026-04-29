from processor import reconstruct_incident

def load_file(path):
    with open(path, "r") as f:
        return f.read()

if __name__ == "__main__":
    inputs = [
        load_file("data/logs.txt"),
        load_file("data/statements.txt"),
        load_file("data/notes.txt")
    ]

    result = reconstruct_incident(inputs)

    print("\n===== MERGED EVENTS =====\n")
    print(result["merged_events"])

    print("\n===== TIMELINE =====\n")
    print(result["timeline"])

    print("\n===== FINAL NARRATIVE =====\n")
    print(result["narrative"])