import os

source = 'automation_instructions.md'
output = 'automation_instructions.pdf'

with open(source, 'r') as f:
    text = f.read()

# Break text into lines for PDF (escape parentheses)
lines = []
for ln in text.splitlines():
    ln = ln.replace('(', '\\(').replace(')', '\\)')
    lines.append(ln)

# Build content stream with simple text placement
content_lines = []
y = 750
for line in lines:
    if line.strip() == '':
        y -= 16
        continue
    content_lines.append(f'BT /F1 12 Tf 50 {y} Td ({line}) Tj ET')
    y -= 16
content_stream = '\n'.join(content_lines)

objects = []

def add(obj):
    objects.append(obj)
    return len(objects)

add('<< /Type /Catalog /Pages 2 0 R >>')
add('<< /Type /Pages /Kids [3 0 R] /Count 1 >>')
add('<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>')
add(f'<< /Length {len(content_stream)} >>\nstream\n{content_stream}\nendstream')
add('<< /Type /Font /Subtype /Type1 /Name /F1 /BaseFont /Helvetica >>')

pdf = '%PDF-1.7\n'
offsets = [0]
for i,obj in enumerate(objects, start=1):
    offsets.append(len(pdf))
    pdf += f'{i} 0 obj\n{obj}\nendobj\n'

xref_offset = len(pdf)
pdf += 'xref\n0 {}\n'.format(len(objects)+1)
pdf += '0000000000 65535 f \n'
for off in offsets[1:]:
    pdf += f'{off:010d} 00000 n \n'

pdf += 'trailer\n<< /Size {} /Root 1 0 R >>\nstartxref\n{}\n%%EOF'.format(len(objects)+1, xref_offset)

with open(output, 'wb') as f:
    f.write(pdf.encode('latin-1'))

print('Generated', output)
