# 汽车品牌知识图谱

## 选题场景

> 随着电动车、混动车的普及，汽车市场正在经历从燃油车向新能源车转型的过程。各国政府推出的碳中和政策（如中国的“双碳目标”）则加速了这一过程。不同品牌在技术路径（如纯电动、氢燃料电池）上各有差异，消费者难以快速了解。知识图谱通过结构化、可视化的信息帮助消费者做出理性选择，避免在选购时常常面对信息过载问题。

> 消费者需求的多样化导致市场细分（如豪华车、经济型车、新能源车）愈加复杂。品牌知识图谱能帮助企业优化市场布局和产品线规划，直观地反映品牌市场定位、车型分布和竞争优势，展示不同品牌的技术积累和市场表现。

> 目前的汽车品牌和车型信息散落在官网、论坛、媒体等渠道，消费者很难系统地掌握全面的信息。通过知识图谱整合这些分散的信息，可以提高信息获取效率。

### 消费者导向
- 选车推荐，知识普及：
- 通过知识图谱帮助用户提供品牌和车型知识的普及，筛选和比较不同品系的信息

### 企业导向
- 市场分析、售后服务优化、精准营销；
- 利用知识图谱细化用户画像，精准匹配汽车广告与用户需求

### 行业导向
- 技术创新、历史与合作研究；
- 传统能源汽车与新型能源汽车的优劣以及政府红利侧重点

## _初步企划——ver0.1_

- 使用Python语言
- 使用个性化的数据结构-树:
```python
class TreeNode:
    """
    树节点类，用于存储知识图谱中的每个节点。
    """
    def __init__(self, name, count=None, url=None):
        """
        初始化节点
        :param name: 节点名称（品牌/车型名称）
        :param count: 节点相关数量信息（如品牌或车型数量）
        :param url: 节点的相关链接（如品牌官网）
        """
        self.name = name
        self.count = count
        self.url = url
        self.children = []  # 子节点列表

    def add_child(self, child_node):
        """
        向节点添加子节点
        :param child_node: 子节点对象
        """
        self.children.append(child_node)

    def __repr__(self, level=0):
        """
        递归打印节点结构
        :param level: 当前层级（用于缩进）
        """
        ret = "\t" * level + repr(self.name) + (f" ({self.count})" if self.count else "") + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

# 创建根节点
root = TreeNode("汽车知识图谱")

# 添加品牌节点
mercedes = TreeNode("奔驰", count=100, url="https://www.mercedes-benz.com")
bmw = TreeNode("宝马", count=80, url="https://www.bmw.com")
toyota = TreeNode("丰田", count=150, url="https://www.toyota.com")

root.add_child(mercedes)
root.add_child(bmw)
root.add_child(toyota)

# 添加车型节点
mercedes.add_child(TreeNode("C-Class", count=30))
mercedes.add_child(TreeNode("E-Class", count=40))
mercedes.add_child(TreeNode("S-Class", count=30))

bmw.add_child(TreeNode("3 Series", count=40))
bmw.add_child(TreeNode("5 Series", count=30))
bmw.add_child(TreeNode("X5", count=10))

toyota.add_child(TreeNode("Corolla", count=70))
toyota.add_child(TreeNode("Camry", count=50))
toyota.add_child(TreeNode("RAV4", count=30))

# 打印树结构
print(root)

# output
'汽车知识图谱'
	'奔驰' (100)
		'C-Class' (30)
		'E-Class' (40)
		'S-Class' (30)
	'宝马' (80)
		'3 Series' (40)
		'5 Series' (30)
		'X5' (10)
	'丰田' (150)
		'Corolla' (70)
		'Camry' (50)
		'RAV4' (30)
```

## License

GNU-GPL

**Free Software, Hell Yeah!**
