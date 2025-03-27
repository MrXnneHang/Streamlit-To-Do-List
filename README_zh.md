简体中文 | [English](https://github.com/MrXnneHang/Streamlit-To-Do-List/blob/main/README.md)

<p align="center">
    <a href="https://github.com/Akshay090/svg-banners">
        <img src="https://svg-banners.vercel.app/api?type=origin&text1=Streamlit-To-Do-List&text2=💖%20Open%20Source&width=800&height=200" alt="Streamlit To-Do List Banner">
    </a>
    <div align="center">
        <!-- Language & Tools -->
        <a href="https://python.org/" target="_blank"><img alt="Python" src="https://img.shields.io/badge/Python-3.11+-blue?logo=python&style=flat-square"></a>
        <a href="https://streamlit.io/"><img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white&style=flat-square"></a>
        <!-- Build Tools -->
        <a href="https://github.com/astral-sh/uv"><img alt="uv" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json&style=flat-square"></a>
         <a href="https://github.com/casey/just"><img alt="just" src="https://img.shields.io/badge/just-🤖-yellow?style=flat-square&logoWidth=20"></a>
         <!-- Code Quality -->
         <a href="https://github.com/astral-sh/ruff"><img alt="Ruff" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json&style=flat-square"></a>
         <a href="https://gitmoji.dev"><img alt="Gitmoji" src="https://img.shields.io/badge/gitmoji-😜%20😍-FFDD67?style=flat-square"></a>
    </div>
</p>

# 一个基于 Streamlit 的待办事件应用

基于 [Streamlit](https://streamlit.io/) , 从 [ShigureLab/python-lib-starter](https://github.com/ShigureLab/python-lib-starter) 模板创建的 To-Do-List 应用。

## 介绍：

原因是我在开发的时候通常总是忘记原本要做什么东西然后需要很长的时间去回想或者根本不记得了。所以我就想着做一个简单的 To-Do-List 来帮助我记录下我要做的事情。

我把任务分为日常（每日），每周，每月，是为了让我把大任务在时间上分解成小任务，这样我就可以更好的去完成它。

它简单地支持了用户语言切换，目前支持中文和英文。

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
