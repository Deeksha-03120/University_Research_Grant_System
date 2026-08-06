import json

# -----------------------------
# Faculty Data
# -----------------------------
faculty = [
    {
        "Faculty ID": 101,
        "Faculty Name": "Arun",
        "Department": "CSE",
        "Publications": 30,
        "H_index": 18,
        "Budget": 150000,
        "Collaboration": 20
    },
    {
        "Faculty ID": 102,
        "Faculty Name": "Meena",
        "Department": "ECE",
        "Publications": 22,
        "H_index": 15,
        "Budget": 95000,
        "Collaboration": 18
    },
    {
        "Faculty ID": 103,
        "Faculty Name": "Karthik",
        "Department": "IT",
        "Publications": 35,
        "H_index": 21,
        "Budget": 120000,
        "Collaboration": 22
    },
    {
        "Faculty ID": 104,
        "Faculty Name": "Priya",
        "Department": "CSE",
        "Publications": 18,
        "H_index": 12,
        "Budget": 80000,
        "Collaboration": 15
    }
]

# ---------------------------------
# Validate Budget
# ---------------------------------

for person in faculty:
    if person["Budget"] < 0:
        raise ValueError("Invalid Budget")

# ---------------------------------
# Calculate Research Score
# ---------------------------------

for person in faculty:
    score = (
        0.4 * person["Publications"]
        + 0.3 * person["H_index"]
        + 0.3 * person["Collaboration"]
    )

    person["Research Score"] = round(score, 2)

# ---------------------------------
# Allocate Grant
# ---------------------------------

for person in faculty:

    if person["Research Score"] >= 25:
        person["Grant"] = person["Budget"]

    elif person["Research Score"] >= 20:
        person["Grant"] = person["Budget"] * 0.75

    else:
        person["Grant"] = person["Budget"] * 0.50

# ---------------------------------
# Faculty receiving above $100000
# ---------------------------------

print("\nFaculty Receiving Grant Above $100000\n")

for person in faculty:
    if person["Grant"] > 100000:
        print(person["Faculty Name"], "->", person["Grant"])

# ---------------------------------
# Department with Maximum Funding
# ---------------------------------

dept = {}

for person in faculty:
    d = person["Department"]

    dept[d] = dept.get(d, 0) + person["Grant"]

max_dept = max(dept, key=dept.get)

print("\nDepartment with Maximum Funding")
print(max_dept, "=", dept[max_dept])

# ---------------------------------
# Rank Faculty
# ---------------------------------

ranking = sorted(
    faculty,
    key=lambda x: x["Research Score"],
    reverse=True
)

print("\nFaculty Ranking")

for i, person in enumerate(ranking, start=1):
    print(i, person["Faculty Name"], person["Research Score"])

# ---------------------------------
# Average Research Score
# ---------------------------------

average = sum(
    p["Research Score"] for p in faculty
) / len(faculty)

print("\nAverage Research Score =", round(average,2))

# ---------------------------------
# Top Performer
# ---------------------------------

top = ranking[0]

print("\nTop Performer")
print(top["Faculty Name"])

# ---------------------------------
# Save Ranking
# ---------------------------------

with open("ranking.json", "w") as file:
    json.dump(ranking, file, indent=4)

print("\nRanking Saved")

# ---------------------------------
# Read Ranking
# ---------------------------------

print("\nReading Ranking File\n")

with open("ranking.json", "r") as file:
    data = json.load(file)

for person in data:
    print(person["Faculty Name"], person["Research Score"])
