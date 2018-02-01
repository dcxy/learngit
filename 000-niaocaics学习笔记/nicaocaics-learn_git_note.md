# Git学习
## 首先，感谢廖老师的Git学习教程带我入门
### 基础知识
（其实不需要任何基础也可以入门，下面的基础个人觉得是会让你更加容易理解）
1. 指针：这个方便理解分支管理里的创建，删除，以及冲突及其解决策略
2. Linux的常见基础命令，如ls cd rm mkdir pwd等我个人是在Windows平台下学习的，Windows下的Git bash的使用和Linux使用差别不大
3. 其他（可能还有别的，我只意识到这俩点。。
### Git与GitHub的区别
Git是一个**软件**，是一个分布式版本控制系统

Github是一个**在线仓库**，可以自己搭或使用其他，如码云
### Git本地常用命令总结
- `git init`
    初始化一个仓库在当前路径
- `git add 文件名+后缀`
    把一个文件提交到暂存区
- `git commit -m "说明"`
    把暂存区的文件提交到当前分支
- `git status`
    查看当前Git的状态
- `git log`
    查看提交日志
- `git branch`
    查看当前Git的分支
- `git branch 分支名称`
    创建新的分支
- `git checkout 分支名称`
    选择分支，前提该分支要存在
- `git merge 分支名称`
    将该分支与当前分支合并
- `git branch -d 分支名称`
    删除该分支
- `git stash`
    将当前的工作暂存
    
    注：stash存储方式一个栈，可存储多个
- `git stash list`
    查看暂存的工作
- `git stash pop`
    恢复最近的工作并将它从暂存删除（像弹出栈顶元素）
- `git tag`
    查看当前标签
- `git tag 标签名 commmit-id`
    给指定的提交命名标签，commit-id可在日志里找到
- `git tag -d 标签名`
    删除指定标签
- 注：第一次使用会让你输入用户名和邮箱使用命令如下：

  `git config --global user.name "Your Name"`
  
  `git config --global user.email "email@example.com"`

### GitHub相关总结
1. 你要有一个Github账号
2. 查看你是否有.ssh,有则备份删除，若无输入如下指令：

    `ssh-keygen -t rsa -C "youremail@example.com"`
    
    将会生成id_isa（私钥）和id_isa.pub（公钥）
    找到公钥文件id_isa.pub，用记事本打开，全选复制粘贴，保存到Github上即可
3. 将本地与GitHub远程库关联，输入如下指令：

    `git remote add origin git@github.com:???????/learngit.git`
    
    将???????区域改成GitHub的用户名，远程库名字为origin，可以变化
    
    注：第一次使用ssh是会警告，警告内容如下：
    
    ``
    The authenticity of host 'github.com (xx.xx.xx.xx)' can't be established.
RSA key fingerprint is xx.xx.xx.xx.xx.
Are you sure you want to continue connecting (yes/no)?
    ``
    
   此时输入yes再敲击回车即可。
4. 把本地内容推送到远程
    
    第一次推送输入如下指令：
    
    `git push -u origin master`
    
    之后推送取消掉-u参数即可，指令如下：
    
    `git push origin master`
5. 从远程库克隆，输入命令

    `git clone ???`
    
    ???部分可以在GitHub的仓库上找到,即：
    
    `git@github.com:niaocaics/learn_git.git`
    (例如，这是我的)
    ![例图](https://wx4.sinaimg.cn/mw690/005I58ycly1fnzt3062xbj30gq083tc3.jpg)
    
### 其他
还有一些个人觉得比较容易，廖老师也讲得很清楚了，所以没有列出

### 最后
再次感谢廖老师的教程，欢迎大家与我交流，我的邮箱是：niaocaics@163.com