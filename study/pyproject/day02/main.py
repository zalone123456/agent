from study_log import *
from pathlib import Path
def main_interface():
    print("===== 学习记录统计器 =====")
    print("1. 添加学习记录")
    print("2. 查看全部记录")
    print("3. 查看统计结果")
    print("4. 保存记录")
    print("0. 退出程序")
    choose=(input("请选择功能"))
    match choose :
        case "1":add_learnrecord(list1)
        case "2":checkrecord(list1)
        case "3":checkstatistics(list1)
        case "4":save_records(list1,file_path)
        case "0":return False
        case _:print("输入错误")
        # 其他操作完成后返回 True，外层循环会继续显示菜单。
    return True
if __name__ == "__main__":
    file_path = Path(__file__).resolve().parent / "learning_records.json"
    # 放在循环外，只初始化一次，避免每轮循环清空记录。
    list1=load_records(file_path)
    # while True 会反复执行，直到遇到 break。
    while True:
        # 先调用菜单函数，等操作结束后判断其返回值。
        # 输入 0 时返回 False，于是执行 break，结束循环。
        if main_interface() is False:
            break
