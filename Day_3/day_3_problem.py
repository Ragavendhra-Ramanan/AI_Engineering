data = data = """
Day 1:
- Commit by Alice: "Initial project setup" (3 files, 45 lines)
- Commit by Bob: "Added login page HTML" (1 file, 28 lines)

Day 2:
- Commit by Alice: "Created database connection" (2 files, 67 lines)
- Commit by Charlie: "Added CSS styling for login" (1 file, 52 lines)

Day 3:
- Commit by Bob: "Fixed login button bug" (1 file, 8 lines)
- Commit by Alice: "Added user registration feature" (3 files, 134 lines)

Day 4:
- Commit by Charlie: "Updated navigation menu" (2 files, 43 lines)

Day 5:
- Commit by Bob: "Added password validation" (1 file, 29 lines)
- Commit by Charlie: "Fixed CSS mobile responsiveness" (1 file, 61 lines)
- Commit by Alice: "Created admin dashboard" (4 files, 178 lines)

Day 6:
- Commit by Bob: "Added logout functionality" (2 files, 37 lines)

Day 7:
- Commit by Alice: "Fixed database connection timeout" (1 file, 12 lines)
- Commit by Charlie: "Updated footer design" (1 file, 24 lines)
- Commit by Bob: "Added forgot password feature" (3 files, 89 lines)
"""

import re


def parse_commit_data(data):
    commit_history = {}
    day_blocks = re.split(r"Day \d+:\n", data)
    for day_index, block in enumerate(day_blocks):
        if not block.strip():
            continue
        day = f"Day {day_index}"
        commits = re.findall(
            r'- Commit by (.*?): "(.*?)" \((\d+) files?, (\d+) lines?\)', block
        )
        for author, message, file_count, line_count in commits:
            if author not in commit_history:
                commit_history[author] = []
            commit_history[author].append(
                {
                    "day": day,
                    "message": message,
                    "file_count": int(file_count),
                    "line_count": int(line_count),
                }
            )
    return commit_history


def summarize_commits(commit_history):
    # Total commits made by each developer (Alice, Bob, Charlie)
    summary_author = {}
    for author, commits in commit_history.items():
        total_commits = len(commits)
        total_files = sum(commit["file_count"] for commit in commits)
        total_lines = sum(commit["line_count"] for commit in commits)
        summary_author[author] = {
            "total_commits": total_commits,
            "total_files": total_files,
            "total_lines": total_lines,
        }
    return summary_author


def summarize_days(commit_history):
    # total files modified each_day by all developers
    summary_days = {}
    for author, commits in commit_history.items():
        for commit in commits:
            day = commit["day"]
            if day not in summary_days:
                summary_days[day] = {"total_files": 0, "total_lines": 0}
            summary_days[day]["total_files"] += commit["file_count"]
            summary_days[day]["total_lines"] += commit["line_count"]
    return summary_days


if __name__ == "__main__":
    commit_history = parse_commit_data(data)
    print("Commit History:", commit_history)
    print("Summary by Author:", summarize_commits(commit_history))
    print("Summary by Day:", summarize_days(commit_history))
