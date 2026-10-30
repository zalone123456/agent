from pathlib import Path
import text_splitter


def check_questions():
    path = Path(__file__).resolve().parent / "evaluation" / "questions.json"
    questions = text_splitter.loader(path)
    print(len(questions))
    kinds = {}
    for i in questions:
        if i["type"] not in kinds:
            kinds[i["type"]] = 1
        else:
            kinds[i["type"]] = kinds[i["type"]] + 1
    print(kinds)
if __name__ == "__main__":
    check_questions()