# Please install OpenAI SDK first: `pip3 install openai`
import model_client
import time


def main():
    question = input("你的问题是什么").strip()
    if question=="":
        print("问题不能为空")
        return
    start1 = time.perf_counter()
    answer = model_client.ask_model(question)
    finally1=time.perf_counter()
    if answer is not None:
        print(answer)
    print(f"耗时：{finally1-start1:.2f}秒")
if __name__ == "__main__":
    main()


