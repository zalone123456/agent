import  json
def splitter(content,chunks_size=400,overlap=80):
    if not chunks_size>0:
        raise ValueError("chunks_size must be greater than 0")
    if not 0<=overlap<chunks_size:
        raise  ValueError("overlap 必须大于等于 0，且小于 chunks_size")
    chunks = []
    start = 0

    while start < len(content):
        end = start + chunks_size
        chunks.append(content[start:end])

        if end >= len(content):
            break

        start += chunks_size - overlap

    return chunks
def loader(path):
    try:
        with open(path,"r",encoding="utf-8") as f:
            content = json.load(f)
        print("读取成功")
        return content
    except OSError as e:
        print(e)

def save(path, content):
    try:
        with open(path,"w",encoding="utf-8") as f:
            json.dump(content, f,ensure_ascii=False,indent=4)
        print("保存成功")
    except OSError as e:
        print(e)

        ''''
每轮从 start 开始，取最多 400 字符。
结束位置超过正文长度时，切片会自动截到末尾，所以短文本和最后一段都能直接处理。

这一块已经到达正文末尾，就结束。
例如正文恰好 400 字符，取完第一块立即停止，避免再取一块重复的尾部。

还没到末尾，起点前进 320。
每块取 400，起点前进 320，相邻自然重叠 80。
''''''







''''''
def splitter(content):
    text=[]
    length = len(content)
    str_Overlap=80
    start = 0
    flag=1
    n=1
    while(len(content)-start>=400):
        if flag==1:
            text.append(content[(n-1)*400:n*400])
            flag=0
            length = length - 400
        else:
            text.append(content[(n - 1) * (400-str_Overlap):n * 400-str_Overlap*(n-1)])
            length = length - 320
        start = start+320
        n=n+1
    if(length!=0):
        text.append(content[(n - 1) * (400-str_Overlap):len(content)])
    return text
'''''''''''