实现爬取每日的必应壁纸图片，并设置为壁纸

运行于linux环境，依赖screen，feh，python，python-pip软件，不同发行版自行安装。

运行：
```
git clone https://github.com/Nan-sh/lybing.git
```
```
cd lybing
```
```
chmod a+x start.sh
```
```
./start.sh
```

设置壁纸：
```
./lybing.sh
```
若是要在开机完成下载并自动设置壁纸，可在开机自启文件内添加自启lybing.sh脚本

这里使用xinit自启，则在~/.xinitrc文件内添加
```
screen -dm bash -c ~/.lybing/lybing.sh
```
