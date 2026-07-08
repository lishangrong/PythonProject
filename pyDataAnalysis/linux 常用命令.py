"""
命令名 --help   看选项参数
man 命令名      查看命令使用方式与作用

pwd： 当前路径
ls: 罗列当前文件
ls -a : 显示所有包含隐藏
ls -l 简写 ll:   以行的方式展示

切换目录 cd
cd ~ 表示使用者的home目录
cd . 表示目前所在目录
cd .. 表示目前目录为止的上一层目录
文件系统相关命令：
mkdir：用于创建目录
    -p 确保父目录名称存在，不存在的就建一个
rm：用于删除一个文件或者目录
    -f 强制直接删除，无需用户确认
    -r 将目录及以下的所有递归逐一删除
    -rf
touch：用于创建文件
cp(copy file)：用于复制文件
cp 文件名称 目标目录
cp -R 文件夹 目标文件夹
mv(move file):用来为文件或者目录改名，或者将文件、目录移入其他位置
mv 1.txt abc.txt

cat：用于链接文件并打印到标准输出设备如console控制台上。适合小文件内容查看
more：以一页一页的形式显示，更方便使用者逐页阅读，翻页结束自动退出.
    按space键翻下一页，按b往回(back)上一页
less: 随意浏览文件，支持翻页和搜索。
    按space键翻下一页，按enter键翻下一行
    按b向上翻一页
    按q退出
head：用于查看文件的开头部分
tail：用于查看文件的结尾部分
    -n 用于显示行数   tail -n 3 abc.txt   (后3行)
                    tail -3 abc.txt   (后三行)
    -f 用于实时显示文件动态  tail -5f abc.txt  (后5行)

echo：用于字符串的输出
echo高级用法： 输出到文件  echo "Log entry" >> log.txt
    > 会覆盖文件，>> 会追加内容


查找：
find 路径 -选项 参数
        -size
        -name
find 路径 -size +100M
find 路径 -name 'abc'
grep：过滤命令
    ps -ef | grep ssh
which：查找linux命令所在目录
    which linux命令名

ln-s: 软链接
ln：硬链接

tar 压缩
tar -zcvf 压缩包名.tar.gz 要被压缩的文件
解压缩
tar -zxvf 压缩包名.tar.gz -C 解压到的路径

history：查看历史命令
tab：自动补齐
ctrl + a 把光标移动到命令开头位置
ctrl + e 把光标移动到命令结尾位置
ctrl + u 清空光标之前的所有命令

vi/vim 编辑器
vim 1.txt  进入文件
输入 i： 输入模式---编辑文件
esc键：输入模式切换至命令模式
：底线命令模式
:wq 保存退出
:wq! 强制保存退出
:q 退出不保存
:q! 强制退出不保存
方向键控制移动
命令 hjkl 移动
翻页 pageup pagedown
行首(home 0) 行尾(end $)
跳到文件的第一行：gg
跳到维尔纳见得最后一行：G
yy:复制当前行
nyy：连续向下复制n行
dd 删除当前行
ndd 向下连续删除n行
p 粘贴
shift + z + z：  保存退出
/内容： 查找文本
u 撤销
ctrl + r 反撤销
i：在当前位置插入
o：向下插入一行
:set nu 设置行号
:set nonu 取消行号设置
:noh / :nohl 取消高亮
:%s/就内容/新内容/gc
:行号(n) 跳转至指定行
"""