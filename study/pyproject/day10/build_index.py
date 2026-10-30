import json
import pathlib
import embedding_client
import chromadb
def loader(path):
    try:
        with open(path,"r",encoding="utf-8") as f:
            content = json.load(f)
        print("读取成功")
        return content
    except OSError as e:
        print(e)
        return []
def main():

    ids = []
    documents = []
    metadatas = []
    path=pathlib.Path(__file__).resolve().parent.parent/"day09"/"data"/"chunks.json"
    content=loader(path)
    print(len(content))
    for chunk in content:
        ids.append(chunk["序号"])
        documents.append(chunk["内容"])
        metadatas.append({"source":chunk["文件名"],"paragraph_start":chunk["location"]["paragraph_start"],"paragraph_end":chunk["location"]["paragraph_end"]})
    embeddings = embedding_client.embed_texts(documents)
    if not embeddings :
        print("报错")
        return []
    print(len(embeddings),len(embeddings[0]))
    path=pathlib.Path(__file__).resolve().parent/"chroma_db"
    client=chromadb.PersistentClient(path)
    collection = client.get_or_create_collection(
        name="learning_docs",
        embedding_function=None,
    )
    if len(documents) == len(embeddings) and len(embeddings) == len(metadatas) and len(embeddings) == len(ids):
        collection.upsert(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )
        print(collection.count())
    else:
        print("长度不一致时")

if __name__ == "__main__":
    main()