import json
from email import message
from pathlib import Path
import text_splitter

def load(path):
    try:
        with open(path,"r",encoding="utf-8") as f:
            content=f.read()
        return content
    except OSError as e:
        print(e)

def process_document(content, source,chunks_size=400,overlap=80):
    if not chunks_size > 0:
        raise ValueError("chunks_size must be greater than 0")
    if not 0 <= overlap < chunks_size:
        raise ValueError("overlap 必须大于等于 0，且小于 chunks_size")
    paragrahs = []
    chunks = []
    if content is None:
        print("路径错误")
        return[]
    if not content.strip() :
        print("文件没有正文")
        return[]
    for i in content.split("\n\n"):
        if i.strip():
            paragrahs.append(i)
    real_content=""
    chunk_id=1
    for i in range(0,len(paragrahs)):
        if len(paragrahs[i])<=chunks_size:
            if not real_content:
                start = i+1
                real_content=paragrahs[i]
            elif len(real_content+"\n\n"+paragrahs[i] )<=chunks_size:
                real_content=real_content+"\n\n"+paragrahs[i]
            else:
                chunks.append({"文件名":source,"location":{"paragraph_start": start, "paragraph_end": i},"序号":source+"#"+f"{chunk_id}","内容":real_content})
                chunk_id=chunk_id+1
                real_content = paragrahs[i]
                start = i + 1
            if i==len(paragrahs)-1:
                chunks.append({"文件名":source,"location":{"paragraph_start": start, "paragraph_end": i+1},"序号":source+"#"+f"{chunk_id}","内容":real_content})
        else:
            if  real_content:
                chunks.append({"文件名":source,"location":{"paragraph_start": start, "paragraph_end": i},"序号":source+"#"+f"{chunk_id}","内容":real_content})
                chunk_id=chunk_id+1
                real_content = ""
            for a in text_splitter.splitter(paragrahs[i],chunks_size,overlap):
                chunks.append({"文件名":source,"location":{"paragraph_start": i+1, "paragraph_end": i+1},"序号":source+"#"+f"{chunk_id}","内容":a})
                chunk_id=chunk_id+1
    return chunks
def main():
    path = Path(__file__).resolve().parent / "docs"
    all_chunks = []
    for i in sorted(path.glob("**/*.txt")):
        source=i.relative_to(path).as_posix()
        content = load(i)
        chunks=process_document(content, source,400,80)
        all_chunks.extend(chunks)
    print(all_chunks)

    path_save=Path(__file__).resolve().parent/"data"/"chunks.json"
    path_save.parent.mkdir(parents=True, exist_ok=True)
    text_splitter.save(path_save,all_chunks)




if __name__ == '__main__':
    main()

