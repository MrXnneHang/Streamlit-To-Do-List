[简体中文](https://github.com/MrXnneHang/Streamlit-To-Do-List/blob/main/README_zh.md) | English

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

# A To-Do-List App built with Streamlit

Created from the [ShigureLab/python-lib-starter](https://github.com/ShigureLab/python-lib-starter) template, based on [Streamlit](https://streamlit.io/).

## Introduction:

The reason for developing this app is that I often forget what I was originally supposed to do during development, requiring a long time to recall or sometimes not remembering at all. So I thought of creating a simple To-Do-List to help me record my tasks.

I categorize tasks into daily, weekly, and monthly to break down large tasks into smaller ones over time, making them easier to accomplish.

It simply supports user language switching, currently supporting Chinese and English.

![image-20250327164514385](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/25/02/202503271645755.png)
![image-20250327164638899](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/25/02/202503271646199.png)

## Deployment

### Project Management Tool: uv

[uv](https://docs.astral.sh/uv/) is the project management tool used for Streamlit-To-Do-List. You can find the appropriate installation method in the [Installation Guide](https://docs.astral.sh/uv/getting-started/installation/).

> Just ensure that `uv -v` can run properly.

### Command Execution Tool: just

[just](https://github.com/casey/just) is a simple and easy-to-use command execution tool written in Rust, allowing convenient execution of commonly used development commands. Refer to [its documentation](https://github.com/casey/just#installation) for installation methods.

> If you cannot install just, you can replace `just start` with `uv run streamlit run src/todo/__main__.py` as described below. For specific commands, refer to the justfile.

### Clone the Project

```bash
git clone https://github.com/MrXnneHang/Streamlit-To-Do-List.git
cd Streamlit-To-Do-List
```

### Start

```bash
just start
```

> Yes, just start - it's that simple!

### Access

If everything goes well, your browser should automatically open to `http://localhost:8501`, where you'll find your Streamlit-To-Do-List.

If not, you can manually access it by referring to the information output in the terminal.

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
