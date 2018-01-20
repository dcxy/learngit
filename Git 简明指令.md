
1. 丢弃工作区修改: `git checkout -- file`
- `git checkout` 其实是用版本库里的版本替换工作区的版本，无论工作区是修改还是删除，都可以“一键还原”
2. 丢弃暂存区修改: `git reset HEAD file`
3. 版本回退 (未推送到远程库): `git reset --hard commit_id`
4. 查看提交历史: `git log`
5. 查看命令历史: `git reflog`

---

6. 查看当前分支: `git branch`
7. 创建分支: `git branch <name>`
8. 切换到分支: `git checkout <name>`
9. 创建 + 切换到分支: `git checkout -b <name>`
10. 合并指定分支到当前分支 (如: 当前在 master, 合并 dev): `git merge dev`
11. 普通合并: `git merge --no-ff <name>`
- 加上 `--no-ff`合并后的历史有分支，`fast forward`合并后看不出来做过合并
12. 删除分支: `git branch -d <name>`
- 强行删除: `git branch -D <name>`
13. 查看分支合并图 (可带参数): `git log --graph[ --pretty=oneline --abbrev-commit]`

---

14. 修复 bug 时临时储存工作区未增加、提交内容: `git stash`
15. 恢复 stash 并删除: `git stash pop`
16. 查看临时储存的内容: `git stash list`
17. 恢复临时储存但不删除 stash: `git stash apply`
- 多次 stash 恢复: `git stash apply stash@{序号}`，序号通过 `git stash list` 查看
18. 删除 stash: `git stash drop`

---

19. 查看远程库信息: `git remote -v`
20. 从本地推送分支: `git push origin <branch-name>`，如果推送失败，先用 `git pull` 抓取远程更新提交
21. 在本地创建和远程分支对应的分支: `git checkout -b <branch-name> origin/<branch-name>`
22. 建立本地分支和远程分支的关联: `git branch --set-upstream <branch-name> origin/<branch-name>`

---

23. 新建标签: `git tag <name>`
- 可在后面指定一个 commit id, 通过 `git log --pretty=oneline --abbrev-commit` 查看 commit id
24. 指定标签信息: `git tag -a <tagname> -m "blablabla..."`
25. 用PGP签名标签: `git tag -s <tagname> -m "blablabla..."`
26. 查看所有标签: `git tag`
27. 查看标签说明: `git show <tagname>`
28. 推送一个本地标签: `git push origin <tagname>`
29. 推送全部未推送过的本地标签: `git push origin --tags`
30. 删除一个本地标签: `git tag -d <tagname>`
31. 删除一个远程标签: `git push origin :refs/tags/<tagname>`
