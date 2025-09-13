import csv
from statistics import multimode

# parse the file to get the data
def load_data(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()[4:] 
    data = []
    for line in lines:
        parts = line.strip().split("\t")
        if len(parts) == 6:
            time, t1, t2, p1, p2, mf = map(float, parts)
            data.append({
                "Time(s)": time,
                "T1(Deg C)": t1,
                "T2(Deg C)": t2,
                "P1(PSI)": p1,
                "P2(PSI)": p2,
                "Mass Flowrate(g/min)": mf
            })
    return data

# calculate the mode and add em to the results dictionary
def mode_for_range(data, tmin, tmax, cols):
    filtered = [row for row in data if tmin <= row["Time(s)"] <= tmax]
    results = {}
    for col in cols:
        values = [row[col] for row in filtered]
        results[col] = multimode(values) 
    return results

# load files
part1method1 = load_data("che260labdataparsing/part1method1.txt")
part1method2 = load_data("che260labdataparsing/part1method2.txt")
part2        = load_data("che260labdataparsing/part2.txt")

# compute
m1_range1 = mode_for_range(part1method1, 250, 350, ["T1(Deg C)", "T2(Deg C)", "P1(PSI)", "P2(PSI)"])
m1_range2 = mode_for_range(part1method1, 600, 700, ["T1(Deg C)", "T2(Deg C)", "P1(PSI)", "P2(PSI)"])
m2_range1 = mode_for_range(part1method2, 100, 200, ["T1(Deg C)", "T2(Deg C)", "P1(PSI)", "P2(PSI)"])
m2_range2 = mode_for_range(part1method2, 1350, 1450, ["T1(Deg C)", "T2(Deg C)", "P1(PSI)", "P2(PSI)"])
p2_range1 = mode_for_range(part2, 0, 20, ["T1(Deg C)", "P1(PSI)"])
p2_range2 = mode_for_range(part2, 140, 180, ["T1(Deg C)", "P1(PSI)"])

# save the modes
results = {
    "Part1 Method1 (250–350s)": m1_range1,
    "Part1 Method1 (600–700s)": m1_range2,
    "Part1 Method2 (100–200s)": m2_range1,
    "Part1 Method2 (1350–1450s)": m2_range2,
    "Part2 (0–20s)": p2_range1,
    "Part2 (140–180s)": p2_range2,
}

with open("che260labdataparsing/mode_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Range", "Column", "Mode Values"])
    for k, v in results.items():
        for col, modes in v.items():
            writer.writerow([k, col, modes])