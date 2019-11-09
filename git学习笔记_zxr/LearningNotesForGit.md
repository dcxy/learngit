#一、简介
1.Git是Linus开发的一种分布式版本控制系统，与分布式概念相对应的是集中式，后者需要一台中央服务器，且必须联网才能工作。  
2.在本地创建`name`和`email`，注：设置为ZhouXR和8437*****@qq.com

---
#二、本地仓库
##1.创建版本库（repository），可理解为目录。
**Step 1**：新建一个目录（如`learn_git`），放到合适的位置  
**Step 2**：`cd`到该目录，用 `git init` 命令将其初始化，则空的Git仓库建好。  
**Step 3**：编写一个文本文件（如`test.txt`）（需要注意word格式为二进制，不能利用版本控制系统来跟踪，图片视频等也无法跟踪其详细变化，只能知道大小变化，故这里采用sublime来编辑）。  
**Step 4**：将文件放到`lean_git`目录下，并用命令`git add test.txt`来将其添加到Git仓库，（注：可以多次`add`不同的文件，最后一次性`commit`到仓库）  
**Step 5**：用命令`git commit -m “这里写本次提交的说明”` 告诉Git，将文件提交到仓库  
##2.修改及查看
**1)**命令`git status`：可通过它来随时掌握仓库当前的状态，会提示是否修改，是否已提交等信息。  
**2)**命令`git diff test.txt`：如果上述命令运行后提示文件被修改过，可用此命令查看对文件进行的修改详情，例如词句的增删等。
提交修改和提交新文件的流程一样，先`add`到仓库，再`commit`到仓库。
##3.版本回退
**1）**命令`git log [--pretty=oneline] [filename]`：显示[某一文件]从最近到最远的提交日志，如果嫌输出信息过于繁复。可以加上后面的参数，只查看版本号和更改说明。

**表1 命令`git log`的常用参数**

|选项   |解释说明|
|:---:|:----:|
|`-p` |按补丁格式显示每个更新之间的差异。|
|`--stat`  |显示每次更新的文件修改统计信息。|
|`--shortstat`|只显示 --stat 中最后的行数修改添加移除统计。|
|`--name-only`|仅在提交信息后显示已修改的文件清单。 |
|`--name-status`|显示新增、修改、删除的文件清单。 |
|`--abbrev-commit`|仅显示 SHA-1 的前几个字符，而非所有的 40 个字符。|
|`--relative-date`|使用较短的相对时间显示（比如，“2 weeks ago”）。|
|`--graph` |显示 ASCII 图形表示的分支合并历史。 |
|`--pretty`  |使用其他格式显示历史提交信息。可用的选项包括 `oneline`，`short`，`full`，`fuller` 和 `format`（后跟指定格式，常用格式如表2所示）。|
  
**表2  `git log –pretty=format`的常用格式**

|选项  |说明  |
|:--:|:--:|
|`%H`     |提交对象（commit）的完整哈希字串|
|`%h`     |提交对象的简短哈希字串|
|`%T`     |树对象（tree）的完整哈希字串|
|`%t`     |树对象的简短哈希字串|
|`%P`     |父对象（parent）的完整哈希字串|
|`%p`     |父对象的简短哈希字串 |
|`%an`    |作者（author）的名字|
|`%ae`    |作者的电子邮件地址|
|`%ad`    |作者修订日期（可以用 --date= 选项定制格式）|
|`%ar`    |作者修订日期，按多久以前的方式显示|
|`%cn`    |提交者（committer）的名字|
|`%ce`    |提交者的电子邮件地址|
|`%cd`    |提交日期|
|`%cr`    |提交日期，按多久以前的方式显示|
|`%s`     |提交说明|  

**2）**在Git中，用`HEAD`表示当前版本，上一个版本就是`HEAD^`，上上一个为`HEAD^^`，为方便表示，上n个版本可以记为`HEAD～n`  
命令`git reset --hard HEAD^`：表示回退到上一个版本，`hard`参数表示彻底将工作区、暂存区和版本库恢复到指定的版本。注：`--soft`参数表示仅撤销已提交的版本库内容，不会修改暂存区和工作区；`--mixed参数`表示撤销已提交的版本库内容和暂存区内容，不会修改工作区内容。  
命令`git reset --hard 3625143 [filename]`：表示[将某文件]回退到`commit id `为`3625143`的版本，不能带路径进行硬性/软性重置（`--mixed`带路径重置已弃用），若带上文件名，则需改参数为`--`。  
**3）**命令 `git reflog`：记录每一次命令，可查看命令历史，即使退回旧版本后想再找回新版本也是可行的，只要找到`commit id`即可。


