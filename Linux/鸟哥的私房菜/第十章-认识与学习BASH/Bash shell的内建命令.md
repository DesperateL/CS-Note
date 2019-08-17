# Bash shell 的内建命令

## **type 查看命令执行**
```bash
[root@www ~]# type [-tpa] name
选项与参数：
    ：不加任何选项与参数时，type 会显示出 name 是外部命令还是 bash 内建命令
-t  ：当加入 -t 参数时，type 会将 name 以底下这些字眼显示出他的意义：
      file    ：表示为外部命令；
      alias   ：表示该命令为命令别名所配置的名称；
      builtin ：表示该命令为 bash 内建的命令功能；
-p  ：如果后面接的 name 为外部命令时，才会显示完整文件名；
-a  ：会由 PATH 变量定义的路径中，将所有含 name 的命令都列出来，包含 alias

范例一：查询一下 ls 这个命令是否为 bash 内建？
[root@www ~]# type ls
ls is aliased to `ls --color=tty' <==未加任何参数，列出 ls 的最主要使用情况
[root@www ~]# type -t ls
alias                             <==仅列出 ls 运行时的依据
[root@www ~]# type -a ls
ls is aliased to `ls --color=tty' <==最先使用 aliase
ls is /bin/ls                     <==还有找到外部命令在 /bin/ls

范例二：那么 cd 呢？
[root@www ~]# type cd
cd is a shell builtin             <==看到了吗？ cd 是 shell 内建命令
```
## **命令的换行**
```bash
范例：如果命令串太长的话，如何使用两行来输出？
[vbird@www ~]# cp /var/spool/mail/root /etc/crontab \
> /etc/fstab /root
```
`\`转义`Enter`,让`Enter`不再具有运行命令的功能。

## **alias unalias 命令别名与取消命令别名**
```bash
[root@www ~]# alias lm='ls -al | more'
[root@www ~]# unalias lm
[root@www ~]# alias                 //列出所有别名
alias cp='cp -i'
alias l.='ls -d .* --color=tty'
alias ll='ls -l --color=tty'
alias lm='ls -l | more'
alias ls='ls --color=tty'
alias mv='mv -i'
alias rm='rm -i'
alias which='alias | /usr/bin/which --tty-only --show-dot --show-tilde'
```
## **history 历史命令**
```bash
[root@www ~]# history [n]
[root@www ~]# history [-c]
[root@www ~]# history [-raw] histfiles
选项与参数：
    ：列出目前内存内的所有 history 记忆
n   ：数字，意思是『要列出最近的 n 笔命令行表』的意思！
-c  ：将目前的 shell 中的所有 history 内容全部消除
-a  ：将目前新增的 history 命令新增入 histfiles 中，若没有加 histfiles ，
      则默认写入 ~/.bash_history
-r  ：将 histfiles 的内容读到目前这个 shell 的 history 记忆中；
-w  ：将目前的 history 记忆内容写入 histfiles 中！
```
$HISTSIZE : 系统记录的最大历史命令数
～/.bash_history 文件记录历史命令

### **`!`命令**
```bash
[root@www ~]# !number
[root@www ~]# !command
[root@www ~]# !!
选项与参数：
number  ：运行第几笔命令的意思；
command ：由最近的命令向前搜寻『命令串开头为 command』的那个命令，并运行；
!!      ：就是运行上一个命令(相当于按↑按键后，按 Enter)

[root@www ~]# history
   66  man rm
   67  alias
   68  man history
   69  history 
[root@www ~]# !66  <==运行第 66 笔命令
[root@www ~]# !!   <==运行上一个命令，本例中亦即 !66 
[root@www ~]# !al  <==运行最近以 al 为开头的命令(上头列出的第 67 个)
```

