# Git 笔记
### 常用操作
`git init`   
`git status`  仓库当前状态   
`git diff` 查看修改内容   


`git add fileName`   
`git commit -m "info"`   

![](GitNote/0AA164D8-7AAE-4192-904E-7495EAF6CAD3.png)
如果add后修改，没有add直接commit会怎样？   
`git diff HEAD -- readme.txt` 会看到区别  
第一次修改 > add > 第二次修改 > add > commit   

### 恢复修改
`git checkout -- fileName`  丢弃工作区的修改，让文件回到最近一次add或commit的状态   
`git reset HEAD fileName`  把暂存区的修改丢弃，放回到工作区（完全丢弃再执行上面一条）   
`git log` 查看历史记录   
`git log —-pretty==oneline`   
`git reflog` 查看命令历史，回到未来的某个版本   
`git reset`   
git中 HEAD表示当前版本，HEAD^表示上一个版本，HEAD^^表示上上个版本，...... , HEAD~100表示往上第一百个    
`git reset --hard HEAD^`   
`git reset --hard 3628164` 回到commit_id以3628164开头的版本    

### 删除
`git rm fileName` + `git commit` 可将文件从版本库中彻底删除    
而如果是通过`rm fileName`误删的话，可以通过`git checkout -- fileName` 还原   
`git checkout` 其实是用版本库里的版本(或者暂存库)替换工作区的版本   



### 配置远程仓库
看是否存在.ssh目录    
`ssh-keygen -t rsa -C "youremail@example.com"`     
目录下id_rsa是私钥，id_rsa.puh是公钥，添加到GitHub SSH keys页面    


### 添加远程库
`git remote add origin git@github.com:Wykay-z/fileName.git`   
`git remote add origin https://github.com/Wykay-z/GitNote.git`   
`git push -u origin master`   
本地提交后就可以使用 `git push origin master` 推送最新修改   


### 从远程库克隆
`git clone git@github.com:Wykay-z/fileName.git`


### 标签管理
`git tag <name>` 创建一个标签，也可以`git tag <name> commit_id`    
`git tag -a <tagname> -m "blablabla..."`  指定添加标签信息   
`git tag` 查看所有标签，按字母排序而不是时间    
`git show <tagname>` 查看标签信息   

`git push origin <tagname>` 推送一个本地标签    
`git push origin --tags`  推送全部未推送过的本地标签    
`git tag -d <tagname>` 删除一个本地标签    
`git push origin :refs/tags/<tagname>` 先删除本地标签再执行这一句可删除远程标签    

