import json
def save(message,path):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(message, f, ensure_ascii=False,indent=4)
        print("保存成功")
    except OSError as e:
        print(e)
