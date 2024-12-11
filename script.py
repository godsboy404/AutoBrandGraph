from flask import Flask, jsonify, render_template, request
from anytree import Node
import json

app = Flask(__name__)

# 加载数据并构建知识图谱树
def load_data_and_build_tree(bank_file, series_file):
    with open(bank_file, mode='r', encoding='utf-8') as f:
        bank_data = json.load(f)

    with open(series_file, mode='r', encoding='utf-8') as f:
        series_data = json.load(f)

    root = Node("Car Knowledge Graph")
    brand_nodes = {}

    for brand_name, details in bank_data.items():
        brand_node = Node(
            f"{brand_name} ({details['count']})",
            parent=root,
            url=details["url"]
        )
        brand_nodes[brand_name] = brand_node

    for brand_name, series_list in series_data.items():
        if brand_name in brand_nodes:
            brand_node = brand_nodes[brand_name]
            for series in series_list:
                Node(
                    f"{series['series']} ({series['count']})",
                    parent=brand_node
                )
    return root

# 查找品牌信息
def search_brand_in_tree(root, brand_name):
    brand_nodes = [node for node in root.children if brand_name.lower() in node.name.lower()]
    results = []

    for brand_node in brand_nodes:
        results.append({
            "type": "brand",
            "name": brand_node.name.split(" (")[0],
            "url": getattr(brand_node, "url", "无URL信息"),
            "models": [child.name.split(" (")[0] for child in brand_node.children]
        })

    model_nodes = [node for node in root.descendants if
                   brand_name.lower() in node.name.lower() and node not in brand_nodes]
    for model_node in model_nodes:
        # 查找车型的母品牌 URL
        parent_brand_node = model_node.parent
        brand_url = getattr(parent_brand_node, "url", "无URL信息")
        results.append({
            "type": "model",
            "name": model_node.name.split(" (")[0],
            "brand_url": brand_url
        })

    return results if results else None

# 加载 JSON 数据并构建知识图谱树
bank_file = "bank.json"
series_file = "series.json"
tree_root = load_data_and_build_tree(bank_file, series_file)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/full_tree", methods=["GET"])
def get_full_tree():
    def render_tree(node, prefix=""):
        lines = [f"{prefix}{node.name}"]
        for child in node.children:
            lines.extend(render_tree(child, prefix + "│   "))
        return lines

    tree_lines = render_tree(tree_root)
    return jsonify({"status": "success", "data": "\n".join(tree_lines)})

@app.route("/search_brand", methods=["GET"])
def search_brand():
    brand_name = request.args.get("brand_name", "").strip()
    if not brand_name:
        return jsonify({"status": "error", "message": "品牌名称不能为空"})

    results = search_brand_in_tree(tree_root, brand_name)
    if results:
        return jsonify({"status": "success", "data": results})
    else:
        return jsonify({"status": "error", "message": f"未找到品牌或车型 '{brand_name}'"})

if __name__ == "__main__":
    app.run(debug=True)
