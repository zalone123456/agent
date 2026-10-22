def add_learnrecord():
    content=input("请输入学习主题：").strip()
    if content=="" :
        print("错误：学习主题不能为空！")
        return

    study_min=input("请输入学习分钟数：").strip()
    try:
        study_min=int(study_min)
        if study_min <= 0:
            raise ValueError("分钟数必须是正整数")
    except:
        print("输入错误")
        main_interface()
        return
    list1.append({content:study_min})
    print("添加成功")

def checkrecord():
    if list1:
        for record in list1:#可以通过items，来获得key 和value
            for topic, minutes in record.items():
                print(f"{topic}————{minutes}分钟")
    else:
        print("暂无学习记录。")

def checkstatistics():
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

def main_interface():
    print("===== 学习记录统计器 =====")
    print("1. 添加学习记录")
    print("2. 查看全部记录")
    print("3. 查看统计结果")
    print("0. 退出程序")
    choose=(input("请选择功能"))
    match choose :
        case "1":add_learnrecord()
        case "2":checkrecord()
        case "3":checkstatistics()
        case "0":return False
        case _:
                print("输入错误")
                main_interface()
        # 其他操作完成后返回 True，外层循环会继续显示菜单。
    return True
if __name__ == "__main__":
    # 放在循环外，只初始化一次，避免每轮循环清空记录。
    list1 = []

    # while True 会反复执行，直到遇到 break。
    while True:
        # 先调用菜单函数，等操作结束后判断其返回值。
        # 输入 0 时返回 False，于是执行 break，结束循环。
        if main_interface() is False:
            break
