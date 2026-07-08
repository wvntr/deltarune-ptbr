import json
from pathlib import Path

root = Path(r'C:\Users\w1ntry\Documents\GitHub\deltarune-traduzido-ptbr')
original_path = root / 'original' / 'cap5' / 'chapter5_strings.json'
translation_path = root / 'traduçao' / 'cap5' / 'strings.json'
report_path = root / 'cap5_strings_alignment_report.txt'


def extract_string_literals(text: str):
    values = []
    i = 0
    n = len(text)
    in_string = False
    escaped = False
    in_line_comment = False
    in_block_comment = False
    depth = 0

    while i < n:
        ch = text[i]
        nxt = text[i + 1] if i + 1 < n else ''

        if in_line_comment:
            if ch == '\n':
                in_line_comment = False
            i += 1
            continue

        if in_block_comment:
            if ch == '*' and nxt == '/':
                in_block_comment = False
                i += 2
                continue
            i += 1
            continue

        if in_string:
            if escaped:
                escaped = False
            elif ch == '\\':
                escaped = True
            elif ch == '"':
                in_string = False
                literal = text[start:i + 1]
                values.append(json.loads(literal))
            i += 1
            continue

        if ch == '/' and nxt == '/':
            in_line_comment = True
            i += 2
            continue

        if ch == '/' and nxt == '*':
            in_block_comment = True
            i += 2
            continue

        if ch == '"':
            in_string = True
            start = i
            escaped = False
            i += 1
            continue

        if ch == '[':
            depth += 1
        elif ch == ']':
            depth -= 1
            if depth < 0:
                break
        i += 1

    return values


def parse_strings_array(path: Path):
    text = path.read_text(encoding='utf-8')
    # Find the first array after the "Strings" property.
    prop_pos = text.find('"Strings"')
    if prop_pos == -1:
        raise ValueError(f'Could not find "Strings" property in {path}')
    array_start = text.find('[', prop_pos)
    if array_start == -1:
        raise ValueError(f'Could not find array start in {path}')
    array_text = text[array_start:]
    literals = extract_string_literals(array_text)
    return literals


orig_entries = parse_strings_array(original_path)
tr_entries = parse_strings_array(translation_path)

print(f'Original entries: {len(orig_entries)}')
print(f'Translation entries: {len(tr_entries)}')

# Preserve the current translation order and normalize to the original length.
aligned_entries = list(tr_entries)
if len(aligned_entries) < len(orig_entries):
    aligned_entries.extend(orig_entries[len(aligned_entries):])
elif len(aligned_entries) > len(orig_entries):
    aligned_entries = aligned_entries[:len(orig_entries)]

result = {'Strings': aligned_entries}
translation_path.write_text(json.dumps(result, ensure_ascii=False, indent=4) + '\n', encoding='utf-8')

report_lines = []
report_lines.append('Capítulo 5 — alinhamento de strings')
report_lines.append(f'Original entries: {len(orig_entries)}')
report_lines.append(f'Translation entries after normalization: {len(aligned_entries)}')
report_lines.append('')
report_lines.append('Posições onde o conteúdo diverge da versão original (não são necessariamente problemas de ordem):')
for idx, (orig_value, tr_value) in enumerate(zip(orig_entries, aligned_entries), 1):
    if orig_value != tr_value:
        report_lines.append(f'[{idx}] original={orig_value!r} | traduzido={tr_value!r}')
        if len(report_lines) >= 15:
            break
if len(report_lines) == 6:
    report_lines.append('Nenhum desvio identificado nos primeiros pontos verificados.')
report_path.write_text('\n'.join(report_lines) + '\n', encoding='utf-8')

print(f'Wrote normalized translation file to {translation_path}')
print(f'Wrote report to {report_path}')
print('Verification:')
print(f'  normalized length = {len(aligned_entries)}')
print(f'  original length = {len(orig_entries)}')
