import sys

modalities = []
athletes_able = 0
athletes_not_able = 0
age_groups = {}

# Loop through the age groups with a 5-year interval
for start_age in range(20, 40, 5):
    end_age = start_age + 4
    age_groups[f'[{start_age}-{end_age}]'] = 0

#skip 1st line
sys.stdin.readline()

# Read all lines from stdin into a list
lines = sys.stdin.readlines()
total_lines = len(lines)

for line in lines:
    input = line.rstrip()  # rstrip() removes trailing newline characters
    values = input.split(',')

    if values[12] == 'true':
        athletes_able += 1
    else:
        athletes_not_able += 1

    if values[8] not in modalities:
        modalities.append(values[8])

    for age_group in age_groups:
        # Extract start and end ages from the age group label
        start, end = map(int, age_group[1:-1].split('-'))
        if start <= int(values[5]) <= end:
            age_groups[age_group] += 1
            break

# Calculate the percentages of athletes able and not able
percentage_able = (athletes_able / total_lines) * 100
percentage_not_able = (athletes_not_able / total_lines) * 100

modalities.sort()
print(f"Modalities: {modalities}")

print(f"Percentage of athletes able: {percentage_able:.1f}%")
print(f"Percentage of athletes not able: {percentage_not_able:.1f}%")

for age_group, count in age_groups.items():
    print(f"{age_group}: {count} athletes")