"----------------------------------------------------------------"
    
                    廖雪峰 Git 教程 学习笔记
    
"----------------------------------------------------------------"

"""1、Git 简介"""
    
    Linus花了两周时间自己用C写了一个分布式版本控制系统，这就是Git！一个月之内，
    Linux系统的源码已经由Git管理了！牛是怎么定义的呢？。

    Git迅速成为最流行的分布式版本控制系统，尤其是2008年，GitHub网站上线了，
    它为开源项目免费提供Git存储，无数开源项目开始迁移至GitHub，
    包括jQuery，PHP，Ruby等等。

    1、安装Git:
       
        a. 在 Linux 上安装 Git:
            
            首先，你可以试着输入git，看看系统有没有安装Git：
                $ git
                The program 'git' is currently not installed. You can install it by typing:
                sudo apt-get install git
            
            如果你碰巧用Debian或Ubuntu Linux，通过一条sudo apt-get install git就可以直接完成Git的安。
            
        b. 在Mac OS X上安装Git:
        
            如果你正在使用Mac做开发，有两种安装Git的方法。
            
            一是安装 homebrew, 然后通过homebrew安装Git，具体方法请参考homebrew的文档：http://brew.sh/。
            第二种方法更简单，也是推荐的方法，就是直接从AppStore安装Xcode，Xcode集成了Git，
            不过默认没有安装，你需要运行Xcode，选择菜单“Xcode”->“Preferences”，
            在弹出窗口中找到“Downloads”，选择“Command Line Tools”，点“Install”就可以完成安装了。       
        
        c. 在Windows上安装Git:    
            
            在Windows上使用Git，可以从Git官网直接下载安装程序,然后按默认选项安装即可。
        
        d. 安装完成后，还需要最后一步设置，在命令行输入：
        
            $ git config --global user.name "Your Name"
            $ git config --global user.email "email@example.com"
            
            因为Git是分布式版本控制系统，所以，每个机器都必须自报家门：你的名字和Email地址。
            注意 git config 命令的 --global 参数，用了这个参数，
            表示你这台机器上所有的 Git 仓库都会使用这个配置，
            当然也可以对某个仓库指定不同的用户名和Email 地址。
            
    2、创建版本库:
        
        什么是版本库呢？
            版本库又名仓库，英文名 repository, 你可以简单理解成一个目录，
            这个目录里面的所有文件都可以被 Git 管理起来，每个文件的修改、
            删除、Git 都能跟踪，以便任何时刻都可以追踪历史，或者在将来某个时刻可以“还原”。
        
        所以，创建一个版本库非常简单，首先，选择一个合适的地方，创建一个空目录：
            $ mkdir learngit
            $ cd learngit
            $ pwd
            /home/zhangkun/learngit
        
        第二步，通过 git init 命令把这个目录变成 Git 可以管理的仓库：
            $ git init
            Initialized empty Git repository in /home/zhangkun/learngit/.git/
        
            瞬间 Git 就把仓库建好了，而且告诉你是一个空仓库，在这个目录下多了一个.git目录
            这个目录是Git 来跟踪管理版本库的，没事千万不要手动修改这个目录里面的文件，
            不然改乱了，就把Git仓库给破坏了。    
            如果你没有看到.git目录，那是因为这个目录默认是隐藏的，用ls -ah命令就可以看见。
            
            $ ls -a
            . .. .git
            $ cd .git
            $ ls a
            branches  config  description  HEAD  hooks  info  objects  refs
            
        把文件添加到版本库：
        
            首先再明确一下，所有的版本控制系统，其实只能跟踪文本文件的改动，
            比如 Txt 文件，网页、所有的程序代码等等，Git 也不例外。
            版本控制系统可以告诉你每次的改动，比如在第5行加了一个单词“Linux”，在第8行删了一个单词“Windows”。    
            
            而图片、视频这些二进制文件，虽然也能由版本控制系统管理，但没法跟踪文件的变化，
            只能把二进制文件每次改动串起来，也就是只知道图片从100KB改成了120KB，
            但到底改了啥，版本控制系统不知道，也没法知道。
            
            不幸的是，Microsoft的Word格式是二进制格式，因此，版本控制系统是没法跟踪Word文件的改动的，
            真正使用版本控制系统，就要以纯文本方式编写文件。
            
            在 /home/zhangkun/learngit 目录下编写一个 readme.txt 文件，
            内容如下：
                Git is a version control system
                Git is free software
            一定要放在/home/zhangkun/learngit目录下，因为这是一个 Git 仓库，
            放到其他地方Git 找不到这个文件。
            
            第一步，用命令git add告诉Git，把文件添加到仓库：
                
                $git add readme.txt
            
                执行上面的命令，没有任何显示，这就对了，Unix的哲学是“没有消息就是好消息”，
                说明添加成功。    
                
            第二步，用命令 git commit 告诉 Git， 把文件提交到仓库：
            
                $git commit -m "wrote a readme file"
                [master (root-commit) 9f1897c] wrote a readme file
                 1 file changed, 2 insertions(+)
                 create mode 100644 readme.txt      
                
                简单解释一下git commit命令，-m后面输入的是本次提交的说明，可以输入任意内容，
                当然最好是有意义的，这样你就能从历史记录里方便地找到改动记录        
                
                git commit 命令执行成功后会告诉你：
                    1 file changed：1 个文件被改动
                    2 insertions：插入了两行内容
                
            为什么Git 添加文件需要 add, commit 一共两步呢？
            因为commit 可以一次提交多个文件，所以你可以 add 不同文件。
                $ git add file1.txt
                $ git add file2.txt file3.txt
                $ git commit -m "add 3 files."   
            
    3、小结：
        
        初始化一个Git 仓库，使用 git init 命令
        
        添加文件到Git 仓库，分两步：
            git add <file> 注意：可以多次使用，添加多个文件
            git commit -m <message>， 完成。
            
            
                            
                
            
            
            
            
            
                             
    
                       
    
    
    
    
    
    
"""2、时光机穿梭"""

"""3、"""