import json

from anytree import Node, RenderTree
from anytree.exporter import JsonExporter


def load_data_and_build_tree(bank_file, series_file):
    """
    从 JSON 文件加载数据并构建知识图谱树
    :param bank_file: 品牌信息的 JSON 文件路径
    :param series_file: 车型信息的 JSON 文件路径
    :return: 构建完成的树根节点
    """
    # 加载 JSON 数据
    with open(bank_file, mode='r', encoding='utf-8') as f:
        bank_data = json.load(f)

    with open(series_file, mode='r', encoding='utf-8') as f:
        series_data = json.load(f)

    # 创建根节点
    root = Node("Car Knowledge Graph")

    # 添加品牌节点
    brand_nodes = {}  # 用于存储品牌节点引用
    for brand_name, details in bank_data.items():
        brand_node = Node(
            f"{brand_name} ({details['count']})",  # 节点名称包含品牌名称和数量
            parent=root,
            url=details["url"]
        )
        brand_nodes[brand_name] = brand_node

    # 添加车型节点
    for brand_name, series_list in series_data.items():
        if brand_name in brand_nodes:
            brand_node = brand_nodes[brand_name]
            for series in series_list:
                Node(
                    f"{series['series']} ({series['count']})",  # 车型名称包含车型和数量
                    parent=brand_node
                )

    return root


def display_tree(root):
    """
    打印树结构
    :param root: 树的根节点
    """
    for pre, fill, node in RenderTree(root):
        print(f"{pre}{node.name}")


def find_brand(root, brand_name):
    """
    根据品牌名称查找并显示相关信息
    :param root: 树的根节点
    :param brand_name: 品牌名称
    """
    # 查找所有匹配的品牌节点
    brand_nodes = [node for node in root.descendants if brand_name in node.name]

    if brand_nodes:
        brand_node = brand_nodes[0]  # 只返回第一个匹配
        print(f"品牌: {brand_node.name}")
        print(f"  品牌页面: {brand_node.url}")
        for child in brand_node.children:
            print(f"  - 车型: {child.name}")
    else:
        print(f"未找到品牌: {brand_name}")


def export_tree_to_json(root, output_file="tree.json"):
    exporter = JsonExporter(indent=2)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(exporter.export(root))
    print(f"JSON 文件已生成：{output_file}")


def main():
    """
    主函数，提供欢迎界面和功能选择
    """
    # JSON 文件路径
    bank_json_path = "bank.json"
    series_json_path = "series.json"

    # 构建知识图谱树
    car_tree_root = load_data_and_build_tree(bank_json_path, series_json_path)

    # 欢迎界面
    print("欢迎使用汽车品牌知识图谱系统！")
    print("请选择功能：")
    print("1. 输出全部知识图谱")
    print("2. 查询特定品牌")

    while True:
        choice = input("请输入选项（1或2，输入'q'退出）：").strip()

        if choice == "1":
            print("\n汽车品牌知识图谱：")
            display_tree(car_tree_root)
        elif choice == "2":
            brand_name = input("请输入品牌名称：").strip()
            print(f"\n查询品牌 '{brand_name}':")
            find_brand(car_tree_root, brand_name)
        elif choice.lower() == "q":
            print("感谢使用汽车品牌知识图谱系统！再见！")
            break
        else:
            print("无效选项，请重新输入！")


if __name__ == "__main__":
    main()
