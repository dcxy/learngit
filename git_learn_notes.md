pandoc
======

1.  Install pandoc.   去http://pandoc.org/installing.html
    找到合适的pandoc下载文件，然后下载安装。Win7建议下载msi文件

2.  点击运行一路默认安装即可，提示成功后，win+R键调出运行框，输入cmd，打开运行窗口，输入pandoc
    \--version查看是否安装成功（如下）

    ![](media/image1.png){width="5.763888888888889in"
    height="1.8854166666666667in"}

3.  【需要先安装好git】如果是在
    unix(linux/macosx)系统下，编辑 \~/.gitconfig
    文件，如果是在windows系统下，编辑 git 安装目录下的
    /mingw64/etc/gitconfig 文件，加上这么一段话：

\[diff \"pandoc\"\]

textconv=pandoc \--to=markdown

prompt = false

\[alias\]

wdiff = diff \--word-diff=color \--unified=1

4.  在你的工程目录（git
    init的路径，如之前未新建工程目录，可以新建后使用git bash窗口
    cd到该路径后执行git init命令）下新建一个
    .gitattributes（linux/mac）文件（windows是gitattributes.txt
    文件），然后写入：

\*.docx diff=pandoc\
当然上面的是docx文件，如果是doc文件，把docx换成doc应该也是一样的。

5.   使用pandoc。对于你想要git 控制版本的文档file.docx
    在命令行(windows)或者unix下的shell，输入命令：

pandoc -s file.docx -t markdown -o file.md这个命令将你的.docx 文档转化为
.md markdown 格式。

6.  **git add file.docx file.md** (或者 git add .)

7.  git commit-m "use pandoc for change docx to md"即可。

8.  现在可以使用对待该word文件如二进制文件一样使用git进行版本控制。如下

9.  修改编辑file.docx 后提交git

10. 想要看本次修改之后与上次commit
    之间的差别，可以使用命令（file.docx是你的word文件名）：

git wdiff file.docx\
这个命令会将本次修改的与上次不同的地方用彩色标识出来。\
\
如果想查看 历次的改变（all changes），可以使用命令：

git log -p \--word-diff=color file.docx

11. 如果想回退到上个版本 可使用git reset \--hard HEAD\^

    参考网址：

    [[https://www.cnblogs.com/yezuhui/p/6853271.html]{.underline}](https://www.cnblogs.com/yezuhui/p/6853271.html)

    [[https://github.com/vigente/gerardus/wiki/Integrate-git-diffs-with-word-docx-files]{.underline}](https://github.com/vigente/gerardus/wiki/Integrate-git-diffs-with-word-docx-files)

    推荐网址-git学习 廖雪峰老师的git教程

    [[https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000]{.underline}](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)

远程
====

1.在本地目录下关联远程repository ：

git remote add origin git\@github.com:git\_username/repository\_name.git

2.取消本地目录下关联的远程库：

git remote remove origin

Your identification has been saved in /c/Users/rjkf-xyg2/.ssh/id\_rsa.

Your public key has been saved in /c/Users/rjkf-xyg2/.ssh/id\_rsa.pub.

0701yang

多人协作
========

多人协作的工作模式通常是这样：

1.  首先，可以试图用git push origin branch-name推送自己的修改；

2.  如果推送失败，则因为远程分支比你的本地更新，需要先用git
    pull试图合并；

3.  如果合并有冲突，则解决冲突，并在本地提交；

4.  没有冲突或者解决掉冲突后，再用git push origin
    branch-name推送就能成功！

5.  如果git pull提示"no tracking
    information"，则说明本地分支和远程分支的链接关系没有创建，用命令git
    branch \--set-upstream branch-name origin/branch-name。

这就是多人协作的工作模式，一旦熟悉了，就非常简单。

偷懒绝招\--设置别名
===================

[[https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/001375234012342f90be1fc4d81446c967bbdc19e7c03d3000]{.underline}](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/001375234012342f90be1fc4d81446c967bbdc19e7c03d3000)

方式一：命令行 \--global参数为是否为针对整整个用户还是本仓库

Git config alias.别名 "替代字符"如 git config \--global **alias**.ci
commit

方式二：直接修改配置文件

当前用户的Git配置文件放在用户主目录下的一个隐藏文件.gitconfig
（C:\\Users\\rjkf-xyg2\\.gitconfig ）

![](media/image2.png){width="3.6659722222222224in" height="2.28125in"}

每个仓库的Git配置文件都放在.git/config文件中
(E:\\测试学习\\learngit\\.git\\config)

![](media/image3.png){width="5.582638888888889in"
height="3.270138888888889in"}
