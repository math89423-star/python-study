# Docker安装
## Linux环境安装
```python
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release
# 添加GPG密钥
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
# 添加稳定版仓库
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```
## Docker常见命令
```python
docker --version  查看 Docker 版本信息，验证是否安装成功
docker info 显示 Docker 系统的详细信息，包括镜像和容器数量等
docker --help 查看所有 Docker 命令的帮助文档，是终极“备忘录”
docker pull 从仓库（如 Docker Hub）下载镜像到本地
docker images 列出本地已下载的所有镜像，查看名称、标签、大小等信息
docker build 根据 Dockerfile 文件构建自己的自定义镜像
docker rmi 删除本地的镜像，以释放磁盘空间

docker run ​创建并启动一个新容器。这是最核心的命令之一
    -d：后台运行（守护进程）
    -p 80:80：端口映射（左为宿主机，右为容器）
    --name：为容器命名
docker ps 列出容器。默认显示正在运行的容器
    -a：显示所有容器（包括已停止的）
docker stop/start/restart ​停止/启动/重启一个容器
docker exec 在正在运行的容器中执行命令。常用于进入容器内部进行调试
    -it：交互式终端
docker rm 删除已停止的容器。删除运行中的容器需加 
    -f 参数强制删除

docker logs 查看容器的日志输出，这是排查应用程序问题最直接的方式
docker cp 在容器和主机之间复制文件
    docker cp my-nginx:/path/to/file
```

## docker常见报错

### 一、网络报错
#### 错误详情
```python
(base) root@lavm-z7gdwyw0x9:/home# docker pull nginx/nginx-prometheus-exporter:1.5.1
Error response from daemon: Get "https://registry-1.docker.io/v2/": context deadline exceeded
```
### 错误原因
遇到 Docker 拉取镜像超时不用着急，这是一个非常常见的问题，尤其是在国内网络环境下。这通常与连接 Docker 官方仓库（registry-1.docker.io）的网络稳定性有关。

### 解决方案
1. ​获取加速器地址​：推荐使用阿里云镜像加速器。你需要前往 阿里云容器镜像服务控制台（https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors）获取你的专属加速器地址（需要登录），其他公共镜像源还包括中科大（USTC）、网易、百度等。
​配置 Docker​：编辑 Docker 的配置文件 /etc/docker/daemon.json（如果文件不存在，请新建）

2. 填入配置​：将以下内容写入文件（请将 https://xxxx.mirror.aliyuncs.com 替换为你从阿里云获取的实际地址）：
```python
{
  "registry-mirrors": [
    "https://xxxx.mirror.aliyuncs.com",
    "https://docker.1ms.run"
  ]
}
```

3. 重启 Docker 服务​：保存文件后，执行以下命令使配置生效。
```python
sudo systemctl daemon-reload
sudo systemctl restart docker
```
4. 验证：```docker pull hello-world```