## Welcome to My Data Lab

# 随笔

记录日常学习的一些笔记，包括转载、复制等。





# 安装

1. 从 GitHub 中clone下来
2. 本地安装配置conda环境，
3. 安装mkdocs 
   1. 方法一：conda install mkdocs
   2. 方法二：pip install mkdocs
4. 本地编译md文件 mkdocs build
5. 编译并push到GitHub，mkdocs gh-deploy

# 常用链接

1. [conda](http://conda.pydata.org/)
2. [Jupyter](https://jupyter.readthedocs.org/)
3. [MkDocs](http://www.mkdocs.org/)
4. ​

### 1. Setup Env

```bash
conda update conda
conda env create --name data --clone root
source active data
pip install mkdocs
```

### 2. Start Jupyter

```
jupyter notebook --config config/jupyter_notebook_config.py
```

### 3. Deploy to GitHub Pages

```
mkdocs gh-deploy --clean
```

