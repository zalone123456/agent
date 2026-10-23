import json


def save_records(records,file_path):
    with open(file_path,'w',encoding='utf-8') as f:
        json.dump(records,f,ensure_ascii=False,indent=4)
    print('records saved')
    return
def load_records(file_path):
    with open(file_path,'r',encoding='utf-8') as f:
        if records:
            records = json.load(f)
            return records
        else:
            print('暂无历史记录')
            return []
def load_records(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            records = json.load(f)
        return records
    except FileNotFoundError:
        print("暂无历史记录")
        return []