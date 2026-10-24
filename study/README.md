# Python 实习学习记录

按学习日保存 Python 练习代码。目前包括学习记录统计器、GitHub 用户资料查询，以及 DeepSeek 单轮问答程序。后续在本 README 中继续更新进度。

## 目录结构

```text
study/
├── README.md
└── pyproject/
    ├── day01/    # 学习记录统计器基础版
    ├── day02/    # JSON 保存、读取和数据检查
    ├── day03/    # GitHub 用户资料查询
    └── day04/
        ├── main.py           # 输入、计时和显示
        └── model_client.py   # 配置、模型调用、用量和异常处理
```

## 学习进度

| 阶段 | 主要内容 |
| --- | --- |
| 第一天 | 输入检查、列表与字典、循环、函数、异常处理、拆模块、Python 环境和 Git 基础 |
| 第二天 | 文件读写、JSON、手动保存、启动读取、记录格式检查和文件异常处理 |
| 第三天 | HTTP、GET 请求、状态码、JSON 响应、超时和网络异常 |
| 第四天 | DeepSeek API、环境变量、SDK、单轮问答、异常分类、调用耗时和 token 用量 |

## 环境与依赖

当前练习使用 Python 3.12，Conda 环境名为 `intership`。第三天部分 f-string 使用了 Python 3.12 支持的引号写法，因此运行完整项目请使用 Python 3.12 或以上版本。

在 Anaconda Prompt 中激活自己的项目环境，再安装第三天和第四天使用的库：

```bash
conda activate intership
python -m pip install requests openai
```

第一天、第二天只使用标准库。PyCharm 中也应选择同一个环境的解释器。以上环境名按自己的实际配置调整。

## 运行方式

以下命令均在 `study` 目录下执行，每次选择一个程序运行：

```bash
python pyproject/day01/main.py
python pyproject/day02/main.py
python pyproject/day03/main.py
python pyproject/day04/main.py
```

也可以在 PyCharm 中选择对应的 `main.py` 运行。第四天需要先在实际使用的运行配置中设置 API Key。

## 第一天和第二天 学习记录统计器

支持添加学习主题和分钟数、查看记录、统计记录数量、累计时长和各主题时长。拒绝空主题和非正整数分钟数。

| 菜单输入 | 功能 |
| --- | --- |
| 1 | 添加记录 |
| 2 | 查看记录 |
| 3 | 查看统计 |
| 4 | 保存记录，仅第二天提供 |
| 0 | 退出 |

第二天版本选择 `4` 后，将全部记录保存到 `day02/main.py` 同目录的 `learning_records.json`。退出不会自动保存；启动时自动读取历史记录。

记录采用列表中嵌套字典的格式，每条记录只有一组键值对：主题为非空字符串，分钟数为正整数。

```json
[
    {"Python": 45},
    {"Git": 30}
]
```

文件不存在时，以空列表开始。JSON 损坏、结构错误或其他读取失败时，报错并停止启动，先检查或备份原文件。保存失败时提示原因。

验证示例：添加 Python 45、Git 30、Python 60，保存并重启后应仍有 3 条、135 分钟；Python 累计 105 分钟，Git 累计 30 分钟。

## 第三天 GitHub 用户资料查询

输入 GitHub 用户名后，查询 `https://api.github.com/users/用户名`，显示用户名、昵称、公开仓库数量、关注者数量和主页地址。没有填写昵称时显示“未填写”。

已处理空输入、404、其他非成功状态、请求超时、网络连接失败和 JSON 解析失败。请求设置 `timeout=10`。

成功查询示例：输入 `zalone123456`，可显示用户名和 `https://github.com/zalone123456`；仓库数和关注者数以接口当前返回为准。

当前查询不使用 Token，受 GitHub API 的未认证请求限额约束。出现 `403` 时查看响应正文；若提示 `API rate limit exceeded`，暂停请求并等待恢复。当前未额外校验响应字段是否完整。

## 第四天 DeepSeek 单轮问答

使用 `openai` Python SDK 调用 DeepSeek，当前代码配置为：

- 服务商：DeepSeek。
- API 基础地址：`https://api.deepseek.com`。
- 模型：`deepseek-flash`。
- 非流式输出，开启思考模式，推理力度为 `high`。
- 客户端超时参数：60 秒；SDK 重试可能使总耗时更长。

### 密钥配置

在 DeepSeek 开放平台创建 API Key，并确认账户具备可用额度。代码通过环境变量 `DEEPSEEK_API_KEY` 读取密钥。

在 PyCharm 中进入 Run → Edit Configurations，选择脚本路径指向 `day04/main.py` 的配置，在 Environment variables 中添加：

| 名称 | 值 |
| --- | --- |
| DEEPSEEK_API_KEY | `<你的 DeepSeek API Key>`，占位说明，不是真实密钥 |

保存后通过该配置运行。若在终端执行，需要在该终端单独配置环境变量；PyCharm 的运行配置不会自动应用到终端。当前代码不会自动读取 `.env` 文件。

不要把真实密钥写进代码、README、截图或 Git 提交。

### 行为与错误处理

程序每次运行接收一个问题，调用一次模型，打印回答后结束；同时显示调用耗时，以及接口提供的输入、输出和总 token 数。未提供用量时明确提示，不自行估算。

- 空问题：提示后结束，不调用模型。
- 密钥未设置或为空：提示“配置缺失”，不创建客户端。
- 超时、网络连接失败、鉴权失败：分别提示。
- 其他 HTTP 错误：显示状态码及错误详情，便于区分余额、参数或模型配置问题。
- 回答为 None、空字符串或纯空格：提示未返回有效回答。

示例问题：“请用两句话解释 Python 字典。”回答由模型生成，不要求每次完全一致。

遇到过的问题：创建客户端时报 Missing credentials，原因是实际运行配置没有提供 `DEEPSEEK_API_KEY`；将环境变量添加到第四天使用的运行配置后解决。

当前实现为单轮问答，尚未加入连续对话和历史保存，也未完整验证响应结构，例如候选结果列表为空的情况。调用可能产生费用，以服务商当前规则为准。

## 版本管理

代码和本 README 纳入 Git。仓库根目录的 `.gitignore` 忽略 Python 缓存、PyCharm 本地配置、虚拟环境、`.env` 和个人学习记录文件。

提交前通过 `git status`、`git diff` 和 `git diff --staged` 检查实际内容，确认没有密钥。`commit` 保存本地版本，`push` 上传到远程仓库。

此前 HTTPS 推送遇到 OpenSSL 连接错误，临时使用 Windows Schannel 后推送成功；需要时可为当前仓库配置该 TLS 后端，保持证书验证开启。
