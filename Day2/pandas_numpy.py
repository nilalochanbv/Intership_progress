import numpy as np

marks = np.array([85, 92, 78, 95, 88])

print("Marks:", marks)
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))



import pandas as pd

data = {
    "Name": ["Arun", "Bala", "Chitra", "Deepak", "Esha"],
    "Marks": [85, 92, 78, 95, 88]
}

df = pd.DataFrame(data)

print("\nStudent Data:")
print(df)

print("\nAverage Marks:", df["Marks"].mean())
print("\nTopper:")
print(df.loc[df["Marks"].idxmax()])