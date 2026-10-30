import json
from pathlib import Path
import text_splitter
def load(path):
    try:
        with open(path,"r",encoding="utf-8") as f:
            content=f.read()
        return content
    except OSError as e:
        print(e)
def main():
    list1=[]
    path=Path(__file__).resolve().parent/"docs"
    if path.is_dir():
        for path in path.glob("*.txt"):
            content = load(path)
            if content is None:
                continue
            if content.strip() == "":
                print("文件没有正文")
                continue
            main_content = text_splitter.splitter(content)
            for i in range(0,len(main_content)):
                list1.append({"source":path.name,"chunk_id":path.name+"#"+str(i+1),"text":main_content[i]})
        print(list1)
        try:
            path = Path(__file__).resolve().parent / "data"/"chunks.json"
            with open(path,"w",encoding="utf-8") as f:
                json.dump(list1,f,ensure_ascii=False,indent=4)
            print(f"保存成功，保存位置是{path},保存了{len(list1)}条")
        except OSError as e:
            print(e)
    else:
        print("路径错误")
    message=text_splitter.loader(path)
    if message is not None:
       for i in message:
           if i["chunk_id"]=="学习笔记.txt#2":
               print(i["text"])


if __name__ == '__main__':
    main()