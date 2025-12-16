import matplotlib.pyplot as plt
import numpy as np

years = np.array([1, 3, 5, 7, 10, 12, 15, 18, 20, 25])
salary = np.array([45, 55, 65, 75, 90, 100, 115, 130, 150, 180])

# Define clusters
junior_mask = years <= 10
senior_mask = (years > 10) & (salary <= 150)
outlier_mask = salary > 150

# Plot clusters
plt.scatter(years[junior_mask], salary[junior_mask],
            s=70, color='skyblue', alpha=0.8, label='Junior (≤10 yrs)')
plt.scatter(years[senior_mask], salary[senior_mask],
            s=70, color='olive', alpha=0.8, label='Senior (11–15 yrs)')
# Highlight outliers
plt.scatter(years[outlier_mask], salary[outlier_mask],
            s=120, color='crimson', alpha=1.0, label='Outliers')

plt.title("Experience vs. Salary with Clusters & Outliers")
plt.xlabel("Years of Experience")
plt.ylabel("Annual Salary (in $1,000s)")
plt.grid(True)
plt.legend()
plt.show()