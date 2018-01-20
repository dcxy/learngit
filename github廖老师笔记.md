github学习笔记

## 版本回退
HEAD指向的版本就是当前版本，因此，Git允许我们在版本的历史之间穿梭，使用命令git reset --hard commit_id。

穿梭前，用git log可以查看提交历史，以便确定要回退到哪个版本。

要重返未来，用git reflog查看命令历史，以便确定要回到未来的哪个版本。
```
git log     # 查看git commit的东西
git log --pretty=oneline # 简洁版
git reflog # 记录每一条命令
git reset --hard commitID或HEAD^^
```
* 版本号 commit ID

版本 | 版本标记
---|---
当前版本 | HEAD
上一版 | HEAD^
上100版 | HEAD～100

