import pandas as pd
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Convert ManaBox CSV to Archidekt format')
parser.add_argument('input_file', help='Input CSV file from ManaBox')
parser.add_argument('output_file', help='Output text file name (MUST be a .txt file)')

args = parser.parse_args()

print("Reading input file...")

# Use the provided input
df = pd.read_csv(args.input_file)

# Drop columns that are not needed for import
df = df.drop(columns=['Binder Name', 'Binder Type', 'Set name', 'Foil', 'Rarity', 'ManaBox ID', 'Scryfall ID', 'Purchase price', 'Misprint', 'Altered', 'Condition', 'Language', 'Purchase price currency'])

# Match the set code format
df['Set code'] = '(' + df['Set code'] + ')'

# Shift the quantity column to the front
quantityShift = df.columns.tolist()
quantityShift.remove('Quantity')
quantityShift = ['Quantity'] + quantityShift
df = df[quantityShift]

# Save with special delimiter
df.to_csv(args.output_file, sep='|', index=False, header=False, quoting=None)

# Read and replace delimiter with spaces
with open(args.output_file, 'r') as file:
    content = file.read()
    
with open(args.output_file, 'w') as file:
    file.write(content.replace('|', ' '))

print(f"\nConversion complete.")
print("Please check the output file for any errors.")
print("If there are any errors, please check the input file for any issues. It should be untouched from ManaBox.")
print("Now copy and paste the contents of the output file into Archidekt!")
