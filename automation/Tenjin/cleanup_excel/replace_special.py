import pandas as pd

# This will remove any special characters from the "Column1" column.

# Load the Excel file into a Pandas DataFrame
df = pd.read_excel("./input/example.xlsx")

# Remove special characters from Column1
df['NAME'] = df['NAME'].str.replace('[^a-zA-Z0-9 \n\.]', '_')
df['NAME'] = df['NAME'].str.replace('___', '_')
df['NAME'] = df['NAME'].str.replace('__', '_')

# Save the cleaned DataFrame to a new Excel file
df.to_excel("./output/cleaned_example.xlsx", index=False)

print('\nClean up completed successfully! ✨')
