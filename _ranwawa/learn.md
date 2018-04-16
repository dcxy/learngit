#廖雪峰:Git教程666
##1 Git简介
###1.1 Git诞生
- 1991年 linus创造linux
- 2002年 linus手工管理社区发过来的版本更新,业务量大了之后开始用BitKeeper
- 2005年 因社区人员试图破解BitKeeper,被终止使用,linus自己写了git
- 2008年 Github上线
###1.2 集中式vs分布式
- 集中式
	- 中央服务器存储资源
	- 客户机工作时先下载
	- 工作完再上传
- 分布式
	- 每台客户机都有完整的版本库
	- 分支功能
###1.3 安装
- window安装
	- 下载:https://git-scm.com/downloads
	- 配置用户信息
		- git config --global user.name "Your Name"
		- git config --global user.name "Your Name"
- linux安装
###1.4 仓库
管理版本的仓库,又叫版本库

**创建仓库**
1. 创建一个目录
	- mkdir learngit
2. 定位到该目录
	- cd learngit
3. 将这个目录变成git仓库
	- git init

**提交文件到仓库**
- **mkdir <filename>** : 创建一个文本文件
	- mkdir readme.txt
	- 必须放在仓库目录及子目录
- **git add <filename>** : 添加文件
	- git add teadme.txt
- **git commit -m "description"**提交文件进入仓库
	- git commit -m "wrote a file"

**注意**
- git无法追踪二进制文件的更新,如:图片,视频等
- word文档也是二进制文件
- 记事本的默认行为容易导致错误

##2 本地仓库
###2.1 时光穿梭机
- **git status [filename]** :  查询仓库当前状况
	- Changes not staged for commit
	- Changes to be commited
	- nothing to commit,working tree clean
- **git reset [filename]** : 撤消当前提交
	- Unstaged changes after reset
- **git diff [filename]** : 查询变更详情
###2.2 版本回退
- **git log** : 查看提交历史
	- HEAD 当前版本
	- git log --pretty=oneline 简化显示
	- 左边的那一串 版本ID
- **git reset --hard HEAD~[number]** : 回退到向前第几个历史版本
- **git reset --hard &lt;ID>** :  回退到指定的历史版本
	- ID可以只是前面几个数字
	- 在命令行窗口还没关闭之前,可以恢复到最新版本
- **git reflog** : 纪录每次的版本操作
	- 当关机后想要恢复新版本,可在这里查看

**原理**
- HEAD指针指向当前版本
- 回退时,只是更换了指针指向的位置而已
- 然后更改了工作区的文件
###2.3 暂存区
- **工作区** : learngit文件夹
- **版本库** : .git文件夹
	- **暂存区** : git add的文件就是放暂存区里面的
	- **分支** : git commit就是把暂存区的文件放进分支
		- 初始加载时,默认创建一个master分支
