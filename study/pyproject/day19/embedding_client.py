import os
import  requests

def embedding(api,question):
    try:
        response = requests.post(
            "https://api.siliconflow.cn/v1/embeddings",
            headers={
                "Authorization": f"Bearer {api}",
                "Content-Type": "application/json"
            },
            json={
                "input": question,
                "model": "BAAI/bge-m3"
            },
        timeout=30
        )
        response.raise_for_status()
        embedding = response.json()["data"][0]["embedding"]
        return embedding
    except Exception as e:
        print(e)

def main():
    api=os.environ.get("SILICONFLOW_API_KEY")
    if not api or not api.strip():
        print("未配置 API Key")
        return
    question=input("问题").strip()
    if not question :
        return
    embeddings=embedding(api,question)
    if not embeddings:
        return
    print(embeddings[:5])
    print(len(embeddings))
if __name__ == "__main__":
    main()