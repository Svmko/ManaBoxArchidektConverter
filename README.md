# ManaBoxArchidektConverter
 Simple script to convert your exported ManaBox csv to a format that Archidekt accepts.

## Usage

```bash
python ManaBoxArchidektConverter.py <input_file> <output_file>
```
After converting, you may copy the contents of the output file and paste it into the "Text import" section of Deck sandbox in Archidekt.

## Example

```bash
python ManaBoxArchidektConverter.py ManaBox.csv Archidekt.txt
```
Make sure this script is in the same directory as your ManaBox.csv file. Otherwise, you will need to provide the full path to the file.
