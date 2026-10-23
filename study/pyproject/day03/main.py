import requests
def fetch_user(username):#发请求、检查状态，成功时返回资料字典
    url="https://api.github.com/users/"+username
    try:
        response=requests.get(url,timeout=10)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print("未找到该用户")
        else:
            print("查询失败")
            print(response.text)
            print(f"状态码：{response.status_code}")
    except requests.exceptions.Timeout:
        print("请求超时，请稍后重试")
    except requests.exceptions.ConnectionError:
        print("网络连接失败，请检查网络")
    except requests.exceptions.JSONDecodeError:
        print("响应格式异常，无法解析 JSON")

def show_user(content):
    print(f"用户名:{content["login"]}")
    print(f"公开仓库数量:{content["public_repos"]}")
    print(f"关注者数量:{content["followers"]}")
    name = content["name"]
    if name is None:
        print("昵称:未填写")
    else:
        print(f"昵称:{name}")
    html_url = content["html_url"]
    print(f"GitHub 主页地址:{html_url}")

def main():
    username = input("请输入用户名").strip()
    if username == "":
        print("用户名不能为空")
        return
    content = fetch_user(username)
    if content is not None:
        show_user(content)


if __name__ == "__main__":
    main()