##4.工作区和暂存区
**1）工作区（working directory）**：指电脑中能看到的目录，比如上面的`learn_git`文件夹。
**2）版本库（repository）**：指工作区中的隐藏目录`.git`，表示Git的版本库。版本库中存放了很多东西，其中最重要的是暂存区（`stage`或`index`）和Git自动创建的第一个分支`master`，以及指向`master`的一个指针`HEAD`。前面所说的向版本库中添加文件的操作，`add`实际上是将文件修改添加到暂存区，而`commit`就是将暂存区中的所有内容提交到当前分支。  

**区分**：  
命令`git diff test.txt`：是工作区（`work dict`）和暂存区（`stage`）之间的比较，工作区进行了修改但还未add到仓库，此时使用会提示修改了哪些内容.
命令`git diff --cached test.txt`：是暂存区（`stage`）和分支（`master`）之间的比较，`add之后`、`commit`之前使用会提示修改了哪些内容.  
命令`git diff HEAD -- test.txt`：工作区和分支之间的比较，此命令可用于查看工作区和版本库中最新版本的区别。

##5.管理修改
**1）**每次修改，如果不`add`到暂存区，那就不会加入到`commit`中。  
**2）**命令`git checkout -- test.txt`：以暂存区为蓝本，覆盖掉工作区，用来丢弃本地修改。  
**3）**命令`git reset HEAD test.txt`：清空暂存区的提交，暂存区变为和仓库中相同的版本。

**注**：`checkout`的默认值为暂存区，和`reset`的默认值为`HEAD`。因此`reset`一般用于重置暂存区（除非使用`--hard`参数，否则不会重置工作区）；而`checkout`命令主要是覆盖工作区。

##6.删除文件
**1）**命令`git rm test.txt`：将文件删除（暂存区和工作区的文件都会被删除）并用`commit`命令提交，则版本库中的文件被删除。  
**2）**若在工作区将某文件误删，则可用命令`git checkout  -- test.txt `将文件从暂存区中取出来，覆盖到工作区，即恢复到了版本库中的最新版本。  
**3）**命令 `git clean -f`可用来删除位于本地库中，但未被Git跟踪的文件，可以在删除之前使用`git clean -n `来获得删除信息，以确定是否删除该文件。

---
#三、远程仓库
##1.添加远程库
**Step1**：登陆GitHub，创建一个`new repository`（新仓库），填写仓库名称`learngit`，其他保持默认设置；  
**Step2**：GitHub提示，可以从该仓库`clone`出新仓库，也可以关联已有的本地仓库，将本地内容`push`到GitHub仓库。现在，选择后者，根据网页提示在终端输入
```
$ git remote add origin https://github.com/ZhouXiaorui1993/learngit.git
```
来添加远程库。这里使用的是`https`协议，也可以用`ssh`协议，将上述地址改为：

```$ git remote add origin git@github.com:ZhouXiaorui1993/learngit.git```

**注**：`ZhouXiaorui1993为GitHub账户名`，`origin`为远程库的名字，是Git的默认叫法，但一般无需修改，`learngit`为`repository`的名字。  
使用`ssh`协议可能会得到一个警告，此时需要将github公钥添加到信任列表，若仍出现问题则需要手动配置`ssh`秘钥，方法如下。（相比之下，`ssh`速度更快，且无需每次`push`都输入账户名和密码，推荐使用）  
###**ssh秘钥配置**  
####1）设置本地git的username和email（前面已经设置过）
```
$ git config --global user.name “ZhouXR”
$ git config --global user.email “8437×××××@qq.com”
```
####2）生成秘钥
```
$ ssh-keygen -t rsa -C “8437×××××@qq.com”
```
连续三个回车，得到两个文件：`id_rsa`和`id_rsa.pub`
####3）添加秘钥到ssh-agent
```
$ eval “$(ssh-agent -s)”
```
得到`agent pid `为xxxx，再输入以下指令
```
$ ssh -add ~/.ssh/id_rsa
```
####4）在Github中添加ssh key
登陆Github，选择`settings`→ `SSH and GPG keys`→ `add ssh key`，将`～/.ssh/id_rsa.pub`中的内容复制到框中，再点击`add`即可。

**Step3**：将本地所有内容推送至远程库。终端输入`git push -u origin master`，这里的`git push`命令实际上是将当前分支`master`推送到远程。注：由于此时远程库是空的，第一次推送时加上了`-u`参数，Git不但会将本地分支内容推送至远程，还会将本地`master`和远程`master`关联起来，在以后的推送或拉取中就可以简化命令。  
此后，只要本地做了`commit`，就可以通过命令`git push <仓库名> <分支名>`来将本地分支的最新修改推送至GitHub。  
**注意**：并不是一定要将本地所有分支都推送至远程，在项目开发过程中，其中`master`为主分支，故要时刻与远程同步；对于团队成员都需要在上面工作的开发分支，也需要与远程同步；而诸如bug修复一类的分支，只在本地使用，就无需推送到远程了。
##2.从远程库克隆(clone)
假设没有本地库，先创建一个远程库，然后从远程库克隆。  
**Step1**：登陆GitHub，创建一个新仓库，命名为`gitskills`，勾选`initialize this repository with a README`，这样GitHub会自动创建一个`README.md`文件。  

