+ git add vs git commit 

前者将文件从工作区加入暂存区,后者将文件从暂存区加入版本库

+ git checkout file vs git reset file

前者将工作区中的文件改动丢弃,后者将暂存区中的文件改动丢弃,差不多和改动文件但是没有git add 一样的效果

+ git remote add origin(名字) + 地址

添加远程仓库,并将名称设为origin-也是默认名称

+ git push 远程仓库名 分支

推送本地仓库指定分支到远程仓库对应分支

+ git checkout -b branch-name(本地分支名) origin/branch-name

在本地创建和远程分支对应的分支,使用git checkout -b branch-name origin/branch-name

+ git branch --set-upstream branch-name(本地分支名) origin/branch-name

建立本地分支和远程分支的关联，使用git branch --set-upstream branch-name origin/branch-name