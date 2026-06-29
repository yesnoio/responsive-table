#!/usr/bin/env python3
"""
transform-tables.py — pre-process responsive tables at build/commit time.

Reads an HTML file, finds every <table>, adds class="responsive" if absent,
and injects <span class="label"> / <span class="data"> wrappers into each <td>
so the responsive CSS works without any client-side JavaScript.

Idempotent: cells that already have a .label child are left untouched.

Usage:
  python3 transform-tables.py page.html            # modifies file in place
  python3 transform-tables.py page.html out.html   # writes to a new file

Requires: pip install beautifulsoup4
"""
import sys
from bs4 import BeautifulSoup


def transform_tables(html: str) -> tuple[str, int]:
    soup = BeautifulSoup(html, 'html.parser')
    changed = 0

    for table in soup.find_all('table'):
        header_row = table.select_one('thead tr')
        if not header_row:
            continue

        # Ensure the table carries the responsive class
        classes = table.get('class', [])
        if 'responsive' not in classes:
            table['class'] = classes + ['responsive']

        headers = [th.get_text(strip=True) for th in header_row.find_all('th')]
        if not headers:
            continue

        tbody = table.find('tbody')
        if not tbody:
            continue

        for row in tbody.find_all('tr'):
            for i, td in enumerate(row.find_all('td')):
                if td.find(class_='label'):
                    continue  # already transformed

                label = soup.new_tag('span')
                label['class'] = 'label'
                label.string = headers[i] if i < len(headers) else ''

                data = soup.new_tag('span')
                data['class'] = 'data'
                for child in list(td.children):
                    data.append(child.extract())

                td.append(label)
                td.append(data)
                changed += 1

    return str(soup), changed


def main():
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} input.html [output.html]', file=sys.stderr)
        sys.exit(1)

    src = sys.argv[1]
    dst = sys.argv[2] if len(sys.argv) > 2 else src

    with open(src, encoding='utf-8') as f:
        html = f.read()

    result, changed = transform_tables(html)

    with open(dst, 'w', encoding='utf-8') as f:
        f.write(result)

    print(f'{changed} cell(s) transformed → {dst}')


if __name__ == '__main__':
    main()
