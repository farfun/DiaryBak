请参考ubuntu显示时间的方法：

编辑文件~/.bashrc:

```bash
export PROMPT_COMMAND="echo -n \[\$(date +%H:%M:%S)\]\ "
```


设置后显示效果如下：
```bash
[07:00:31] user@name:~$
```

