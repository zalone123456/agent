"""第十九天：提供给模型的工具说明。"""

tools = [
    {
        "type": "function",  # 这是一个函数工具
        "function": {
            "name": "select_data_topic",  # 模型请求调用时使用的名称
            "description": "按学习主题精确查询已保存的学习记录，例如查询 Python 的记录。",
            "parameters": {
                "type": "object",  # 参数整体是一个 JSON 对象
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "要查询的学习主题，例如 Python、Git 或 MySQL。",
                    }
                },
                "required": ["topic"],  # 查询时必须提供主题
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_statistics",
            "description": "查询学习记录总数、累计学习分钟数，以及各主题的记录数和累计分钟数。",
            "parameters": {
                "type": "object",
                "properties": {},  # 统计不需要提供参数
                "required": [],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_knowledge",
            "description": "根据问题检索学习笔记和项目资料，返回相关原文片段及来源。",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "需要从学习资料中查找的问题或知识点。",
                    },
                },
                "required": ["query"],
                "additionalProperties": False,
            },
        },
    },
]
