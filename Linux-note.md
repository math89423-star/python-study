# Linux系统运维
## IP与端口查看
若出现服务器与本地通信不通的问题，排查过程
1. **确认云服务器是否放开了安全组**
需要检查云服务器的防火墙管理是否放开了对应的TCP和UDP端口，若开放端口为（1/65535）则代表开放全部端口，源IP（0.0.0.0/0）代表监听所有地址连接。

2. **在服务器上确保防火墙是否关闭**
```systemctl status firewalld``` 查看防火墙状态
开启时显示示例：
```python
(base) root@lavm-z7gdwyw0x9:~# systemctl status firewalld
● firewalld.service - firewalld - dynamic firewall daemon
     Loaded: loaded (/lib/systemd/system/firewalld.service; enabled; vendor preset: enabled)
     Active: active (running) since Tue 2025-11-11 10:33:37 CST; 8min ago
       Docs: man:firewalld(1)
   Main PID: 584 (firewalld)
      Tasks: 2 (limit: 4572)
     Memory: 35.6M
        CPU: 657ms
     CGroup: /system.slice/firewalld.service
             └─584 /usr/bin/python3 /usr/sbin/firewalld --nofork --nopid

Nov 11 10:33:41 lavm-z7gdwyw0x9 firewalld[584]: WARNING: COMMAND_FAILED: '/usr/sbin/ip6tables -w10 -t filter -F DOCKER->
Nov 11 10:33:41 lavm-z7gdwyw0x9 firewalld[584]: WARNING: COMMAND_FAILED: '/usr/sbin/ip6tables -w10 -t filter -X DOCKER->
Nov 11 10:33:41 lavm-z7gdwyw0x9 firewalld[584]: WARNING: COMMAND_FAILED: '/usr/sbin/ip6tables -w10 -t filter -F DOCKER->
Nov 11 10:33:41 lavm-z7gdwyw0x9 firewalld[584]: WARNING: COMMAND_FAILED: '/usr/sbin/ip6tables -w10 -t filter -X DOCKER->
Nov 11 10:33:41 lavm-z7gdwyw0x9 firewalld[584]: WARNING: COMMAND_FAILED: '/usr/sbin/ip6tables -w10 -t filter -F DOCKER->
Nov 11 10:33:41 lavm-z7gdwyw0x9 firewalld[584]: WARNING: COMMAND_FAILED: '/usr/sbin/ip6tables -w10 -t filter -X DOCKER->
Nov 11 10:33:41 lavm-z7gdwyw0x9 firewalld[584]: WARNING: COMMAND_FAILED: '/usr/sbin/ip6tables -w10 -t filter -F DOCKER->
Nov 11 10:33:41 lavm-z7gdwyw0x9 firewalld[584]: WARNING: COMMAND_FAILED: '/usr/sbin/ip6tables -w10 -t filter -X DOCKER->
Nov 11 10:33:41 lavm-z7gdwyw0x9 firewalld[584]: WARNING: COMMAND_FAILED: '/usr/sbin/ip6tables -w10 -t filter -F DOCKER->
Nov 11 10:33:41 lavm-z7gdwyw0x9 firewalld[584]: WARNING: COMMAND_FAILED: '/usr/sbin/ip6tables -w10 -t filter -X DOCKER->
lines 1-21/21 (END)
```

防火墙管理命令：
```systemctl start firewalld``` 启动防火墙
```systemctl stop firewalld```  关闭防火墙
```systemctl enable firewalld``` 启动开机自启
```systemctl disable firewalld``` 禁用开机自启

若需要在防火墙开启时，开放特定端口
```firewall-cmd --zone=public --add-port=27090/tcp --permanent``` 添加tcp的放行端口（如27090）
```firewall-cmd --zone=public --add-port=27090/udp --permanent```  添加udp的放行端口（如27090）

若需要在防火墙开启时，移除特定端口
```firewall-cmd --zone=public --remove-port=27090/tcp --permanent``` 移除tcp的放行端口（如27090）


```firewall-cmd --reload```    重载防火墙
```firewall-cmd --list-port``` 查看放行端口

3. **测试链接**
PowerShell: 
(例如测试服务器ip：223.109.141.37，port：27090)
```python
Test-NetConnection -computer 223.109.141.37 -port 27090
```
成功返回提示：
```python
ComputerName     : 223.109.141.37
RemoteAddress    : 223.109.141.37
RemotePort       : 27090
InterfaceAlias   : 以太网
SourceAddress    : 192.168.0.103
TcpTestSucceeded : True
```
Bash:
```telnet 223.109.141.37 27090```
4. **服务器状态与配置检查**
若网络连通性测试成功，需要排查是否是服务器本身配置出错
使用```PS```命令确认目标进程确实以及在服务器上运行成功，并处于正常端口监听
```ps aux | grep srcds``` 或 ```ps aux | grep 27090```
使用```netstat```命令检查端口监听状态
```netstat -tulnp | grep 27090```

## Linux系统下的文件解压与压缩
常见的压缩文件格式解压与压缩方式
| 文件后缀名 | 特点与用途 |  解压方式 | 压缩方式 |
| :-------- | :-------- | :-------- | :------ |
| .tar | 仅打包不压缩 ，用于合并多个目录或文件 | tar -xvf file.tar| tar -cvf file.tar file |
| .gz | 使用gzip压缩单个文件，压缩率与速度均衡，不保留原文件 | gunzip file.gz | gzip file |
| .tar.gz / .tgz | 先tar打包，再用gzip压缩 | tar -zxvf file.tar.gz | tar -zcvf file.tar.gz file |
| .zip | 跨平台兼容性好，在windows和linux间交换文件方便 | unzip file.zip | zip -r file.zip file|
| .xz | 使用xz工具压缩，压缩率通常最高 | unxz file.xz | xz file |
| .7z | 使用7-Zip，压缩率高，支持多种格式 | 7z x file.7z | 7z a file.7z file | 

**核心命令详解**
tar命令：
-c : 创建新的归档文件
-x : 从归档中提取文件
-v : 详细模式，处理文件时显示这些文件
**-f : 指定归档文件名。该参数后必须紧跟文件名。**
-C ： 指定解压到的目录。例如：```tar -xvf archive.tar -C /target/path```
-t : 列出归档内容，但不解压。例如：```tar -tf archive.tar```

zip命令：
压缩目录：务必使用 -r 选项递归处理，如```zip -r myzip.zip mydir```
查看压缩包内容：使用```unzip -l archive.zip```可以在解压前查看包内文件列表
解压到指定目录：使用```-d```选项，如```unzip archive.zip -d /path/to/directory/```




  