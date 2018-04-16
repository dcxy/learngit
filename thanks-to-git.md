# 感谢见过最好的 git 教程

##  一、感谢廖雪峰老师

廖老师，您好！

我最开始学编程，目前也没学会的编程语言是 JavaScript ，当时教我课程的老师从编程思想开始的。当时的时间投入少，上完课回去的作业，在 GitHub 提交作业总是卡在 PR 上，明明背下了所有 git 的命令，但是遇到报错信息，还是打开谷歌，开始查找：fatal:xxxx 。大多数查找的结果都是只言片语的解释，我像个病人一样，能用的代码敲进命令指示符，却发现就像病急的病人看见药都往嘴里塞，却还治不好。

无论是 Python、JS ，市面总能找到对应的产品，但是 git 作为开源仓库，能找到的只有一片一片没有串成网的信息。您的课程填补了这一空白，甚至，学到一半，我很好奇为什么这不是一门收费课程。之前我找到的 git 课程，要么几乎都是我已知的信息，要么就是完全看不懂，直到看懂您的教程，通篇敲完所有代码，并用 markdown 把您的文章重新排版，并存到本地以便随时检索，我才对 git 才算入门。

这是我看过最好的 git 教程，感慨于您对 git  的深入的理解，浅出的讲解，感谢您的付出，以及精湛的讲解技艺。（我自己曾经做过三年某知名培训机构的老师，无论是突出重点、气氛营造、内容详略、讲什么不讲什么，再动笔前，您花在思考架构上的时间并不会比写作本身少）

再三感谢！

##  二、更好的 git 教程

学完教程，我在敲代码的时候，一直以程序员小白的身份思考：

- 我自己能给自己讲明白吗？
- 有没有更好的理解方法？
- 有没有没讲清楚的地方？
- 教程本身还缺什么？

这是我看过最好的 git 教程，但是我希望这能变成更好的教程。通过自己给自己讲解，以及阅读教程下的评论，关于教程本身，有一些自己的想法。

当然，我这已经是鸡蛋里挑骨头了，我保留我的意见，希望给您从其他角度的入手的观点。

我看到不少留言提到，教程很好，但需要多练几遍。其实这就是教程面临的一个很尴尬的问题：**记不住！**

解决记不住，我有四条建议：

### 建议一：如果有代码注释就更帮助理解

大多数的代码都是基于英语的，而程序化的语言，就是把一些英文单词**「翻译」**过来，在程序语言中：

- `.` 可以简单翻译为中文的 ‘的’ 字
- `-` 后大多是参数，而且这个参数一般不唯一
-  `--` 后大多是文件

把一些单词简写恢复成都认识的单词，能快速记忆，譬如在**安装 git**一节中

**1.git config 的理解**

```
 git config --global user.name "Your Name"
 git config --global user.email "email@example.com"
```
理解为

```
git config --global user.name "Your Name"
// git 设置 ——面向全局 用户的姓名"你的名字"
git config --global user.email "email@example.com"
// git 设置 ——面向全局 用户的邮箱"你的邮箱"
```

**2.cd 、mkdir、pwd 的理解**

```
cd code
mkdir learngit
cd learngit
pwd
```

理解

```
cd code
// cd = change directory 切换目录切换到 code 文件夹
mkdir learngit
// mkdir = make directory 创建一个资料目录
pwd
// pwd =print work directory 打印现在资料所在目录
```
**3.cat 的理解**

```
cat readme.txt
```

理解

```
cat readme.txt
// cat = catch 打开 readme.txt
```

这里其实您可以多提一句的，对于二进制文件，`cat  <filename>`都能打开， vi 环境下都能进行编辑。

###  建议二：如果能讲清楚这样设计的好处，会更容易理解记忆

讲完**工作区和暂存区**后，您通过程序说了执行的先后顺序，但是，为什么 git 还需要工作区和暂存区，我能感觉教程中已经有表示，但没说清。

git 需要工作区和暂存区，我的理解，能做到随时有后悔药可以吃：

