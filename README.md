# 汽车品牌知识图谱

## 可视化版本使用说明
> 确保文件结构如下；运行`script.py`，访问`http://127.0.0.1:5000`。
```
project/
├── script.py
├── templates/
│   └── index.html
├── bank.json
└── series.json
```

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

### 实用导向
- 因为在找数据集的时候实在是找不到现成的，包含动力系统、驱动方式、价格等的成品数据集了，所以只能用目前的简单数据集（品牌、车型），后来发现汽车之家的搜索方式也有“按品牌”的方法，而“存在即合理”，所以私以为这种搜索方式应该是有使用对象的，所以这一项小作业也算是低劣地复刻了一项不是很废な功能qwq

#### 听我~~狡辩~~解释（由LLM大神生成）
##### 解决的痛点
简化筛选过程  
对于品牌忠诚度较高的用户来说，他们只关注特定品牌的车型（如大众、本田、丰田等）。按品牌搜索可以帮助这些用户迅速找到自己感兴趣的车型，而无需在大量无关信息中浪费时间。  
品牌形象与定位选择  
汽车品牌通常具有特定的市场定位（豪华、经济实用、运动等）。用户通过按品牌搜索，能快速找到与其偏好或预算相匹配的选项，例如寻找豪华品牌（宝马、奔驰）或经济型品牌（铃木、现代）。  
缩小初始选择范围  
面对海量车型和复杂参数时，很多用户可能感到迷茫。从品牌出发搜索，可以帮助他们从广泛的市场中快速缩小选择范围，形成第一步决策。  
研究品牌全系车型  
一些用户会因为看到新款车或听说某品牌的优势而想了解该品牌的全系产品。这种情况下，“按品牌”搜索功能能满足他们的需求，让用户方便地纵览某品牌的车型布局。  
##### 适用的用户场景
品牌粉丝  
对特定品牌具有较高偏好或忠诚度的消费者，例如钟爱德系车的用户，他们可能只对宝马、大众、奥迪等品牌的车型感兴趣。  
对比同一品牌内的多款车型  
用户想比较品牌内不同级别车型的配置与价格（如丰田的卡罗拉和凯美瑞）。  
针对性探索  
想尝试某品牌新技术或新车型的用户，比如因为听说了特斯拉的新功能，想查阅该品牌所有车型。  
预算约束明确的用户  
用户可能听说某品牌主打性价比，想快速浏览它的全部车型，以匹配自身预算。  
汽车爱好者或研究者  
对特定品牌进行系统了解的需求，如查看品牌的历史和创新技术。  
##### 为什么它被低估？
搜索习惯的变化  
随着智能搜索和推荐算法的发展，许多人更习惯直接输入具体需求（如SUV、7座车、10万以内的车），而非按品牌分类浏览。  
竞争搜索方式的多样化  
“按用途搜索”或“按参数筛选”的功能通常能更高效满足多数用户的核心需求，使“按品牌”看似显得笨拙。  
对潜在用户的覆盖面有限  
并非所有用户对品牌具有清晰的偏好，一些用户可能只想解决“预算10万买什么车”或“适合家庭的7座车”等问题，而不是品牌优先。  

对于本人来说，可能父母辈会想到“买一辆二三十万的车”，而我的想法可能是“想买辆标致/捷尼赛思有哪些型号/大众的高尔夫现在怎么样了”……

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
