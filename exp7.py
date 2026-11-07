import matplotlib.pyplot as plt

# --------------------------------------------------
# SAMPLE STUDENT DATA
# --------------------------------------------------
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
study_time = [2, 3, 2.5, 4, 6]

student_names = ["Aarav", "Diya", "Rohan", "Meera"]
assignments = [5, 8, 4, 7]

marks = [48, 55, 61, 64, 68, 72, 76, 81, 87, 92]

# --------------------------------------------------
# CREATE THREE SUBPLOTS
# --------------------------------------------------
figure, chart = plt.subplots(1, 3, figsize=(15, 5))

figure.suptitle(
    "Student Academic Performance",
    fontsize=16,
    fontweight="bold"
)

# --------------------------------------------------
# 1. LINE GRAPH
# --------------------------------------------------
chart[0].plot(
    weekdays,
    study_time,
    marker="o",
    markersize=8,
    color="#2563EB",
    linewidth=2.5
)
chart[0].set_title("Daily Study Time", fontsize=12, fontweight="bold")
chart[0].set_xlabel("Day")
chart[0].set_ylabel("Study Hours")
chart[0].grid(True, linestyle="--", alpha=0.5)

# --------------------------------------------------
# 2. BAR GRAPH
# --------------------------------------------------
chart[1].bar(
    student_names,
    assignments,
    color=["#FF6B6B", "#4ECDC4", "#FFD166", "#6C5CE7"],
    edgecolor="black",
    linewidth=0.7
)
chart[1].set_title("Assignments Completed", fontsize=12, fontweight="bold")
chart[1].set_xlabel("Students")
chart[1].set_ylabel("Number of Assignments")

# Display values on bars
for i, value in enumerate(assignments):
    chart[1].text(
        i,
        value + 0.2,
        str(value),
        ha="center",
        fontweight="bold"
    )

# --------------------------------------------------
# 3. HISTOGRAM
# --------------------------------------------------
chart[2].hist(
    marks,
    bins=[40, 50, 60, 70, 80, 90, 100],
    color="#8E44AD",
    edgecolor="white",
    linewidth=1.5
)
chart[2].set_title("Exam Score Distribution", fontsize=12, fontweight="bold")
chart[2].set_xlabel("Marks")
chart[2].set_ylabel("Number of Students")
chart[2].grid(axis="y", linestyle="--", alpha=0.4)

# --------------------------------------------------
# FINAL FORMATTING
# --------------------------------------------------
plt.tight_layout()
plt.show()