![](https://cdn.liaoxuefeng.com/cdn/files/attachments/001384907720458e56751df1c474485b697575073c40ae9000/0)
###2.4 管理修改
1. 修改文件
2. git add
3. 修改文件
4. git commit
	- **只会同步第1次修改**
	- 待处理问题:我这里无法同步第1次修改,会报错
###2.5 撤销修改
- **git checkout -- filename** : 撤消修改
	- --不能少，否则会切换到另外一个分支
	-  在add或78commit后修改的内容会被撤消
- **git reset HEAD filename** :  撤消暂存区缓存
	- add到暂存区的内容,可以撤回到工作区
###2.6 删除文件
1. 创建test.txt
2. 将test.txt提交到版本库中
2. 从工作区删除test.txt
	- 如果要删除文件
		- git rm test.txt
		- git commit -m "remove test.txt"
	- 如果要恢复test.txt
		- git checkout -- test.txt
		- 实际上checkout的原理是从分支中恢复文件到工作区
##3 远程仓库
###3.1 配置github
由于本地和github是SSH加密通信，所以要先配置一下加密钥。
1. **ssh-keygen -t rsa -C "274544338@qq.com"** : 生成密钥对
	- id_rsa:私钥
	- id_rsa.pub:公钥
2. 进入github帐户设置
	- 添加SSH密钥
	- 粘贴公钥里面的文本
###3.2 连接远程仓库
**提交到远程仓库**
1. 创建github仓库
2. 连接github
	- git remote add origin https://github.com/ranwawa/learngit
3. 提交到远程仓库
	- git push -u origin master
		- -u第一次时使用,将远程和本地的master关联起来
		- 后续只用git push origin master即可

**从远程仓库克隆**
1. 复制远程仓库链接
2. 从远程仓库复制
	- git clone https://github.com/ranwawa/hello-world
##4 分支管理
把当前master分支复制成另外一个分支
###4.1 创建与合并分支
**分支原理**
- 原始状态
	- HEAD指向master分支的最近一次提交指针
-修改分支
	- master分支的指针向前移动
- 创建分支时dev
	- 多了一个分支指针dev
	- HEAD指向新分支的最近一次提交
- 修改分支
	- dev的指针向前移动
- 合并分支
	- master指针移动到dev最近一次提交指针
	- 删除dev指针
	- HEAD指向master指针

**创建分支**
1. **git branch** : 查看所有分支
2. **git branch [name]** : 创建分支
3. **git checkout [name]** : 跳转到指定分支
	- git checkout -b <name> 创建并跳转到指定分支.2,3步的简写
4. 在分支上进行更新
5. **git merge [name]** : 合并分支
6. **git branch -d [name]** : 删除分支

**注意**
- 因为分支的快捷和安全性
- 官方建议一直在分支上工作
- 然后进行合并再删除
###4.2 解决冲突
- 当同时存在两个分支时
- 每个分支上的同一文件同一位置都进行修改
- 合并时会报错,并自动修改该文件内容
- 手动修复后
- 再add commit一次即可
- **git log --graph --pretty=oneline** : 查看分支合并情况
###4.3 分支管理策略
**分支合并原理**
- Fast Forward 模式
	- 普通情况下,默认是这种模式
	- 删除分支后
	- 分支信息完全销毁
- no-ff 模式
	- 合并时会生成一个新的commit
	- 删除分支后,历史仍然存在
待处理问题:还是没有完全明白这两者的区别......
**分支策略**
- master是非常稳定的, 只用来发布新版本,不用来干活
- 平时都在dev上干活
- 团队成员都拷贝dev,向dev上合并
###4.4 Bug分支
- 当前正在一个分支dev上开发
- 又接到另外一个bug任务
- 这时需要开一个bug分支来修复
- 因为同一台电脑上的分支共享暂存区
- 所以开bug分支会把dev上的内容也带过来
- 这样在提交bug的时候就会把未完成的dev也提交上去
- 所以要先隐藏dev再开bug然后合并 

**步骤**
1. **git stash** : 隐藏分支
2. 创建bug分支并跳转
3. 进行修改并提交
4. 跳到master分支并合并
5. 删除bug分支并跳转到dev分支
6. **git stash list** : 查看所有隐藏分支
7. **git stash apply stash@{0}** : 恢复指定分支
8. **git stash drop ** : 删除指定隐藏分支
	- git stash pop : 恢复并删除隐藏分支
###4.5 Feature分支
- 当前正在一个分支dev上开发
- 接到一个新功能的任务
- 需要再开一个分支单独处理这个新任务
- 此时任务已经提交但没有合并
- 但是这个任务现在不需要了
- 普通方式无法删除
- **git branch -D feature**

**注意**
- 开发新功能都要开一个新分支来办
- 没有合并的分支,强行删除后无法恢复
###4.6 多人协作
- **git remote** : 查看远程仓库信息
	- git remote -v : 查看详细信息
- **git push origin name** : 推送到远程指定分支

**哪些分支需要推送到远程**
- master是主分支,需要时刻同步
- dev是开发分支,需要时刻同步
- bug分支用于本地修复,不用同步
- feature分支,如果和小伙伴同时开发,则需要同步

**抓取分支**
1. 创建和远程仓库的连接
	- git remote add origin https://github.com/ranwawa/learngit
2. 克隆远程仓库
	- git clone https://github.com/ranwawa/learngit
3. 创建开发分支并关联远程分支
	- git checkout -b dev origin/dev
4. 修改并commit
5. 推送到远程仓库
	- git push origin dev

**分支冲突**
- 当两个不同的伙伴
- 同时编辑了一个文件
- 推送到同一个远程分支上时会报错

1. 建立与远程分支的连接
	- git branch --set-upstream-to origin.dev
2. 拉取远程分支更新
	- git pull
3. 修改冲突并提交
4. 推送
	- git push origin/dev
##5 标签管理
- 将标签和某个commit绑定到一起
- 相当于是commitID的别名
- 实质上是一个静态的指针
- 指向那个commit

###5.1 创建标签
1. **git tag** : 查看当前所有标签
2. **git tag v2.1.2** : 给当前HEAD打一个标签
	- git tag v0.0.2 coummitIdName 在指定commitId上打个标签
3. **git show v0.0.1** : 显示标签详细信息
	- git tag 并不是按时间排列的
###5.2 操作标签
- **git push origin v1.0** : 推送标签到远程仓库
	- **git push origin tags** : 摄像头所有标签
- **git tag -d v0.0.1** : 删除标签
- **git push origin :refs/tags/v0.9** : 删除远程标签
