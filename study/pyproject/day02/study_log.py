import json


def add_learnrecord(list1):
    content=input("请输入学习主题：").strip()
    if content=="" :
        print("错误：学习主题不能为空！")
        return

    study_min=input("请输入学习分钟数：").strip()
    try:
        study_min=int(study_min)
        if study_min <= 0:
            raise ValueError("分钟数必须是正整数")
    except ValueError:
        print("输入错误")
        return
    list1.append({content:study_min})
    print("添加成功")

def checkrecord(list1):
    if list1:
        for number, record in enumerate(list1, start=1):#可以通过items，来获得key 和value
            for topic, minutes in record.items():
                print(f"{number}.{topic}————{minutes}分钟")
    else:
        print("暂无学习记录。")

def checkstatistics(list1):
    if len(list1)==0:
        print("暂无学习记录")
        return

    print(f"记录数量：{len(list1)}条")
    total_minutes = 0
    for record in list1:
        for minutes in record.values():
            total_minutes += minutes

    print(f"累计学习：{total_minutes}分钟")
    print("按主题统计：")

    # 汇总字典：键是学习主题，值是这个主题的累计分钟数。
    topic_totals = {}

    # 外层循环逐条取出学习记录，每条 record 都是一个字典。
    for record in list1:
        # items() 同时取出记录中的主题和分钟数。
        for topic, minutes in record.items():
            # 第一次遇到该主题时，先创建对应的键，累计值设为 0。
            if topic not in topic_totals:
                topic_totals[topic] = 0

            # 每条记录都要累加；已有主题不会重新归零。
            # 这句要放在 if 外面，否则同一主题后续的记录不会被累计。
            topic_totals[topic] += minutes

    # 全部统计完成后，再逐项输出，每个主题只输出一次。
    for topic, minutes in topic_totals.items():
        print(f"{topic}：{minutes}分钟")

def save_records(list1,file_path):
    try:
        with open(file_path,"w",encoding="utf-8") as f:
            json.dump(list1,f,ensure_ascii=False,indent=4)
        print("写入成功")
    except OSError as e:
        print(f"保存失败：{e}")

def load_records(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            records = json.load(f)
    except FileNotFoundError:
        print("暂无历史记录")
        return []
    except json.JSONDecodeError:
        raise ValueError("JSON 文件损坏，请检查文件")
    except OSError as e:
        raise OSError(f"读取失败：{e}")

    if not isinstance(records, list):
        raise ValueError("记录格式错误：最外层必须是列表")

    for record in records:
        if not isinstance(record, dict) or len(record) != 1:
            raise ValueError("每条记录必须是只有一个键值对的字典")

        for topic, minutes in record.items():
            if not isinstance(topic, str) or not topic.strip():
                raise ValueError("学习主题必须是非空字符串")

            if type(minutes) is not int or minutes <= 0:
                raise ValueError("分钟数必须是正整数")

    print("读取成功")
    return records