**Step2**：现在远程库已经准备完成，用命令
```
$ git clone [-o <name>] https://github.com/ZhouXiaorui1993/gitskills.git
```
克隆一个本地库，这里选项`-o`可以将克隆下来的库在本地重命名为指定`name`，若不加则默认为`origin`。此时`cd`到`gitskills`文件夹，就可以在本地看到`README.md`文件了。  
若有多人协作开发，则每人从远程克隆一份就可以了。  
 
##3.远程库的信息
**1）**命令`git remote [-v]`：不带参数时，列出所有远程库名，带有参数`-v`时，可以查看远程主机的网址。  
**2）**命令`git remote show <远程库名>`：可以查看该远程库的详细信息。  
**3）**命令`git remote add <远程库名> <网址>`：添加远程库。  
       命令 `git remote rm <远程库名>`：删除远程库。  
##3.利用远程库多人协作工作
**Step1**：从远程库`clone`文件到本地，默认情况下只能看到本地的`master`分支。如果要在其中的`dev`分支上进行开发，则用命令` git checkout -b dev origin/dev` 来创建本地的`dev`分支；  
**Step2**：修改完成后，试图使用命令`git push origin <branch name>`来推送自己的修改至远程；  
**Step3**：如果推送失败，则是由于远程分支比自己的本地更新，需要先用命令
`git pull origin <远程分支名>：<本地分支名>`取回远程该分支的更新，并与本地的指定分支合并。
若是远程分支与当前分支合并，则可省略冒号后的部分。  
**Step4**：如果合并有冲突，则手动解决冲突，并在本地提交；  
**Step5**：若没有冲突或冲突解决以后，再用`git push origin <branch name>`推送自己的修改至远程。  

**注**：若`git pull`命令提示`“no tracking information”`，则说明本地分支和远程分支之间的链接关系未创建，此时可用命令`git branch –set-upstream-to <本地分支名> origin/<远程分支名>`来建立二者的关联。  

**补充**
**1）**命令`git fetch <远程库名> [分支名]`：将远程的某个分支的更新取回本地，若不加分支名，则将远程所有分支的更新取回本地。所取回的更新，在本地要用远程库名/分支名的形式读取。  
**2）**取回远程更新后，可在其基础上，使用`git checkout -b <newbranch> <远程库名>/<分支名>`创建一个新的分支。此外，也可使用`git merge <远程库名>/<分支名>`在本地分支上合并远程分支。  
可以看出，`git pull`命令相当于`git fetch`和`git merge`两个命令的结合使用。  
---
#四、分支管理
##1.创建与合并分支
**Step1**：创建新的分支（branch），命名为`dev`，然后切换到`dev`分支，命令如下
```
$ git branch dev
$ git checkout dev
```
也可以用命令`git checkout -b dev`来代替上述两条命令，其中参数`-b`表示创建并切换。  

**注**：`master`为主分支，`HEAD`指向当前分支，`master`指向提交，新建的分支指向`master`相同的提交。  
**Step2**：可以用命令`git branch`来查看所有分支，当前分支前会有`*`标志。
补充：`git branch`命令可带选项，其中`-r`选项可用来查看远程分支；`-a`选项查看所有分支。

**Step3**：在当前分支上正常add和提交文件。
命令 `git checkout master` 可切换回maser分支，此时在`master`分支上无法看到`dev`分支上提交到的修改内容。  
**Step4**：将`dev`分支的工作成果合并到`master`分支上，先切换到`master`分支，再使用命令`git merge dev`。注：`git merge`命令是用于将指定分支合并到当前分支。  
**Step5**：合并完成后，如果不在需要dev分支，则可用命令`git branch -d dev`来删除`dev`分支。  
**注1**：若某分支未进行合并但想要将其舍弃，可以采用命令`git branch -D dev`来强行删除。
命令`git push origin :dev`可用来删除远程库中的`dev`分支。

**注2**：命令`git reflog –date=local | grep <branchname>`:查看对某一分支的操作记录，从而找出该分支的创建来源。

