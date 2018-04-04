# 基础命令
|命令|释义|
|:--|:--
|conda update --all|升级所有的环境依赖包
|conda update conda|更新Anconda

# 解决Anaconda闪退问题
> 升级navigator：`conda update anaconda-naviagtor`,确认升级信息后即可

如果任然不行，可执行后续步骤：
1. 重置navigatior，执行：`anaconda-navigator --reset`
2. 升级客户端，执行：`conda update anaconda-client`
3. 升级安装依赖包，执行：`conda update -f anaconda-client`