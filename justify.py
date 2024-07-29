import argparse

def justify_text(paragraph, width):
    words = paragraph.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + len(current_line) > width:
            for i in range(width - current_length):
                current_line[i % (len(current_line) - 1 or 1)] += ' '
            lines.append(''.join(current_line))
            current_line = []
            current_length = 0
        current_line.append(word)
        current_length += len(word)

    lines.append(' '.join(current_line).ljust(width))
    return lines

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Justify text to a specified width")
    parser.add_argument("--paragraph-string", type=str, required=True, help="Paragraph to be justified")
    parser.add_argument("--paragraph-width", type=int, required=True, help="Width for justification")

    args = parser.parse_args()
    justified_text = justify_text(args.paragraph_string, args.paragraph_width)

    for idx, line in enumerate(justified_text, start=1):
        print(f"Array [{idx}] = \"{line}\"")
