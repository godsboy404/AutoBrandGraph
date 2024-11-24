# 汽车品牌知识图谱
## _初步企划——ver0.1_

此小项目是YNU-DSA-LAB-02的核心部分。

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

## 选题场景

### 消费者导向
- 选车推荐，知识普及：
- 通过知识图谱帮助用户提供品牌和车型知识的普及，筛选和比较不同品系的信息

### 企业导向
- 市场分析、售后服务优化、精准营销；
- 利用知识图谱细化用户画像，精准匹配汽车广告与用户需求

### 行业导向
- 技术创新、历史与合作研究；
- 传统能源汽车与新型能源汽车的优劣以及消费红利侧重点

Markdown is a lightweight markup language based on the formatting conventions
that people naturally use in email.
As [John Gruber] writes on the [Markdown site][df1]

> The overriding design goal for Markdown's
> formatting syntax is to make it as readable
> as possible. The idea is that a
> Markdown-formatted document should be
> publishable as-is, as plain text, without
> looking like it's been marked up with tags
> or formatting instructions.

This text you see here is *actually- written in Markdown! To get a feel
for Markdown's syntax, type some text into the left window and
watch the results in the right.

## Tech

Dillinger uses a number of open source projects to work properly:

- [AngularJS] - HTML enhanced for web apps!
- [Ace Editor] - awesome web-based text editor
- [markdown-it] - Markdown parser done right. Fast and easy to extend.
- [Twitter Bootstrap] - great UI boilerplate for modern web apps
- [node.js] - evented I/O for the backend
- [Express] - fast node.js network app framework [@tjholowaychuk]
- [Gulp] - the streaming build system
- [Breakdance](https://breakdance.github.io/breakdance/) - HTML
to Markdown converter
- [jQuery] - duh

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

## Installation

Dillinger requires [Node.js](https://nodejs.org/) v10+ to run.

Install the dependencies and devDependencies and start the server.

```sh
cd dillinger
npm i
node app
```

For production environments...

```sh
npm install --production
NODE_ENV=production node app
```

## Plugins

Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |

## Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantaneously see your updates!

Open your favorite Terminal and run these commands.

First Tab:

```sh
node app
```

Second Tab:

```sh
gulp watch
```

(optional) Third:

```sh
karma test
```

#### Building for source

For production release:

```sh
gulp build --prod
```

Generating pre-built zip archives for distribution:

```sh
gulp build dist --prod
```

## Docker

Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the
Dockerfile if necessary. When ready, simply use the Dockerfile to
build the image.

```sh
cd dillinger
docker build -t <youruser>/dillinger:${package.json.version} .
```

This will create the dillinger image and pull in the necessary dependencies.
Be sure to swap out `${package.json.version}` with the actual
version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on
your host. In this example, we simply map port 8000 of the host to
port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart=always --cap-add=SYS_ADMIN --name=dillinger <youruser>/dillinger:${package.json.version}
```

> Note: `--capt-add=SYS-ADMIN` is required for PDF rendering.

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000
```

## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
