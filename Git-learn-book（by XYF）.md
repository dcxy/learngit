# Git操作笔记
## 基本操作
### 创建版本库
什么是版本库呢？版本库又名仓库，英文名repository，你可以简单理解成一个目录，这个目录里面的所有文件都可以被Git管理起来，**每个文件的修改、删除**，Git都能跟踪，以便任何时刻都可以追踪历史，或者在将来某个时刻可以“还原”。
- 创建一个learngit文件准备作为git仓库
```
$ mkdir learngit
$ cd learngit
$ pwd
//pwd命令用于显示当前目录路径
$ ls
//ls命令用于显示当前目录的文件
```	
- 将该文件夹初始化为git仓库
``` 
$ git init
```
- 添加文件进入learngit仓库
1. 将本地文件拖进该仓库文件夹
2. 
``` 
$ git add readme.txt
//将该文件添加进仓库(注意：可以反复添加，再一次性commit)
```
3.//用命令git commit告诉Git，把文件提交到仓库：
```
 $ git commit -m "wrote a readme file"
//-m后面输入的是本次提交的说明，可以输入任意内容，当然最好是有意义的，这样你就能从历史记录里方便地找到改动记录。
```
4. 补充&小结：
- **cat** 文件名 可以读取文档内容
- git status命令可以让我们时刻掌握仓库当前的状态
- git diff顾名思义就是查看difference，在后面添加文件名字后就可以看到具体修改了什么，确认修改内容后就可以commit文件了。
- 要随时掌握工作区的状态，使用git status命令。
- 如果git status告诉你有文件被修改过，用git diff可以查看修改内容。
- **git checkout – 文件名把没暂存(即没add)的干掉，或者说，丢弃工作区，回到到暂存状态 **
- git reset HEAD 文件名把暂存的状态取消，工作区内容不变，但状态变为“未暂存”。 
- **clear可以清屏**
***
### 版本回退
**git log命令显示从最近到最远的提交日志**
*想要退出git log状态，按q即可*
> 在Git中，用HEAD表示当前版本，也就是最新的提交3628164...882e1e0（注意我的提交ID和你的肯定不一样），上一个版本就是HEAD^，上上一个版本就是HEAD^^，当然往上100个版本写100个^比较容易数不过来，所以写成HEAD~100。

现在，我们要把当前版本“append GPL”回退到上一个版本“add distributed”，就可以使用**git reset**命令：
``` 
$ git reset --hard HEAD^
```

总结：

- HEAD指向的版本就是当前版本，因此，Git允许我们在版本的历史之间穿梭，使用命令git reset --hard commit_id。
- 穿梭前，用git log可以查看提交历史，以便确定要回退到哪个版本。
- 要重返未来，用**git reflog**查看命令历史，以便确定要回到未来的哪个版本。

![Alt text](./0.jpg)


## 撤销修改
### 上传到版本库后
命令**git checkout -- readme.txt**
意思就是，把readme.txt文件在工作区的修改全部撤销，这里有两种情况：

>一种是readme.txt自修改后还没有被放到暂存区，现在，撤销修改就回到和版本库一模一样的状态；
一种是readme.txt已经添加到暂存区后，又作了修改，现在，撤销修改就回到添加到暂存区后的状态。
总之，就是让这个文件回到最近一次git commit或git add时的状态。

*PS：git checkout -- file命令中的--很重要，没有--，就变成了“切换到另一个分支”的命令，我们在后面的分支管理中会再次遇到git checkout命令。*

### 上传到暂存区后
**git reset HEAD file**可以把**暂存区**的修改回退到工作区


###小结

>场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令git checkout -- file。
**场景2：**当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令git reset HEAD file，就回到了场景1，第二步按场景1操作。
场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，参考版本回退一节，不过前提是没有推送到远程库。

## 删除
###删除已经提交的文件
$ rm test.txt 可以删除该test文件
这个时候，Git知道你删除了文件，因此，工作区和版本库就不一致了，git status命令会立刻告诉你哪些文件被删除了

**现在有两个选择**
- 一是确实要从版本库中删除该文件，那就用命令git rm删掉，并且git commit
- 另一种情况是删错了，因为版本库里还有呢，所以可以很轻松地把误删的文件恢复到最新版本
**$ git checkout - - test.txt**
- **PS：git checkout其实是用版本库里的版本替换工作区的版本，无论工作区是修改还是删除，都可以“一键还原”。**



