git
===

简介
---

#### 下载安装
```
git config --global user.name "zhuoyan"
git config --global user.email "zhuoyan2015@outlook.com"
```
全局配置用户名和邮箱

#### 创建仓库，添加和提交
    git init
    git add <file>
    git commit -m "description"

##### 查看仓库状态和修改
    git status
    git diff

#### 版本回退
    git log
    git log --pretty=oneline
    git reset --hard HEAD^
    git reset --hard HEAD~10
    git reset --hard commitid
    git reflog

#### 工作区和暂存区
工作区
版本库里包含暂存区【stage/index】、分支、和指向分支的指针HEAD【默认是master分支】
```
git add
git commit
```

#### 管理修改
```
git commit -m "description" 
git diff HEAD -- <file>
```

#### 撤销修改
```
git checkout -- <file>
git reset HEAD <file>
git reset --hard HEAD^
git reset --hard commitid
```

#### 删除文件
```
rm <file>
git rm <file>
```

#### 远程仓库
- 创建ssh-key 并关联github
```
ssh-keygen -t rsa -C "zhuoyan2015@outlook.com"
```

- 创建github远程仓库 关联并推送到远程库
```
git remote add origin git@github.com:zhuoyan/learngit.git
git push -u origin master`
```

- SSH警告
The authenticity of host 'github.com (xx.xx.xx.xx)' can't be established.
RSA key fingerprint is xx.xx.xx.xx.xx.
Are you sure you want to continue connecting (yes/no)?
第一次使用Git的clone或者push命令连接GitHub时，会得到一个警告，输入yes即可。
Warning: Permanently added the RSA host key for IP address '52.74.223.119' to th                                  e list of known hosts.
52.74.223.119　　github.com 添加host映射即可

- 克隆远程库到本地
```
git clone git@github.com:zhuoyan/zhuoyan.github.io.git
```

#### 分支管理
- 创建与合并分支
```
git branch
git branch <name>
git checkout <name>
git checkout -b <name>
git branch -d <name>
git merge <name>
``` 
- 解决冲突
```
git add <file>
git commit -m "conflict fixed"
git log --graph --prettyoneline --abbrev-commit
```

- 分支管理策略
```
git checkout -b dev
git add misaka.txt
git commit -m "dev commit"
git checkout master
git merge --no-ff -m "merge with no-ff"
git log --graph --pretty=oneline --abbrev-commit
```
平时都应在dev分支上提交或合并，master分支仅用来发布。
带--no-ff参数的分支合并有历史信息，不带参数的FastFwor删除后就看不出合并过。

- 多人协作
```
git remote
git remote -v
git push origin master
git push origin dev
git clone git@github.com:zhuoyan/learngit.git
git branch
git checkout -b dev origin/dev
git add misaka.txt
git commit -m "others"
git push origin dev
git pull
git branch --set-upstream dev origin/dev
git branch --set-upstream-to=origin/dev  dev 
git pull
git add
git commit -m "conflict fixed"
git push origin dev
```
多人协作造成远程库分支与本地库分支冲突，
git push失败，
git pull到本地
git branch --set-upstream-to=origin/dev dev 如果git pull也失败，指定分支链接
然后合并冲突，修改提交后再推送

#### 标签管理
- 创建标签 
```
git tag <name>
git tag <name> commitid
git tag -a <name> -m "description"
git tag -s <name> -m "description"
git tag
git show <name>
```

- 操作标签
```
git tag -d <name>
git push origin <name>
git push origin --tags
git push origin :refs/tags/<name>
```
通过标签【如：v1.0】来方便查找commitid版本，标签名按字母和数字排序
创建的标签都在本地，不会自动推送。
推送到远程的标签【也要提交】
删除推送到远程的标签 先删除本地标签再推送删除标签 【远程库删除的标签 本地也须手动删除】

#### Github
fork → clone → pull request

#### 自定义Git
- 其他全局配置
```
git config --global color.ui true
```
- 忽略特殊文件
```
.gitignore文件
git add -f <file>
git check-ignore -v <file>
```
	
- 配置别名
```
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.ci commit
git config --global alias.br branch
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```
在用户根目录的.gitconfig文件中可以看到这些配置

#### [搭建git服务器](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/00137583770360579bc4b458f044ce7afed3df579123eca000)

#### 命令总结
```
clear 清屏 【cmd: cls】
pwd 当前目录
mkdir 创建目录 【cmd: mkdir或md】
rm <file> 删除文件 【cmd: del <file>】
cd 打开目录
cat <file>  在git bash查看文件内容 
ls 当前目录下的文件和目录 【cmd: dir】
ls -ah 当前目录下所有文件和目录【包含隐藏的】

