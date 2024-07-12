import re
def read_ass_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()


def write_ass_file(file_path, lines):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)


def parse_events(lines):
    events = []
    event_section = False
    for line in lines:
        if line.strip().startswith('[Events]'):
            event_section = True
        elif event_section and line.strip().startswith('Dialogue:'):
            events.append(line.strip())
    return events


def transform_events(events):
    transformed_events = []
    num_events = len(events)

    for i, event in enumerate(events):
        prev_line = events[i - 1] if i > 0 else 'Dialogue: 0,0:00:00.00,0:00:00.00,Default,,0,0,0,,...'
        next_line = events[i + 1] if i < num_events - 1 else 'Dialogue: 0,0:00:00.00,0:00:00.00,Default,,0,0,0,,...'

        current_line = event
        transformed_event = f"{prev_line}\n{current_line}\n{next_line}\n"
        transformed_events.append(transformed_event)

    return transformed_events


def main(input_file, output_file):
    lines = read_ass_file(input_file)
    events = parse_events(lines)
    transformed_events = transform_events(events)
    write_ass_file(output_file, transformed_events)


if __name__ == "__main__":
    input_file = 'input_subtitles.ass'
    output_file = 'output_subtitles.ass'
    main(input_file, output_file)
