data_points = [12, 15, 18, 100, 14, 17, 13, 101]
average = sum(data_points) / len(data_points)
outliers = [point for point in data_points if point > 2 * average]

print(f"Average: {average}")
print(f"Outliers: {outliers}")