git init 创建版本库
git add <file> 添加到仓库
git commit -m "description" 提交到仓库并添加说明

git status 查看仓库状态
git diff 查看文件修改内容
git diff file 查看指定文件修改内容

git log 查看提交日志
git log --pretty=oneline 查看日志美化一行
git reflog 查看提交日志 【通过日志里的id回退版本】

git reset --hard HEAD 回退版本
【HEAD表示最新版本/HEAD^上一个版本/HEAD^^上两个版本.../HEAD~100前100个版本】
【--hard选项，那么工作目录也更新，如果用--soft选项，那么都不变。】
git reset --hard commitid 回退到指定版本 【根据id自动补全查找】

git checkout -- <file> 将**工作区**的修改还原到本地版本库 
【情况A: 未添加的工作区修改，情况B: 添加到暂存区后的工作区修改，即回退到最近一次的git commit或git add时的状态】
git reset HEAD <file> 将**暂存区**的修改还原到工作区 
【HEAD表示最新版本 撤销暂存区的最后一次git add】
git rm <file> 删除文件

ssh-keygen -t rsa -C "zhuoyan2015@outlook.com" 
【在用户主目录创建ssh key 一路回车 然后添加到github的ssh key】
git remote add origin git@github.com:zhuoyan/zhuoyan/lerangit.git 
关联远程库【必须在本地git库里才能关联】
git push -u origin master 将master分支推送到远程库 -u指定默认分支后可简写为git push
git clone git@github.com:zhuoyan/zhuoyan.github.io.git 将远程库克隆到本地

git branch 查看分支
git branch <name> 创建分支
git checkout <name> 切换到分支
git checkout -b <name> 创建并切换到分支
git branch -d <name> 删除分支
git merge <name> 合并某分支到当前分支

git log --graph --prettyoneline --abbrev-commit 查看简写格式的分支合并日志
分支合并出现冲突后 先根据Git用<<<<<<<，=======，>>>>>>>标记出不同分支来修改文件
然后添加到暂存区 提交到分支 打印日志查看分支合并的结果

git merge --no-ff -m "merge with no-ff" 
不带--no-ff参数 实际是fast foward模式 即将master的指针指向dev分支 删除分支后就会丢失分支信息
带--no-ff参数 实际是在master分支上进行了一次新的提交 所以还带了-m参数和会有新的commitid 

git remote 查看远程库
git remote -v 查看远程库详细信息
git push origin master 将本地库master分支提交到远程库
git checkout -b dev origin/dev 创建远程库dev分支关联的本地库dev分支 【克隆远程库到本地一般只有默认master分支】
git push origin dev 将本地库dev分支提交到远程库
git pull 拉取到本地库 【相当于 git fetch抓取+git merge合并】
git branch --set-upstream dev origin/dev 指定本地库分支与远程库分支链接【已废弃 用下面的命令】 
git branch --set-upstream-to=origin/dev  dev 指定本地库分支与远程库分支链接

git tag <name> 创建标签 默认是HEAD
git tag <name> commitid 创建标签 可以指定commitid
git tag -a <name> -m "description" commitid 创建指定id带说明的标签
git tag -s <name> -m "description" 创建私钥签名的标签【没有gpp会报错】
git tag 查看所有标签
git show <name> 查看标签详细信息

git tag -d <name> 删除本地标签
git push origin <name> 推送本地标签 
git push origin --tags 推送本地所有未推送的标签
git push origin :refs/tags/<name> 删除远程库的标签

.gitignore文件 过滤规则  【Windows下文件另存为创建该文件】 
git add -f <file> 忽略规则强制提交
git check-ignore -v <file> 检查文件是否被规则过滤

git config --global color.ui true 配置ui颜色
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.ci commit
git config --global alias.br branch
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit" 
【究极方便的日志命令】
```

#### 其他补充
git add 把当前文件放入暂存区域。
git commit 给暂存区域生成快照并提交。
git reset 用来撤销最后一次git add files，你也可以用git reset 撤销所有暂存区域文件。
git checkout 把文件从暂存区域复制到工作目录，用来丢弃本地修改。

#### 相关链接
[廖雪峰的git教程](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)