# Please install OpenAI SDK first: `pip3 install openai`
import model_client
import time
import chat_storage
from pathlib import Path


def main():
    messages = [
        {"role": "system", "content": "你是大肥鱼"},
    ]
    file_path = Path(__file__).resolve().parent / "chat_history.json"
    while True:
        question = input("你的问题是什么").strip()
        if question == "":
            print("问题不能为空")
            continue
        if question == "/exit":
            break
        if question == "/clear":
            messages = [
                {"role": "system", "content": "你是大肥鱼"},
            ]
            print("上下文已清空")
            continue
        if question == "/save":
            chat_storage.save(messages,file_path)
            continue
        messages.append({"role": "user", "content": question})
        #start1 = time.perf_counter()
        answer = model_client.ask_model(messages)
       # finally1=time.perf_counter()
        if answer is not None:
            print(answer)
            messages.append({"role": "assistant", "content": answer})
        else:
            del messages[-1]
            continue
        if len(messages) > 11:
            del messages[1]
            del messages[1]


if __name__ == "__main__":
    main()


