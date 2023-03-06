from pprint import pprint

import inquirer


choices = {"Computers": ["Pc", "Mac"],
           "Books": ["Science Fiction", "Satire", "Biography"],
           "Science": None,
           "Nature": None,
           "Fantasy": None,
           "History": None}

# choices = [("Computers", ("Pc", "Mac")),
#            ("Books", ("Science Fiction", "Satire", "Biography")),
#            "Science",
#            "Nature",
#            "Fantasy",
#            "History"]

questions = [
    inquirer.Checkbox(
        "interests",
        message="What are you interested in?",
        choices=choices,
        default=["Computers", "Books"],
    ),
]

answers = inquirer.prompt(questions)

pprint(answers, indent=4)

# for answer in answers["interests"]:
#     if not isinstance(answer, str) and len(answer) > 0:
#         questions = [
#             inquirer.Checkbox(
#                 f"{answer}:",
#                 message=f"What {answer} are you interested in?",
#                 choices=answer,
#             ), ]
#         answers.update(inquirer.prompt(questions))

for answer in answers["interests"]:
    sub_choices = choices[answer]
    if (sub_choices is not None) and len(sub_choices) > 0:
        questions = [
            inquirer.Checkbox(
                f"{answer}:",
                message=f"What {answer} are you interested in?",
                choices=sub_choices,
            ), ]
        answers.update(inquirer.prompt(questions))

pprint(answers, indent=4)

