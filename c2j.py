import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    """
    将 CSV 文件转换为 JSON 文件。

    :param csv_file_path: 输入的 CSV 文件路径
    :param json_file_path: 输出的 JSON 文件路径
    """
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        # 读取 CSV 数据
        csv_reader = csv.DictReader(csv_file)
        data = {row['bank']: {"count": row['count'], "url": row['url']} for row in csv_reader}

    # 写入 JSON 文件
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

    print(f"CSV 数据已成功转换为 JSON 文件：{json_file_path}")


from collections import defaultdict
def csv_to_nested_json(csv_file_path, json_file_path):
    """
    将 CSV 转换为嵌套 JSON 结构。
    :param csv_file_path: 输入的 CSV 文件路径
    :param json_file_path: 输出的 JSON 文件路径
    """
    # 使用 defaultdict 组织数据
    nested_data = defaultdict(list)

    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # 按照 bank 将 series 和 count 嵌套
        for row in csv_reader:
            bank = row["bank"]
            series_info = {"series": row["series"], "count": int(row["count"])}
            nested_data[bank].append(series_info)

    # 转换为普通字典并写入 JSON 文件
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(nested_data, json_file, indent=4, ensure_ascii=False)

    print(f"CSV 数据已成功转换为嵌套 JSON 文件：{json_file_path}")



# 主程序
if __name__ == "__main__":
    # 示例文件路径
    input_csv = "./series.csv"  # 输入的 CSV 文件路径
    output_json = "./series.json"  # 输出的 JSON 文件路径

    # 转换 CSV 到 JSON
    csv_to_nested_json(input_csv, output_json)