import numpy as np

# Create an array with student marks
marks = np.array([78, 85, 90, 67, 92, 75, 88, 80, 95, 70])

# Calculate statistical values
mean_marks = np.mean(marks)
median_marks = np.median(marks)
max_marks = np.max(marks)
min_marks = np.min(marks)
std_marks = np.std(marks)

# Display the results
print("Student Marks Analysis")
print("----------------------")
print("Student Marks:", marks)
print("Mean Marks:", mean_marks)
print("Median Marks:", median_marks)
print("Maximum Marks:", max_marks)
print("Minimum Marks:", min_marks)
print("Standard Deviation:", round(std_marks, 2))

# Display a short analysis
print("\nResult Analysis")
print("----------------------")
print(f"The average marks are {mean_marks}.")
print(f"The median marks are {median_marks}.")
print(f"The highest mark is {max_marks}.")
print(f"The lowest mark is {min_marks}.")
print(f"The standard deviation is {std_marks:.2f}.")
