"----------------------------------------------------------------"
    
                    廖雪峰 Git 教程 学习笔记
    
"----------------------------------------------------------------"

"""1、Git 简介"""
    
    Linus花了两周时间自己用C写了一个分布式版本控制系统，这就是Git！一个月之内，
    Linux系统的源码已经由Git管理了！牛是怎么定义的呢？。

    Git迅速成为最流行的分布式版本控制系统，尤其是2008年，GitHub网站上线了，
    它为开源项目免费提供Git存储，无数开源项目开始迁移至GitHub，
    包括jQuery，PHP，Ruby等等。

    安装Git:
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
            
                   
    
    
    
    
    
    
"""2、时光机穿梭"""

"""3、"""