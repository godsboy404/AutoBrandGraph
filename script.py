from flask import Flask, jsonify, render_template, request
import json
from anytree import Node, RenderTree

app = Flask(__name__)

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
                Node(f"{series['series']} ({series['count']})", parent=brand_node)

    return root

def generate_tree_string(root):
    tree_str = ""
    for pre, fill, node in RenderTree(root):
        tree_str += f"{pre}{node.name}\n"
    return tree_str

def search_brand_in_tree(root, brand_name):
    matching_nodes = [node for node in root.descendants if brand_name.lower() in node.name.lower()]
    if matching_nodes:
        result = ""
        for node in matching_nodes:
            result += f"{node.name}\n"
            for child in node.children:
                result += f"  └── {child.name}\n"
        return result
    else:
        return None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/full_tree")
def get_full_tree():
    try:
        bank_file = "bank.json"
        series_file = "series.json"
        root = load_data_and_build_tree(bank_file, series_file)
        tree_string = generate_tree_string(root)
        return jsonify({"status": "success", "data": tree_string})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route("/search_brand")
def search_brand():
    try:
        brand_name = request.args.get("brand_name", "").strip()
        if not brand_name:
            return jsonify({"status": "error", "message": "品牌名称不能为空"})

        bank_file = "bank.json"
        series_file = "series.json"
        root = load_data_and_build_tree(bank_file, series_file)
        result = search_brand_in_tree(root, brand_name)
        if result:
            return jsonify({"status": "success", "data": result})
        else:
            return jsonify({"status": "error", "message": "未找到指定品牌"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)