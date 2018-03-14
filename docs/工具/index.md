## Welcome to My Data Lab

# 环境配置

## 安装

1. 从 GitHub 中clone下来

2. 本地安装配置conda环境，
3. 安装mkdocs 
   1. 方法一：conda install mkdocs
   2. 方法二：pip install mkdocs
4. 本地编译md文件 mkdocs build
5. 编译并push到GitHub，mkdocs gh-deploy

## 常用链接

1. [conda](http://conda.pydata.org/)
2. [Jupyter](https://jupyter.readthedocs.org/)
3. [MkDocs](http://www.mkdocs.org/)
4. ​

## 安装
### 1. 安装mkdocs
方法一
```bash
conda update conda
conda env create --name data --clone root
source active data
pip install mkdocs

```

## 使用

### 2. 打开Jupyter

```
jupyter notebook --config config/jupyter_notebook_config.py
```

### 3. 本地编辑并上传到GitHub

```
mkdocs gh-deploy
```

