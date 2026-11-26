# reader.py — Nancy (issue #2) · checked by Audrey
# Reads a constraint table (.txt) into memory and displays it.
#
# Functions to write — shared names, do not rename them (README, section 4):
#   read_table(path)                  -> tasks, n
#   display_constraint_table(tasks)   -> prints the table

def read_table(path):
    """Read a constraint table from a .txt file and return tasks, n."""
    tasks = {}
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            task_number = int(parts[0])
            duration = int(parts[1])
            preds = [int(p) for p in parts[2:]]
            tasks[task_number] = {"duration": duration, "preds": preds}
    n = len(tasks)
    return tasks, n


def display_constraint_table(tasks):
    """Print the constraint table from memory."""
    print(f"{'Task':<8}{'Duration':<12}{'Predecessors'}")
    print("-" * 35)
    for task in sorted(tasks):
        duration = tasks[task]["duration"]
        preds = tasks[task]["preds"]
        preds_str = ", ".join(str(p) for p in preds) if preds else "—"
        print(f"{task:<8}{duration:<12}{preds_str}")