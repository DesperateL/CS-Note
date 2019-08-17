# Shell的变量功能

## 1. 变量的使用与设置:echo、变量设置规则、unset
### - echo
eg: 读取变量
```bash
> echo $PATH
/Users/gopher/.cargo/bin:/Library/Frameworks/Python.framework/Versions/3.7/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/go/bin:/Users/gopher/go/bin
```
eg: 设置变量
```bash
> name=leung
> echo $name
leung
> echo $(name)
leung
> echo ${name}
leung
```
**推荐${variable}形式**
### - 变量的设置规则
1. 变量与变量内容以一个等号`=`来连结，如下所示： 
`myname=VBird`

2. 等号两边不能直接接空格符，如下所示为错误： 
`myname = VBir`或 `myname=VBird Tsai`

3. 变量名称只能是英文字母与数字，但是开头字符不能是数字，如下为错误： 
`2myname=VBird`

4. 变量内容若有空格符可使用双引号`"`或单引号`'`将变量内容结合起来，但
双引号内的特殊字符如 $ 等，可以保有原本的特性，如下所示：
`var="lang is $LANG"`则`echo $var`可得`lang is en_US`
单引号内的特殊字符则仅为一般字符 (纯文本)，如下所示：
`var='lang is $LANG'`则`echo $var`可得`lang is $LANG`

