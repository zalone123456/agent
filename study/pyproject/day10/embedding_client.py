import os
import requests


def embed_texts(texts):
    list1=[]
    api=os.environ.get("SILICONFLOW_API_KEY")
    if not api or not api.strip():
        print("api错误")
        return []
    if  texts ==[]:
        return []
    try:
        response = requests.post(
            "https://api.siliconflow.cn/v1/embeddings",
            headers={
                "Authorization": f"Bearer {api}",
                "Content-Type": "application/json",

            },
            json={
                "input":texts,
                "model": "BAAI/bge-m3"
            },
        timeout=30
        )
        response.raise_for_status()
        content = response.json()
    except requests.exceptions.Timeout as e:
        print(e)
        return[]
    except requests.exceptions.ConnectionError as e:
        print(e)
        return[]
    except requests.exceptions.HTTPError as e:
        print(e)
        return[]
    except  OSError as e:
        print(e)
        return[]

    #print(content)
    sorted_data=sorted(content["data"], key=get_index)
    for i in range(0,len(sorted_data)):
        #print(f"index:{sorted_data[i]["index"]}")
        #print(f"向量维度：{len(sorted_data[i]["embedding"])}")
        #print(f"前5个数字{sorted_data[i]["embedding"][:5]}")
        list1.append(sorted_data[i]["embedding"])
    return list1
def get_index(items):
    return items["index"]
def  main():
    texts = ["怎样保存聊天记录？","输入 /save 保存当前聊天历史。","今天的天气很好"]
    content=embed_texts(texts)
    for i in range(0,len(content)):
        print(f"index:{i},前5个数字:{content[i][:5]}")
if __name__ == "__main__":
    main()