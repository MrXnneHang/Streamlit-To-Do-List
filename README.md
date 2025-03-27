# A To-Do-List App buit with Streamlit

## 介绍：

原因是我在开发的时候通常总是忘记原本要做什么东西然后需要很长的时间去回想或者根本不记得了。所以我就想着做一个简单的 To-Do-List 来帮助我记录下我要做的事情。

重要的在于拆分。我把任务分为日常（每日），每周，每月，是为了让我把大任务在时间上分解成小任务，这样我就可以更好的去完成它。

对了，它简单地支持了双语切换，目前支持中文和英文。

![alt text](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/25/02/202503271604519.png)

![alt text](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/25/02/202503271604247.png)

## 部署

### 项目管理工具 uv

[uv](https://docs.astral.sh/uv/) 是 Streamlit-To-Do-List 用来进行项目管理的工具，你可以从[安装指南](https://docs.astral.sh/uv/getting-started/installation/)找到合适的安装方式～

> 只需要保证 uv -v 可以正常运行即可

### 命令执行工具 just

[just](https://github.com/casey/just) 是一款用 rust 编写的简单易用的命令执行工具，通过它可以方便地执行一些开发时常用的命令。安装方法请参考[它的文档](https://github.com/casey/just#installation)～

> 如果你不方便安装 just, 也可以在下文中用 `uv run streamlit run src/todo/__main__.py` 代替 `just start`, 具体命令参见 justfile 文件～

### 克隆项目

```bash
git clone https://github.com/MrXnneHang/Streamlit-To-Do-List.git
cd Streamlit-To-Do-List
```

### 启动

```bash
just start
```

> 是的，just start,非常简单～

### 访问

如果没有意外的话，你会自动跳转到浏览器并打开 `http://localhost:8501`，这就是你的 Streamlit-To-Do-List 了。

如果没有的话你也可以通过参考终端输出的信息手动访问。

```bash
(streamlib-to-do) xnne@xnne-PC:~/code/streamlit-to-do$ just start
uv lock
Resolved 46 packages in 2ms
uv sync
Resolved 46 packages in 2ms
Audited 45 packages in 0.32ms
uv run streamlit run src/todo/__main__.py

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://172.29.0.1:8501
```
