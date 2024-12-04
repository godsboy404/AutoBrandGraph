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
    with open(bank_file, mode='r', encoding='utf-8') as f:
        bank_data = json.load(f)

    with open(series_file, mode='r', encoding='utf-8') as f:
        series_data = json.load(f)

    root = Node("Car Knowledge Graph")

    # 添加品牌节点
    brand_nodes = {}
    for brand_name, details in bank_data.items():
        brand_node = Node(
            f"{brand_name} ({details['count']})",
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
                    f"{series['series']} ({series['count']})",
                    parent=brand_node
                )

    return root


def search_in_tree(root, query):
    """
    根据输入查询品牌或车型信息
    :param root: 树的根节点
    :param query: 搜索关键字
    """
    results = []

    # 查找品牌节点
    brand_nodes = [node for node in root.children if query.lower() in node.name.lower()]
    for brand_node in brand_nodes:
        results.append({
            "type": "brand",
            "name": brand_node.name.split(" (")[0],
            "url": getattr(brand_node, "url", "无URL信息"),
            "models": [child.name.split(" (")[0] for child in brand_node.children]
        })

    # 查找车型节点
    model_nodes = [node for node in root.descendants if query.lower() in node.name.lower()]
    for model_node in model_nodes:
        if model_node not in brand_nodes:
            parent_brand_node = model_node.parent
            results.append({
                "type": "model",
                "name": model_node.name.split(" (")[0],
                "brand_url": getattr(parent_brand_node, "url", "无URL信息")
            })

    return results


def display_tree(root):
    """
    打印树结构
    :param root: 树的根节点
    """
    for pre, fill, node in RenderTree(root):
        print(f"{pre}{node.name}")


def export_tree_to_json(root, output_file="tree.json"):
    """
    导出树结构到 JSON 文件
    :param root: 树的根节点
    :param output_file: 输出的 JSON 文件路径
    """
    exporter = JsonExporter(indent=2)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(exporter.export(root))
    print(f"JSON 文件已生成：{output_file}")


def main():
    """
    主函数，提供用户界面与功能
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
    print("2. 查询品牌或车型")
    print("3. 导出知识图谱为 JSON 文件")

    while True:
        choice = input("请输入选项（1、2、3，输入'q'退出）：").strip()

        if choice == "1":
            print("\n汽车品牌知识图谱：")
            display_tree(car_tree_root)
        elif choice == "2":
            query = input("请输入品牌或车型名称：").strip()
            if not query:
                print("请输入有效的品牌或车型名称！")
                continue

            results = search_in_tree(car_tree_root, query)
            if results:
                print("\n查询结果：")
                for item in results:
                    if item["type"] == "brand":
                        print(f"品牌: {item['name']}")
                        print(f"  品牌页面: {item['url']}")
                        print("  车型:")
                        for model in item["models"]:
                            print(f"    - {model}")
                    elif item["type"] == "model":
                        print(f"车型: {item['name']}")
                        print(f"  母品牌页面: {item['brand_url']}")
            else:
                print(f"未找到与 '{query}' 相关的品牌或车型！")
        elif choice == "3":
            output_file = input("请输入导出文件的名称（默认为 tree.json）：").strip()
            output_file = output_file if output_file else "tree.json"
            export_tree_to_json(car_tree_root, output_file)
        elif choice.lower() == "q":
            print("感谢使用汽车品牌知识图谱系统！再见！")
            break
        else:
            print("无效选项，请重新输入！")


if __name__ == "__main__":
    main()