## 创建ssh key 推送github
**详见廖雪峰网站**

### 小结
小结
- 要关联一个远程库，使用命令**git remote add origin git@server-name:path/repo-name.git**；
- 如果要重新关联新的远程库，则需要先**git remote rm origin**
- 关联后，使用命令git push -u origin master第一次推送master分支的所有内容；
此后，每次本地提交后，只要有必要，就可以使用命令**git push origin master**推送最新修改；
- 分布式版本系统的最大好处之一是在本地工作完全不需要考虑远程库的存在，也就是有没有联网都可以正常工作，而SVN在没有联网的时候是拒绝干活的！当有网络的时候，再把本地提交推送一下就完成了同步，真是太方便了！

## 从远程仓库克隆
**$ git clone git@github.com:michaelliao/gitskills.git**
### 小结
>要克隆一个仓库，首先必须知道仓库的地址，然后使用git clone命令克隆。
Git支持多种协议，包括https，但通过ssh支持的原生git协议速度最快。
#



## 分支管理
### 创建分支 git branch fz1
**切换到分支**： git chenkout fz1
查看当前分支：git branch
*git branch命令会列出所有分支，当前分支前面会标一个*号。*

注意：新创建的分支，是空的。
### 合并分支   git merge fz1
git merge命令用于合并指定分支到当前分支。

>合并分支时，加上--no-ff参数就可以用普通模式合并，合并后的历史有分支，能看出来曾经做过合并，而fast forward合并就看不出来曾经做过合并。
### 删除分支 git branch -d fz1
*删除分支需要在其他分支上进行*


   
###小结
Git鼓励大量使用分支：
查看分支：git branch
创建分支：git branch name
切换分支：git checkout name
创建+切换分支：git checkout -b name
合并某分支到当前分支：git merge name
删除分支：git branch -d name

>当Git无法自动合并分支时，就必须首先解决冲突。解决冲突后，再提交，合并完成。
用git log --graph命令可以看到分支合并图。




### stash
**当手头工作没有完成时，先把工作现场git stash一下，然后去修复bug，修复后，再git stash pop，回到工作现场。**
恢复的时候，先用git stash list查看，然后恢复指定的stash，用命令：
$ git stash apply stash@{0}

### 强行删除
开发一个新feature，最好新建一个分支；
如果要丢弃一个没有被合并过的分支，可以通过git branch -D <name>强行删除。


### 多人合作
- master分支是主分支，因此要时刻与远程同步；
- dev分支是开发分支，团队所有成员都需要在上面工作，所以也需要与远程同步；
- bug分支只用于在本地修复bug，就没必要推到远程了，除非老板要看看你每周到底修复了几个bug；
- feature分支是否推到远程，取决于你是否和你的小伙伴合作在上面开发。


**多人协作的工作模式通常是这样：**
1. 首先，可以试图用git push origin branch-name推送自己的修改；
2. 如果推送失败，则因为远程分支比你的本地更新，需要先用git pull试图合并；
3. 如果合并有冲突，则解决冲突，并在本地提交；
4. 没有冲突或者解决掉冲突后，再用git push origin branch-name推送就能成功！
>如果git pull提示“no tracking information”，则说明本地分支和远程分支的链接关系没有创建，用命令git branch --set-upstream branch-name origin/branch-name。
这就是多人协作的工作模式，一旦熟悉了，就非常简单。

## 标签管理
创建标签：$ git tag v1.0

查看标签：$ git tag
>注意，标签不是按时间顺序列出，而是按字母排序的。可以用git show （tagname）查看标签信息：

删除标签：$ git tag -d v1.0
并从远程删除（如果有的话）$ git push origin :refs/tags/v1.0

推送本地标签到远程  $ git push origin v1.0
或一次性推送：$ git push origin --tags

### 小结
- 命令git tag <name>用于新建一个标签，默认为HEAD，也可以指定一个commit id；
- git tag -a <tagname> -m "blablabla..."可以指定标签信息；
- git tag -s <tagname> -m "blablabla..."可以用**PGP**签名标签；
- 命令git tag可以查看所有标签。
- 命令git push origin <tagname>可以推送一个本地标签；
- 命令git push origin --tags可以推送全部未推送过的本地标签；
- 命令git tag -d <tagname>可以删除一个本地标签；
- 命令git push origin :refs/tags/<tagname>可以删除一个远程标签。