##2.解决冲突
若同一文件在不同分支都进行了修改并提交，则合并时可能会出现冲突（`git`会有提示），此时需要手动修改文件以消除冲突，提交后再进行合并即可（可`cat`查看文件内容以发现冲突所在位置）。
命令`git log –graph`可以看到分支合并图。
##3.分支管理策略
一般情况下，git默认合并分支为`Fast Forward`模式，此模式下，若删除原分支，则会丢失其信息。若想保留该历史信息，则可强制禁止该模式，这样合并时Git会生成一个新的`commit`。
命令```git merge --no-ff -m “新的commit描述” branch_name```可以禁止`Fast Forward`模式
##4.bug分支
当出现bug的时候，我们会通过创建新的bug分支去进行修复，修复完成后提交合并，最后删除bug分支。若此时手头工作未完成，可通过`git stash`命令来将工作现场“储藏”，然后去修复bug，修复后再利用`git stash pop`，回到工作现场。命令` git stash list`可用来查看储藏列表。

**对`git stash`命令的实验**：
**1）**现有主分支`master`，从主分支分出的子分支`dev`。现在在子分支`dev`上修改了文件`test`，由于还没完成，所以不能进行提交。  
**2）**假定此时`master`分支上的`problem`文件出现bug，则切换到`master`分支进行修复。切换过来以后，安全考虑，先用`cat`指令查看了一下`test`文件，发现刚才在子分支上的修改被带过来了。  
**3）**为避免接下来修复后提交时将该修改也一起提交，故切换回`dev`。利用`git stash`指令将这里的工作隐藏。  
**4）**再切换回`master`分支，再次用`cat`指令查看`test`文件，发现该文件不见了。证明隐藏生效，可以修复bug了。首先从`master`创建临时分支——`issue-001`，切换到这个分支上打开`problem`文件，对其进行修改后提交，再切换回`master`分支，将临时分支合并到主分支，bug解决，删除`issue-001`分支。  
**5）**为继续进行`dev`中未完成的工作，切换回`dev`分支，执行命令`git stash pop`，找回原文件。

---
#五、标签管理

##1.创建标签
为方便查找文件版本，可以对版本号打上标签，步骤如下：

**Step1**：切换到需要打标签的分支上

**Step2**：用命令`git tag [-a] <tagname> [-m] [“解释性文字”] [版本id]`新建一个标签，默认为`HAED`版本，也可以加上`commit id`指定任意版本。注：也可以加上选项`-s` ，用私钥签名一个标签（`PGP`签名），具体用法百度可查。

命令`git show <tagname>`可以看到说明文字，若加上了签名，则也可以看到签名信息

命令`git tag`可以查看所有标签

##2.操作标签
**1）**如果标签打错了，可通过命令`git tag -d <tagname>`来将其删除。因为创建的标签都只存储在本地，不会自动推送到远程。所以打错的标签可在本地安全删除。  

**2）**若要推送某个标签至远程，可使用命令`git push origin <tagname>`，或者使用命令`git push origin --tags`将所有尚未推送到远程的标签一次性推送至远程。  
**3）**对于已经推送到远程的标签，如果想要删除，则需要先用`git tag -d <tagname>`将其在本地删除，然后通过命令`git push origin :refs/tags/<tagname>`将其从远程删除。  

---
#六、使用GitHub
##1.GitHub中的一些功能解释
Gist:用于管理和发布一些没必要保存在仓库中的代码。
Popular repository:显示用户的公开仓库中受欢迎的仓库。
Contributions:显示每日用户对仓库的贡献程度。
Contibution activity:按时间顺序显示具体贡献活动的链接。
watch:相当于"订阅"，点击后，在用户的公开活动中会显示该仓库的更新。
star:相当于"收藏"，用户可以在该标记中找到被star过的仓库。
Fork:将原项目复制到了自己的仓库中，相当于在原有主分支上新建了一个分支。
code:显示该仓库中的文件列表。
issue:用于bug报告、功能添加、方向性讨论等。
pull request:代码的更改和讨论都可以在此进行。
pulse:显示该仓库最近的活动信息。
Graphs:以图表形式显示该仓库的各项指标。
commits:显示当前分支的提交历史。
branches:查看仓库的分支列表。
releases:显示仓库的tag列表。


##2.在GitHub中参与一个开源项目的步骤如下:
**Step1**:访问想要参与的项目主页，点击`Fork`则将该项目仓库复制到了自己的远程库下。注:在GitHub中，可以任意Fork开源仓库。
**Step2**:将复制得到的内容从自己的远程库中clone至本地仓库。注意:一定要从自己的账户下clone，只有这样才可以推送修改至远程，如果从作者账号clone，则没有推送修改的权限。
**Step3**:对其中的内容进行修改，工作完成后推送至自己的远程库。
**Step4**:如果希望作者接受你的修改，则可以在GitHub上发起一个pull request。如果对方接受，则修改就合并到该项目中，开源项目即得到了完善。
##