>**没有暂存区**
每次文件都要保存提交，仓库容量过大；
开发一个功能，做了一半上传上去，可能会让 HEAD 崩溃；
本地文件出现问题，只能回滚至上一个版本的 HEAD 。

就像手机里的单机的 RGB游戏，有暂存（缓存 index & stage ）、存档点（HEAD）。如果没有缓存，那么必须找到存档点才能退出，遇到手机断电，刚刚就白玩了。

之后再讲上传回滚在保护哪个区的数据会更容易理解。


###  建议三：更好的图片能更容易说清楚

在**版本会、回退**一节中，对 git 的描述是时光机，如果真的出现时光机，会不会更容易理解呢？

![](http://ovdtbcicu.bkt.clouddn.com/15211635847942.jpg)

在**管理修改**一节中，图形能更形象的说明，是哪些文件提交了，每个区的文件是哪个。

**章节：分区原理 -> 管理修改**

![](http://ovdtbcicu.bkt.clouddn.com/15211665766062.jpg)

第一次修改 -> git add -> 第二次修改 -> git commit

在**版本库**一节中，图形能更形象的说明，每一段代码在干什么，起什么作用。

![](http://ovdtbcicu.bkt.clouddn.com/15211650187109.jpg)
![](http://ovdtbcicu.bkt.clouddn.com/15211650272782.jpg)


###  建议四：更好的回顾方式——小测试

![](http://ovdtbcicu.bkt.clouddn.com/15211809173920.jpg)

git reset 的三个参数：hard、rest 、soft

执行 git reset 的三个参数后，剩下哪个文件？

```
git reset –soft HEAD^ 只是改变版本头指向，不改变暂存区和工作区。
git reset –mixed HEAD^ 更改指向，改变暂存区，不改变工作区。
git reset –hard HEAD^ 更改指向，该变暂存区，改变工作区。
```


参考答案

```
git reset –soft HEAD^ 只是改变版本头指向，不改变暂存区和工作区。
// 暂存区是 D、工作区是 E , 箭头指向 C
git reset –mixed HEAD^ 更改指向，改变暂存区，不改变工作区。
// 暂存区是 C、工作区是 E , 箭头指向 C
git reset –hard HEAD^ 更改指向，该变暂存区，改变工作区。
// 暂存区、工作区都是 C , 箭头指向 C
```

适宜难度的练习，在不同场景判断是哪一句代码，比机械的把您的代码敲一遍更有效（机械敲代码也是必不可少的），为了巩固您讲的 git 原理，我在 CodeSchool 完成对应的 git 练习，大多时候能使用出正确的命令，以下摘自[CodeSchool](https://www.codeschool.com/) 的 [GIT REAL](http://gitreal.codeschool.com/) 练习题。

---

#### LEVEL 4: COLLABORATION BASICS

**1.SEND CHANGES**

You've committed some work so now it's time to share! Push it out for your co-workers to see.

答案：`  git push `


**2.GET CHANGES**

Looks like your co-worker pushed some changes before you did! Your push was rejected. Retrieve the latest changes, and merge them into your branch in one step.

答案：` git pull ` 

**3.FIX CONFLICTS**

Git is reporting a conflict with your co-worker's changes in "index.html". Just discard his changes, and keep your own (the HEAD).

解决代码冲突

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Our Cat-alog</title>
  </head>
  <body>
    <nav>
      <ul>
<<<<<<< HEAD
        <li><a href="cat.html">Cats</a></li>
        <li><a href="dog.html">Dogs</a></li>
=======
        <li><a href="cat.html">Felines</a></li>
        <li><a href="dog.html">Canines</a></li>
>>>>>>> 6a487f9eb0e0a5110bdf2a45a4f5dbcc3d4eec53
      </ul>
    </nav>
  </body>
</html>
```

答案：修改为


```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Our Cat-alog</title>
  </head>
  <body>
    <nav>
      <ul>
     HEAD
        <li><a href="cat.html">Cats</a></li>
        <li><a href="dog.html">Dogs</a></li>
      </ul>
    </nav>
  </body>
</html>
```

**4.MARK FIXED**

Mark the conflict in index.html as resolved.

答案：` git add --all ` 

**5.COMMIT FIX**

Last, commit your merged changes. Don't forget to add a message so we know what the commit was about!

答案：` git commit -m 'conflict fixed' ` 

---

PS : 和您的课程相比，CodeSchool 的课程讲解太弱，读完您的教程再做题，除了熟悉命令，还能更快的了解逻辑。

最开始看到期末总结的时候，以为是一个小项目的测试，但是看到的时候，有惊喜也有一点点的失落，真希望最后能让学习 git 的我们了解到自己到底是哪里还是薄弱环节。

###  反思

嘴上简单的给您说的四点建议，做起来一点也没我说的那么简单。尤其是第三、第四条建议，需要花费的时间一点也不少，对于一个免费教程而言，做到这些是在强人所难。

但，这是我看到最好的 git 教程，我也希望它能更好！

如果您愿意，我愿意每周抽出四五个小时，试着在一个月帮您完善这些部分，如果您对教程还有其他的想法，我也希望能帮到您。

而且，我相信，有这样想法的学员不止我一个～～


##  三、来自章节上的缺憾

老师的教程基于 PC 制作，对 Mac 的问题并未提及：

## 3.1 Mac 最大的问题

.DS_Store 文件在 git merge 上的冲突

---
### 如何删除GIT中的.DS_Store

作者：iOSReverse
链接：https://www.jianshu.com/p/fdaa8be7f6c3
來源：简书

#### .DS_Store 是什么

使用 Mac 的用户可能会注意到，系统经常会自动在每个目录生成一个隐藏的 .DS_Store 文件。.DS_Store(英文全称 Desktop Services Store)是一种由苹果公司的Mac OS X操作系统所创造的隐藏文件，目的在于存贮目录的自定义属性，例如文件们的图标位置或者是背景色的选择。相当于 Windows 下的 desktop.ini。

#### 删除 .DS_Store

如果你的项目中还没有自动生成的 .DS_Store 文件，那么直接将 .DS_Store 加入到 .gitignore 文件就可以了。如果你的项目中已经存在 .DS_Store 文件，那就需要先从项目中将其删除，再将它加入到 .gitignore。如下：

删除项目中的所有.DS_Store。这会跳过不在项目中的 .DS_Store

```
find . -name .DS_Store -print0 | xargs -0 git rm -f --ignore-unmatch
// 将 .DS_Store 加入到 .gitignore
echo .DS_Store >> ~/.gitignore
//更新项目
git add --all
git commit -m '.DS_Store banished!'
```

如果你只需要删除磁盘上的 .DS_Store，可以使用下面的命令来删除当前目录及其子目录下的所有.DS_Store 文件:

`find . -name '*.DS_Store' -type f -delete`

#### 禁用或启用自动生成

禁止.DS_store生成：`defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE`

恢复.DS_store生成：
`defaults delete com.apple.desktopservices DSDontWriteNetworkStores`

参考：[在Mac系统中如何显示和隐藏文件](https://www.jianshu.com/p/a1c2495b02aa)

---

## 3.2 近似语句的区分

有些等效语句，使用的时候，它们之间的区别能好的的理解 git 本身，对比后更难出错。

---
### git 易错指南 

#### 1. Git 中 git commit -m "" 与 git commit -a -m "" 的区别 

一般仓库中的文件可能存在于这三种状态：

1）Untracked files → 文件未被跟踪；

2）Changes to be committed → 文件已缓存，这是下次提交的内容；

3）Changes bu not updated → 文件被修改，但并没有添加到缓存区。

git commit -m ""  只会提交添加到缓存区的文件（只提交添加的）

git commit -a -m ""  能提交修改过，但是没有添加到缓存区的文件（修改过的就能提交）

原文地址：http://blog.csdn.net/tyleraxin/article/details/42462311

#### 2. git reflog 与 git log

git reflog 可以查看所有分支的所有操作记录（包括commit和reset的操作），包括已经被删除的commit记录，
git log 不能察看已经删除了的commit记录

#### 3. git reset 的三个参数：hard、rest 、soft

git reset –soft HEAD^ 只是改变版本头指向，不改变暂存区和工作区。
// 暂存区是 D、工作区是 E , 箭头指向 C
git reset –mixed HEAD^ 更改指向，改变暂存区，不改变工作区。
// 暂存区是 C、工作区是 E , 箭头指向 C
git reset –hard HEAD^ 更改指向，该变暂存区，改变工作区。
// 暂存区、工作区都是 C , 箭头指向 C

#### 4.git commit --amend用法

git commit –-amend -m '覆盖原有说明'

你的代码已经提交到git库，leader审核的时候发现有个Java文件代码有点问题，于是让你修改，通常有2种方法：

方法1：leader 将你提交的所有代码 abandon掉，然后你回去 通过git reset …将代码回退到你代码提交之前的版本，然后你修改出问题的Java文件，然后 git add xx.java xxx.java -s -m “Porject : 1.修改bug…” 
最后通过 git push origin HEAD:refs/for/branches

方法2： 
leader不abandon代码，你回去之后，修改出问题的Java文件，修改好之后，git add 该出问题.java 
然后 git commit –-amend –no-edit, 
最后 git push origin HEAD:refs/for/branches。

原文地址：http://blog.csdn.net/zhujiangtaotaise/article/details/73505770

---

## 3.3 Git官方网站的资料

不知道是不是因为版权的问题，您只给了链接，没有给资料。可能因为GFW，这部分我不了解情况，但我斗胆把 Git 的官方网站的资料放到这里：

![git-cheatsheet－1](http://ovdtbcicu.bkt.clouddn.com/git-cheatsheet－1.png)

![git-cheatsheet－2](http://ovdtbcicu.bkt.clouddn.com/git-cheatsheet－2.png)



##  四、git 教程中的惊喜

真的没想到 git 教程会有段子，平时看个电影都找不到彩蛋的我，无意间看到这么多亮点：

1.在讲解**版本回滚**的时候，我看到了：「果然，我胡汉三又回来了。」以及「整个世界终于清静了！」；
2.在讲解**分支管理**的时候，我看到了：「平行宇宙的比喻」；
3.在讲解**解决冲突**的时候，我看到了：「人生不如意之事十之八九，合并分支往往也不是一帆风顺的。」；

4.在讲解**标签管理**的时候，我看到了：

```
Git有commit，为什么还要引入tag？
“请把上周一的那个版本打包发布，commit号是6a5819e...”
“一串乱七八糟的数字不好找！”

如果换一个办法：

“请把上周一的那个版本打包发布，版本号是v1.2”
“好的，按照tag v1.2查找commit就行！”
所以，tag就是一个让人容易记住的有意义的名字，它跟某个commit绑在一起。
```
5.在讲解**使用码云**的时候，我看到了：「如果我们希望体验Git飞一般的速度，可以使用国内的Git托管服务——码云」；

6.在讲解**配置别名**的时候，我看到了：「有没有经常敲错命令？比如git status？status这个单词真心不好记。」

自己上课知道面对一堆文字有多难，有了这些，不是仅仅的学会一项技能，而真的学的很开心～

7.在讲解**管理权限**的时候，我很喜欢您的态度：

```
有很多不但视源代码如生命，而且视员工为窃贼的公司，会在版本控制系统里设置一套完善的权限控制，每个人是否有读写权限会精确到每个分支甚至每个目录下。

这里我们也不介绍Gitolite了，不要把有限的生命浪费到权限斗争中。
```

8.**多人项目管理**，是之前学 git 出错最多的地方，死都死在冲突后，不会解决冲突，最后无奈删掉自己本地文件，备份资料，再利用 git pull 拉下来。

##  五、致谢

这已经不是 git 笔记了，感谢您无私的完备教程分享，感谢您课程细细的准备，您的 JavaScript 课程我也会作为后期必学内容之一。

感谢您！

赞助我给的是 99 的档，我知道，这远远不及 git 这门课的价值。我希望以后能用更多的感谢能花在购买您的付费课程上，也会一直愿意期待您做出更好的课程。

如果，您想继续完善 git 课程，或者想把这门课做的更好，我愿意继续帮您一块做！

联系方式：xiaochaogezaici@126.com

小超哥









