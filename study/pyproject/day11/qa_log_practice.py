import json
import pathlib
import tempfile
import os
def save_record(record, file_path):
    temp_path = None
    try:
        if not file_path.exists():
            records=[]
        else:
            with open(file_path,'r',encoding='utf-8') as f:
                records=json.load(f)
        if not isinstance(records, list):
            print("格式错误")
            return
        records.append(record)
        with tempfile.NamedTemporaryFile(
                mode="w",
                encoding="utf-8",
                dir=file_path.parent,
                delete=False,
        ) as temp_file:
            temp_path = pathlib.Path(temp_file.name)
            json.dump(records, temp_file, ensure_ascii=False, indent=4)
        os.replace(temp_path, file_path)

    except json.JSONDecodeError as e:
        print(f"JSON 格式错误：{e}")
        return
    except OSError as e:
        print(e)
        return
    finally:
        if temp_path is not None:
            try:
                temp_path.unlink(missing_ok=True)
            except OSError as e:
                print(f"清理临时文件失败：{e}")
def main():
    record = {
        "问题": "怎么保存聊天记录？",
        "回答": "输入 /save 可以保存。"}
    path=pathlib.Path(__file__).resolve().parent/"practice_records.json"
    save_record(record, path)
if __name__ == '__main__':
    main()