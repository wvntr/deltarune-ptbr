import json
import re
from collections import defaultdict, deque
from pathlib import Path

root = Path(r'C:\Users\w1ntry\Documents\GitHub\deltarune-traduzido-ptbr')
orig = root/'original'/'cap5'/'chapter5_strings.json'
tr = root/'traduçao'/'cap5'/'strings.json'


def extract_array_entries(text: str):
    start = text.find('[')
    end = text.rfind(']')
    if start == -1 or end == -1 or end < start:
        raise ValueError('Could not find JSON array')
    arr_text = text[start:end+1]
    matches = list(re.finditer(r'"(?:\\.|[^"\\])*"', arr_text))
    entries = []
    line_numbers = []
    for m in matches:
        # skip the opening/closing bracket tokens and any non-entry strings; we only want entries in the array itself
        value = json.loads(m.group(0))
        line = arr_text.count('\n', 0, m.start()) + 1
        entries.append(value)
        line_numbers.append(line)
    return entries, line_numbers


orig_text = orig.read_text(encoding='utf-8')
tr_text = tr.read_text(encoding='utf-8')

orig_arr, orig_lines = extract_array_entries(orig_text)
tr_arr, tr_lines = extract_array_entries(tr_text)

print('original entries', len(orig_arr))
print('translated entries', len(tr_arr))
print('same length?', len(orig_arr) == len(tr_arr))

# Report the first mismatches before reordering.
print('\nFirst mismatches before reordering:')
for i, (a, b) in enumerate(zip(orig_arr, tr_arr), 1):
    if a != b:
        print(f'  index {i}: original="{a}" | translated="{b}"')
        print(f'    original line {orig_lines[i-1]} | translated line {tr_lines[i-1]}')
        break
else:
    print('  none')

# Build a mapping from string value to the positions where it appears in the translated array.
positions = defaultdict(deque)
for idx, value in enumerate(tr_arr):
    positions[value].append(idx)

# Reorder translated array to match the original order.
reordered = []
for value in orig_arr:
    if value not in positions or not positions[value]:
        raise ValueError(f'Missing value in translated array: {value!r}')
    reordered.append(tr_arr[positions[value].popleft()])

# Write the reordered array back into the translation file while preserving the top-level structure.
# We only replace the array portion between the first [ and the last ].
new_text = tr_text
start = new_text.find('[')
end = new_text.rfind(']')
if start == -1 or end == -1 or end < start:
    raise ValueError('Could not find array in translation file')

array_text = json.dumps(reordered, ensure_ascii=False, indent=4)
# Put the array content on its own lines with 4-space indentation inside the existing file.
new_text = new_text[:start] + array_text + new_text[end+1:]
tr.write_text(new_text, encoding='utf-8')

print('\nReordered translation file written successfully.')

# Report a few line shifts after reordering (using the original positions).
print('\nRepresentative line shifts:')
for i, value in enumerate(orig_arr):
    if i >= 20:
        break
    # Find the line number of this value in the original file and the translated file before/after.
    # For the translated file we now use the same order as the original, so the current line is the same index.
    print(f'  index {i+1}: {value!r} | original line {orig_lines[i]} | translated line {tr_lines[i]}')
