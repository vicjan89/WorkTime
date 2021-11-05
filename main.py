# Import `os`
import os

# Retrieve current working directory (`cwd`)
cwd = os.getcwd()
cwd

# Change directory
os.chdir("/path/to/your/folder")

# List all files and directories in current directory
os.listdir('.')

# Import pandas
import pandas as pd

# Assign spreadsheet filename to `file`
file = 'example.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('Sheet1')