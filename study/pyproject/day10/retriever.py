import chromadb
import pathlib
import embedding_client
def main():
    question = questions()
    results=retrieve(question,3)
    if not results:
        return
    # 外层：遍历每个问题的结果组
    for i in range(len(results["documents"])):
        print(f"\n===== 问题 {i + 1} 的检索结果 =====")

        # 内层：遍历当前问题找到的每条记录
        for j in range(len(results["documents"][i])):
            chunk_id = results["ids"][i][j]
            text = results["documents"][i][j]
            metadata = results["metadatas"][i][j]
            distance = results["distances"][i][j]

            print(f"\n第 {j + 1} 条：")
            print(f"编号：{chunk_id}")
            print(f"来源：{metadata['source']}")
            print(
                f"段落：{metadata['paragraph_start']}"
                f"～{metadata['paragraph_end']}"
            )
            print(f"距离：{distance}")
            print(f"正文：{text}")

def retrieve(questions, top_k=3):
    if not questions:
        return
    path = pathlib.Path(__file__).resolve().parent / "chroma_db"
    if not path.is_dir():
        print("请先运行建库程序")
        return
    client = chromadb.PersistentClient(path)

    try:
        collections = client.get_collection(
            name="learning_docs",
            embedding_function=None,
        )
        if collections.count()==0:
            print("集合为空，请先运行建库程序")
            return
        question_vectors = embedding_client.embed_texts(questions)
        if not question_vectors:
            return
        results = collections.query(
            query_embeddings=question_vectors,
            n_results=top_k,

        )
        return results
    except chromadb.errors.NotFoundError:
        print("未找到集合，请先运行建库程序")
        return


def questions():
    questions=[]
    while True:
        quesion=input("请输入问题").strip()
        if not quesion:
            break
        else:
            questions.append(quesion)
    if len(questions)>0:
        return questions
    else:
        print("问题是空")
        return
if __name__ == "__main__":
    main()