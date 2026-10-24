import os
from openai import OpenAI, APITimeoutError, APIConnectionError, AuthenticationError, APIStatusError


def ask_model(question):
    try:
        api_key=os.environ.get('DEEPSEEK_API_KEY')
        if not api_key:
            print("配置缺失")
            return
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com",
            timeout=60,
        )
        response = client.chat.completions.create(
            model="deepseek-flash",
            messages=[
                {"role": "system", "content": "你是大肥鱼"},
                {"role": "user", "content": question},
            ],
            stream=False,
            reasoning_effort="high",
            extra_body={"thinking": {"type": "enabled"}},
        )
        usage = response.usage

        if usage is not None:
            print(f"输入 token：{usage.prompt_tokens}")
            print(f"输出 token：{usage.completion_tokens}")
            print(f"总 token：{usage.total_tokens}")
        else:
            print("接口未提供用量信息")
        answer =response.choices[0].message.content
        if  not answer or not answer.strip():
            print("模型未返回有效回答")
            return
        else:
            return answer
    except APITimeoutError as e:
        print(f"请求超时{e}")
    except APIConnectionError as e:
        print(f"网络连接失败{e}")
    except AuthenticationError as e:
        print(f"鉴权失败，请检查密钥{e}")
    except APIStatusError as e:
        print(f"HTTP 错误，状态码：{e.status_code}，详情：{e}")

