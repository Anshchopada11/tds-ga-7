# employee_visualization.py
# Email: 24f1001822@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample employee dataset
data = """
employee_id,department,region,performance_score,years_experience,satisfaction_rating
EMP001,Marketing,Middle East,61.09,1,4.4
EMP002,Marketing,Latin America,67.43,5,3.6
EMP003,HR,Europe,86.21,9,4.4
EMP004,IT,Latin America,87.94,12,3.5
EMP005,Sales,Middle East,70.49,15,4.9
EMP006,Finance,Europe,76.21,7,4.3
EMP007,Finance,Asia,84.11,8,4.1
EMP008,Finance,North America,73.12,10,4.0
EMP009,IT,Europe,68.75,6,3.8
EMP010,Sales,Asia,71.23,4,4.5
"""

# Load dataset into a DataFrame
from io import StringIO
df = pd.read_csv(StringIO(data))

# Calculate frequency count for Finance department
finance_count = df[df['department'] == 'Finance'].shape[0]
print(f"Frequency count for Finance department: {finance_count}")

# Create histogram for department distribution
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='department', palette='Set2')
plt.title("Employee Count by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.xticks(rotation=45)
plt.tight_layout()

# Save as HTML file using mpld3 for interactivity
import mpld3
html_str = mpld3.fig_to_html(plt.gcf())
with open("employee_department_distribution.html", "w") as f:
    f.write(html_str)
