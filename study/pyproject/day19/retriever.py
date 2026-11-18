import chromadb
import pathlib
import embedding_client
import os
def main():
    query = input("问题").strip()
    results=search_knowledge(query)
    print(results)

def search_knowledge(query):
    try:
        # 1. 检查问题
        if not isinstance(query, str) or not query.strip():
            return {
                "ok": False,
                "error": "查询问题不能为空",
            }
        api = os.environ.get("SILICONFLOW_API_KEY")
        if not api or not api.strip():
            return {
                "ok": False,
                "error": "未配置 SiliconFlow API Key",
            }
        embeddings = embedding_client.embedding(api, query)
        if not embeddings:
            return {
                "ok": False,
                "error": "问题向量化失败",
            }

        path = pathlib.Path(__file__).resolve().parent.parent / "day10" / "chroma_db"
        if not path.is_dir():
            return {
                "ok": False,
                "error": "没有找到向量库目录",
            }
        client = chromadb.PersistentClient(path)
        collection = client.get_collection(
            name="learning_docs",
            embedding_function=None
        )
        if collection.count() == 0:
            return {
                "ok": True,
                "data": {"chunks": []},
            }
        results = collection.query(
            query_embeddings=[embeddings],
            n_results=3
        )
        ids = results["ids"][0]
        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        chunks = []

        for i in range(len(ids)):
            metadata = metadatas[i]

            chunk = {
                "chunk_id": ids[i],
                "source": metadata["source"],
                "paragraph_start": metadata["paragraph_start"],
                "paragraph_end": metadata["paragraph_end"],
                "text": documents[i],
            }

            chunks.append(chunk)
        return {
                "ok": True,
                "data": {"chunks": chunks},
        }
    except Exception as e:
        print(f"知识库检索出错：{e}")
        return {
            "ok": False,
            "error": "知识库检索失败",
        }

if __name__=="__main__":
    main()