5. 可用跳脱字符` \ `将特殊符号(如 [Enter], $, \, 空格符, '等)变成一般字符；

6. 在一串命令中，还需要藉由其他的命令提供的信息，可以使用反单引号\`命令\`或 `$(命令)`。特别注意，那个 \` 是键盘上方的数字键 1 左边那个按键，而不是单引号！ 例如想要取得核心版本的配置：
`version=$(uname -r)`再`echo $version`可得`2.6.18-128.el5`

7. 若该变量为扩增变量内容时，则可用 "$变量名称" 或 ${变量} 累加内容，如下所示：
`PATH="$PATH":/home/bin`

8. 若该变量需要在其他子程序运行，则需要以 export 来使变量变成环境变量：
`export PATH`

9. 通常大写字符为系统默认变量，自行配置变量可以使用小写字符，方便判断 (纯粹依照使用者兴趣与嗜好) ；

10. 取消变量的方法为使用 unset ：`unset 变量名称`例如取消 myname 的配置：
`unset myname`

### - env: 观察环境变量
范例一：列出目前的 shell 环境下的所有环境变量与其内容。
```
[root@www ~]# env
HOSTNAME=www.vbird.tsai    <== 这部主机的主机名
TERM=xterm                 <== 这个终端机使用的环境是什么类型
SHELL=/bin/bash            <== 目前这个环境下，使用的 Shell 是哪一个程序？
HISTSIZE=1000              <== 『记录命令的笔数』在 CentOS 默认可记录 1000 笔
USER=root                  <== 使用者的名称啊！
LS_COLORS=no=00:fi=00:di=00;34:ln=00;36:pi=40;33:so=00;35:bd=40;33;01:cd=40;33;01:
or=01;05;37;41:mi=01;05;37;41:ex=00;32:*.cmd=00;32:*.exe=00;32:*.com=00;32:*.btm=0
0;32:*.bat=00;32:*.sh=00;32:*.csh=00;32:*.tar=00;31:*.tgz=00;31:*.arj=00;31:*.taz=
00;31:*.lzh=00;31:*.zip=00;31:*.z=00;31:*.Z=00;31:*.gz=00;31:*.bz2=00;31:*.bz=00;3
1:*.tz=00;31:*.rpm=00;31:*.cpio=00;31:*.jpg=00;35:*.gif=00;35:*.bmp=00;35:*.xbm=00
;35:*.xpm=00;35:*.png=00;35:*.tif=00;35: <== 一些颜色显示
MAIL=/var/spool/mail/root  <== 这个用户所取用的 mailbox 位置
PATH=/sbin:/usr/sbin:/bin:/usr/bin:/usr/X11R6/bin:/usr/local/bin:/usr/local/sbin:
/root/bin                  <== 不再多讲啊！是运行文件命令搜寻路径
INPUTRC=/etc/inputrc       <== 与键盘按键功能有关。可以配置特殊按键！
PWD=/root                  <== 目前用户所在的工作目录 (利用 pwd 取出！)
LANG=en_US                 <== 这个与语系有关，底下会再介绍！
HOME=/root                 <== 这个用户的家目录啊！
_=/bin/env                 <== 上一次使用的命令的最后一个参数(或命令本身)
```
### - set:观察环境变量和自定义变量
```
[root@www ~]# set
BASH=/bin/bash           <== bash 的主程序放置路径
BASH_VERSINFO=([0]="3" [1]="2" [2]="25" [3]="1" [4]="release" 
[5]="i686-redhat-linux-gnu")      <== bash 的版本啊！
BASH_VERSION='3.2.25(1)-release'  <== 也是 bash 的版本啊！
COLORS=/etc/DIR_COLORS.xterm      <== 使用的颜色纪录文件
COLUMNS=115              <== 在目前的终端机环境下，使用的字段有几个字符长度
HISTFILE=/root/.bash_history      <== 历史命令记录的放置文件，隐藏档
HISTFILESIZE=1000        <== 存起来(与上个变量有关)的文件之命令的最大纪录笔数。
HISTSIZE=1000            <== 目前环境下，可记录的历史命令最大笔数。
HOSTTYPE=i686            <== 主机安装的软件主要类型。我们用的是 i686 兼容机器软件
IFS=$' \t\n'             <== 默认的分隔符
LINES=35                 <== 目前的终端机下的最大行数
MACHTYPE=i686-redhat-linux-gnu    <== 安装的机器类型
MAILCHECK=60             <== 与邮件有关。每 60 秒去扫瞄一次信箱有无新信！
OLDPWD=/home             <== 上个工作目录。我们可以用 cd - 来取用这个变量。
OSTYPE=linux-gnu         <== 操作系统的类型！
PPID=20025               <== 父程序的 PID (会在后续章节才介绍)
PS1='[\u@\h \W]\$ '      <== PS1 就厉害了。这个是命令提示字符，也就是我们常见的
                             [root@www ~]# 或 [dmtsai ~]$ 的配置值啦！可以更动的！
PS2='> '                 <== 如果你使用跳脱符号 (\) 第二行以后的提示字符也
name=VBird               <== 刚刚配置的自定义变量也可以被列出来喔！
$                        <== 目前这个 shell 所使用的 PID
?                        <== 刚刚运行完命令的回传值。
```
### - export: 自定义变量转化为环境变量
子程序仅会继承父程序的环境变量， 子程序不会继承父程序的自定义变量。
1. 自定义变量转化为环境变量
```bash
> export 变量名称
```
2. 显示所有环境变量
```bash
> export
ANDROID_HOME=/Users/gopher/Library/Android/sdk
ANDROID_NDK_HOME=/Users/gopher/Library/Android/sdk/android-ndk-r20
Apple_PubSub_Socket_Render=/private/tmp/com.apple.launchd.h3ChrJt9hs/Render
HOME=/Users/gopher
...(省略)
```
Q: 为啥我配的环境变量在另一个终端就没用了？为啥我重启了之后也没有用的？
A：需要把相应的变量声明写入.bashrc（你用的是zsh就写到.zshrc中） ...等开机启动的文件中，然后`source .bashrc`或者`. .bashrc`运行这个脚本来使这些配置生效。

Q:`./xxx.sh bash xxx.sh sh xxx.sh` 与`source xxx.sh`或者`. xxx.sh`有什么区别？
A：注意绝对/相对路径，bash或者sh等运行脚本，是会启动一个子线程去执行，脚本设置的变量不会传回到父进程中。`source | .`启动的脚本是直接在父进程中运行。
## 2. 变量键盘读取、数组与宣告： read, array, declare
### 1. read
read [-pt] variable
选项与参数：
- -p  ：后面可以接提示字符！
- -t  ：后面可以接等待的『秒数！』这个比较有趣～不会一直等待使用者啦！
### 2. declare / typeset
declare [-aixr] variable
选项与参数：
- -a  ：将后面名为 variable 的变量定义成为数组 (array) 类型
- -i  ：将后面名为 variable 的变量定义成为整数数字 (integer) 类型
- -x  ：用法与 export 一样，就是将后面的 variable 变成环境变量；
- -r  ：将变量配置成为 readonly 类型，该变量不可被更改内容，也不能 unset

declare +x sum  <== 将 - 变成 + 可以进行『取消』动作
declare -p sum  <== -p 可以单独列出变量的类型
### 3. 数组 (array) 变量类型 
```bash
> var[1]=aa
> var[2]=bb
> var[3]=cc
> echo "${var[1]}, ${var[2]}, ${var[3]}"
aa, bb, cc
```
**下标从1开始**
## 3. 与文件系统及程序的限制关系： ulimit
ulimit [-SHacdfltu] [配额]
选项与参数：
- -H  ：hard limit ，严格的配置，必定不能超过这个配置的数值；
- -S  ：soft limit ，警告的配置，可以超过这个配置值，但是若超过则有警告信息。
      在配置上，通常 soft 会比 hard 小，举例来说，soft 可配置为 80 而 hard 
      配置为 100，那么你可以使用到 90 (因为没有超过 100)，但介于 80~100 之间时，
      系统会有警告信息通知你！
- -a  ：后面不接任何选项与参数，可列出所有的限制额度；
- -c  ：当某些程序发生错误时，系统可能会将该程序在内存中的信息写成文件(除错用)，
      这种文件就被称为核心文件(core file)。此为限制每个核心文件的最大容量。
- -f  ：此 shell 可以创建的最大文件容量(一般可能配置为 2GB)单位为 Kbytes
- -d  ：程序可使用的最大断裂内存(segment)容量；
- -l  ：可用于锁定 (lock) 的内存量
- -t  ：可使用的最大 CPU 时间 (单位为秒)
- -u  ：单一用户可以使用的最大程序(process)数量。
## 4. 变量内容的删除、取代与替换





