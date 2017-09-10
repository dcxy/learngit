---
title: tool-git
date: 2017-09-06 07:40:19
tags: Git
categories: 学习
---

### 版本控制系统

集中式：(SVN，CVS)

+ 工作前都需要把最新代码从中央库 Pull 下来。工作完成然后再 Push 到中央库中，意味着必须联网。受网络限制，并且不安全

分布式：(Git，BitKeeper)

+ 每一台终端都是一个中央服务器。代码保存在本地，十分灵活。

---

### 时光穿梭

#### 工作区和暂存区

|             命令组             |                意义                 |
| :-------------------------: | :-------------------------------: |
|        git add file         |    文件添加到暂存区。可反复多次使用，添加多个文件到暂存区    |
| git commit -m "description" | `-m`后面输入的是本次提交的说明。可以一次提交多个文件到当前分支 |
|         git status          |             查看当前目录的状态             |
|          git diff           |              查看修改内容               |

---

#### 管理修改

|            命令组             |         意义         |
| :------------------------: | :----------------: |
| git log (--pretty=oneline) |     当前文件所有历史版本     |
|          cat file          |       查看文件内容       |
|         git reflog         |     查看每一次提交的id     |
| git reset --hard commit_id | 回到某一版本。HEAD 就是当前版本 |

---

#### 撤销修改

|         命令组          |                    意义                    |
| :------------------: | :--------------------------------------: |
| git checkout -- file | 丢弃工作区修改。回到最近一次`git commit`或`git add`时的状态 |
| git reset HEAD file  |                把暂存区的修改撤销掉                |

---

#### 删除文件

|     命令组     |                    意义                    |
| :---------: | :--------------------------------------: |
| git rm file | 删除文件。删除后可以借助 git checkout 恢复文件到版本库中存在的文件的最新版本 |

---

### 远程仓库

#### 添加远程仓库

|             命令组             |                意义                |
| :-------------------------: | :------------------------------: |
| git remote add origin [url] |             关联一个远程库              |
|  git push -u origin master  |        第一次推送master分支的所有内容        |
|   git push origin master    | 第一次之后每次推送最新修改。推送dev分支到远程origin分支 |

---

#### 从远程仓库克隆

|                   命令组                    |            意义            |
| :--------------------------------------: | :----------------------: |
|             git clone [url]              |    https协议克隆一个仓库。速度慢     |
| git clone git@github.com:[用户名]/[仓库名].git | `ssh`支持的原生`git`协议。克隆一个仓库 |

---

### 分支管理

#### 创建与合并分支

|          命令组           |         意义         |
| :--------------------: | :----------------: |
| git checkout -b [分支名称] |      创建加切换到分支      |
|   git branch [分支名称]    |        创建分支        |
|  git checkout [分支名称]   |       切换到分支        |
|       git branch       |        查看分支        |
|    git merge [分支名称]    |    合并指定分支到当前分支     |
|  git branch -d [分支名称]  | 删除指定分支(确保当前不在此分支上) |

---

#### 解决冲突

双方修改同一文件的不同地方不会触发。相反修改同一文件的同一地方才会触发。各自修改提交后，合并时就会出现冲突。我们切换到主分支下，对文件进行最终修改后。再进行提交即可

```txt
CONFLICT (content): Merge conflict in [文件名称]
Automatic merge failed; fix conflicts and then commit the result.
```

|       命令组       |    意义     |
| :-------------: | :-------: |
| git log --graph | 可以看到分支合并图 |

---

#### 分支管理策略

|               命令组                |                    意义                    |
| :------------------------------: | :--------------------------------------: |
| git merge --no-ff -m "描述" [分支名称] | 合并分支时，强制禁用Fast forward模式。此时Git就会在merge时生成一个新的commit。所以需要加上-m参数 |

+ 加上`--no-ff`参数就可以用普通模式合并，合并后的历史有分支，能看出来曾经做过合并，而`Fast Forward`合并看不出来曾经做过合并。

分支策略： `master`分支应该是非常稳定的，也就是仅用来发布新版本，平时不能在上面干活。干活都在`dev`分支上，也就是说，`dev`分支是不稳定的，到某个时候，比如1.0版本发布时，再把`dev`分支合并到`master`上，在`master`分支发布1.0版本。你和你的团队每个人都在`dev`分支上干活，每个人都有自己的分支，时不时地往`dev`分支上合并就可以了。所以团队合作看起来就像这样：

