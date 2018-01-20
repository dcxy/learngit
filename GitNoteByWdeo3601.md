## 远程仓库

#### 添加远程库

    1. 要关联一个远程库，使用命令 
     `git remote add origin git@server-name:path/repo-name.git` ；
    
    2. 关联后，使用命令 `git push -u origin master` 第一次推送master分支的所有内容；
    
    3. 此后，每次本地提交后，只要有必要，就可以使用命令 `git push origin master` 推送最新修改；

#### 从远程库克隆
    
    Git支持多种协议，包括https，但通过ssh支持的原生git协议速度最快。
    
    1. 用命令git clone克隆一个本地库 `git clone git@github.com:wdeo3601/gitskills.git` 
    

## 分支管理

#### 创建与合并分支

    1. 创建dev分支，然后切换到dev分支：git checkout -b dev 
    
    2. git checkout命令加上-b参数表示创建并切换，相当 于以下两条命令：  
        git branch dev  
        git checkout dev
        
    3. 查看当前分支(列出所有分支，当前分支前面会标一个*号)： git branch
    
    4. 切换回master分支：git checkout master
    
    5. 把dev分支的工作成果合并到master分支上：git merge dev  
        git merge命令用于合并指定分支到当前分支。
    
    6. 删除dev分支了：git branch -d dev
    
    小结
    Git鼓励大量使用分支：
    
    查看分支：git branch
    
    创建分支：git branch <name>
    
    切换分支：git checkout <name>
    
    创建+切换分支：git checkout -b <name>
    
    合并某分支到当前分支：git merge <name>
    
    删除分支：git branch -d <name>

#### 解决冲突

    1. `git status` 也可以告诉我们冲突的文件  
        Git用<<<<<<<，=======，>>>>>>>标记出不同分支的内容
    
    2. 用 `git log --graph` 命令可以看到分支合并图。
    
#### 分支管理策略

    在实际开发中，我们应该按照几个基本原则进行分支管理：
    
    首先，master分支应该是非常稳定的，也就是仅用来发布新版本，平时不能在上面干活；
    
    那在哪干活呢？干活都在dev分支上，也就是说，dev分支是不稳定的，到某个时候，比如1.0版本发布时，再把dev分支合并到master上，在master分支发布1.0版本；
    
    你和你的小伙伴们每个人都在dev分支上干活，每个人都有自己的分支，时不时地往dev分支上合并就可以了。  


    1. 强制禁用Fast forward模式合并分支 `git merge --no-ff -m "merge with no-ff" dev` 
    
#### Bug 分支

    当你接到一个修复一个代号101的bug的任务时，很自然地，你想创建一个分支issue-101来修复它，但是，等等，当前正在dev上进行的工作还没有提交，幸好，Git还提供了一个stash功能，可以把当前工作现场“储藏”起来，等以后恢复现场后继续工作
    
    1. 保存现场工作区 `git stash`
    
    2. 恢复工作现场（不自动删除）：`git stash apply` `git stash apply stash@{0}`
    
    3. 删除保存的工作现场：`git stash drop`
    
    4. 恢复的同时把stash内容也删了：`git stash pop`
    
    5. 查看保存的工作现场：`git stash list`

#### Feature 分支

    开发一个新feature，最好新建一个分支；
    
    如果要丢弃一个没有被合并过的分支，可以通过git branch -D <name>强行删除。
    
    1. 强行删除分支：`git branch -D feature-vulcan`

#### 多人协作

    1. 查看远程库的信息，用 `git remote`
    
    2. 用 `git remote -v` 显示更详细的信息
    
    3. 推送分支： `git push origin master`
    
    4. 抓取分支：`git pull`
    
    -------------------------------
    
    多人协作的工作模式通常是这样：
    
    首先，可以试图用 `git push origin branch-name` 推送自己的修改；
    
    如果推送失败，则因为远程分支比你的本地更新，需要先用 `git pull` 试图合并；
    
    如果合并有冲突，则解决冲突，并在本地提交；
    
    没有冲突或者解决掉冲突后，再用 `git push origin branch-name` 推送就能成功！
    
    如果 `git pull` 提示 `“no tracking information”`，则说明本地分支和远程分支的链接关系没有创建，用命令 `git branch --set-upstream branch-name origin/branch-name` 。
    
    这就是多人协作的工作模式，一旦熟悉了，就非常简单。
    
    --------------------------------
    
    小结
    查看远程库信息，使用 `git remote -v`；
    
    本地新建的分支如果不推送到远程，对其他人就是不可见的；
    
    从本地推送分支，使用 `git push origin branch-name`，如果推送失败，先用 `git pull` 抓取远程的新提交；
    
    在本地创建和远程分支对应的分支，使用 `git checkout -b branch-name origin/branch-name`，本地和远程分支的名称最好一致；
    
    建立本地分支和远程分支的关联，使用 `git branch --set-upstream branch-name origin/branch-name`；
    
    从远程抓取分支，使用 `git pull`，如果有冲突，要先处理冲突。

## 标签管理

#### 创建标签

    1. 命令 `git tag <name>` 用于新建一个标签，默认为HEAD，也可以指定一个commit id；
    
    2. `git tag -a <tagname> -m "blablabla..."` 可以指定标签信息；
    
    3. `git tag -s <tagname> -m "blablabla..."` 可以用PGP签名标签；

#### 操作标签

    1. 命令 `git push origin <tagname>` 可以推送一个本地标签；
    
    2. 命令 `git push origin --tags` 可以推送全部未推送过的本地标签；
    
    3. 命令 `git tag -d <tagname>` 可以删除一个本地标签；
    
    4. 命令 `git push origin :refs/tags/<tagname>` 可以删除一个远程标签。