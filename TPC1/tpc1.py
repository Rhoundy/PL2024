"""This module contains functions related to TPC1."""
import sys

modalities = []
ATHELETES_ABLE = 0
ATHLETES_NOT_ABLE = 0
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
    line_input = line.rstrip()  # rstrip() removes trailing newline characters
    values = line_input.split(',')

    if values[12] == 'true':
        ATHELETES_ABLE += 1
    else:
        ATHLETES_NOT_ABLE += 1

    if values[8] not in modalities:
        modalities.append(values[8])

    for age_group in age_groups:
        # Extract start and end ages from the age group label
        start, end = map(int, age_group[1:-1].split('-'))
        if start <= int(values[5]) <= end:
            age_groups[age_group] += 1
            break

# Calculate the percentages of athletes able and not able
percentage_able = (ATHELETES_ABLE / total_lines) * 100
percentage_not_able = (ATHLETES_NOT_ABLE / total_lines) * 100

modalities.sort()
print(f"Modalities: {modalities}")

print(f"Percentage of athletes able: {percentage_able:.1f}%")
print(f"Percentage of athletes not able: {percentage_not_able:.1f}%")

for age_group, count in age_groups.items():
    print(f"{age_group}: {count} athletes")