![](http://ww1.sinaimg.cn/large/006gmCthly1fja91noavhj30du03hjrf.jpg)

---

#### Bug 分支

当某一天你在工作时，你的Boss告诉你你之前的代码出现了bug。需要你在一个小时内改完，可是你当前在dev上进行的工作暂时还没有完成没办法提交。预计还有很久的时间，可又必须在一个小时内改完bug。该怎么办：

|             命令组             |              意义              |
| :-------------------------: | :--------------------------: |
|          git stash          | 可以把当前工作现场“储藏”起来，等以后恢复现场后继续工作 |
| git stash apply [stash@{0}] |    恢复指定的工作现场。stash 内容并不删除    |
| git stash drop [stash@{0}]  |          删除指定 stash          |
|        git stash pop        |     恢复到前一工作现场。并删除该 stash     |

**注意：**

首先确定要在哪个分支上修复 bug，假定需要在`master`分支上修复，就从`master`创建临时分支`issue-101`。修复完成后，再切换回`master`分支进行合并。最后删除`issue-101`分支。在不同分支上进行修复，工作区中看到的代码不一定是相同的，需要确保这一点。并且在不同分支上进行修复后，最后会合并到该分支上。如果代码要最终发布，你需要再将你分之上的代码`merge`到`master`分支上。

---

#### 多人协作

**注意：**

合作开发新功能时，最好在一个新的分支上进行新功能的开发，而不去污染主分支。当该功能开发好之后再去合并到主分支即可。

|          命令组           |                    意义                    |
| :--------------------: | :--------------------------------------: |
|     git remote -v      | 查看远程库的详细信息。( fetch，push 抓取和推送的`origin`的地址 ) |
| git push origin [分支名称] |           推送该分支的本地内容到远程库的分支上。            |

**注意：**

这里还有一个学问就是，并不是一定要把本地分支往远程推送，那么，哪些分支需要推送，哪些不需要呢？

+ `master`分支是主分支，因此要时刻与远程同步
+ `dev`分支是开发分支，团队所有成员都需要在上面工作，所以也需要与远程同步
  + 多人协作时，大家都会往`master`和`dev`分支上推送各自的修改。
+ `bug`分支只用于在本地修复bug，就没必要推到远程了，除非老板要看看你每周到底修复了几个bug
+ `feature`分支是否推到远程，取决于你是否和你的同班合作在上面开发

|                   命令组                    |                    意义                    |
| :--------------------------------------: | :--------------------------------------: |
| git checkout -b branch-name origin/branch-name |             在本地创建和远程分支对应的分支              |
| git branch --set-upstream branch-name origin/branch-name |              建立本地分支和远程分支的关联              |
|       git push origin branch-name        | 本地新建的分支如果不推送到远程，对其他人就是不可见的，  从本地推送分支到远程(会让你输github的用户名和密码)。 |

多人协作的工作模式通常是这样：

1. 首先从远程库clone下项目，然后在本地创建远程`origin`的`dev`分支到本地。然后就可以在`dev`分支上提交修改
2. 然后可以试图用`git push origin branch-name`推送自己的修改
3. 如果推送失败，则因为远程分支比你的本地更新，需要先用`git pull`拉取下来最新的提交，如果拉取失败则是因为远程的分支与本地的分支没有建立链接。设置好后再`git pull`进行合并
4. 如果合并有冲突，则解决冲突，并在本地提交
5. 没有冲突或者解决掉冲突后，再用`git push origin branch-name`推送就能成功

**错误：**

```
fatal: Cannot update paths and switch to branch 'dev' at the same time.
Did you intend to checkout 'origin/dev' which can not be resolved as commit?
```

**解决：**

```nginx
git remote show origin

git remote update

git fetch

git checkout -b local-name origin/remote-name
```

---

> **本文作者：** IIluosions
>
> **本文链接：** [http://www.jiyongguang.xin/2017/07/12/tool-git/](http://www.jiyongguang.xin/2017/07/12/tool-git/)
>
> **版权声明： **本博客所有文章除特别声明外，均采用 [CC BY-NC-SA 3.0 CN](https://creativecommons.org/licenses/by-nc-sa/3.0/cn/) 许可协议。转载请注明出处！