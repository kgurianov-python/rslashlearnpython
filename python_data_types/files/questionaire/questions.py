from collections import defaultdict


def format_questions(file_path, start=1):
    count = start
    start_marker = f"{count}."
    stop_marker = f"Answer"
    save_lines = False
    questions = defaultdict(list)
    print(f"{start_marker=}, {stop_marker=}")
    with open(file_path, 'r') as file:
        for line in file:
            if start_marker in line:
                save_lines = True
            if save_lines:
                questions[start_marker].append(line)
            if stop_marker in line:
                save_lines = False
                count = count + 1
                start_marker = f"{count}."

    return questions


def save_formatted_questions(file_path, questions):
    with open(file_path, 'w') as file:
        for question in questions:
            file.write(question['text'])
            for option in question['options']:
                file.write(option + '\n')
            file.write('\n')


file_path = "input.txt"
unformatted_questions = format_questions(file_path)
for key, val in unformatted_questions.items():
    print(len(val))
    print(*val, sep='\r')

# save_formatted_questions("output.txt", formatted_questions)
