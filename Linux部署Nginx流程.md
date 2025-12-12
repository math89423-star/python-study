## Nginx的核心功能与价值
Nginx是一款轻量级、高性能的HTTP服务器与反向代理服务器，也是当前企业级Web服务中最常用的组件之一。它的核心作用可以概括为四大类：
1. **静态服务**：直接搭建静态网页服务（如官网、产品文档、前端打包后的单页应用），支持高效处理静态资源（HTML\CSS\JS\图片等）。
2. **反向代理**：作为客户端与后端服务的“中间层”，转发请求至后端API或应用服务器如（TomCat、Node.js），隐藏真实服务地址，提升安全性。
3. **负载均衡**：面对高并发场景时，将请求均匀分发到多台后端极其，避免单点服务器过载，保障稳定性。
4. **SSL终端**：统一处理HTTPS加密解密，管理SSL证书，无需向后端服务单独配置HTTPS，简化整体架构。

| 特征 | 正向代理（Forward Proxy）| 反向代理（Reverse Proxy）|
| :---- | :--------------------- | :---------------------- |
| 代理对象 | 代理**客户端** | 代理**服务器端** |
| 配置位置 | 客户端需要显示配置代理服务器地址 | 对客户端透明，客户端无感知|
| 主要用途 | 突破访问限制、缓存加速、内容过滤 | 负载均衡、暴露单一入口、安全防护、SSL卸载 |
| 隐藏对象 | 隐藏**客户端**身份 | 隐藏**真实服务器**身份 |

正向代理：正向代理充当客户端的“代言人”，代表其访问外部资源。
反向代理：反向代理是服务端的“调度中心”，客户端请求发送到反向代理，由它转发到内网的后端服务器。

## Nginx部署流程
1. 查看Nginx镜像
在Docker Hub上找到最新的Nginx镜像查看。
Docker Hub地址：hub.docker.com/_/nginx

2. 拉取Nginx镜像
通过docker pull指令拉取。
```docker pull nginx:1.29.3```

3. docker部署Nginx镜像
通过docker run命令启动：```docker run -d --name nginx-test -p 80:80 nginx:1.29.3```

4. 挂载目录
通过挂在宿主机目录，实现配置持久化、日志分离、网页文件独立管理，步骤如下：

第一步：创建宿主机目录
• nginx_logs ：日志文件目录
• nginx_conf ：配置文件目录
• nginx_web ：项目文件目录（这里可以存放web文件）
```python
# 创建html（网页）、conf（配置）、logs（日志）三个目录
mkdir /root/nginx/nginx_conf
mkdir /root/nginx/nginx_logs
mkdir /root/nginx/nginx_web
```
授权文件夹，防止nginx操作文件夹权限不足
```python
chmod 777 /root/nginx/nginx_conf
chmod 777 /root/nginx/nginx_logs
chmod 777 /root/nginx/nginx_web
```
第二步：启动容器并挂载目录
挂载操作会直接将两个文件夹内容同步，若是直接用宿主机的空文件夹直接挂载到容器内部的配置文件目录上，会造成nginx容器配置文件目录被同步为空文件夹，进而导致容器启动失败。故我们需要先启动一遍容器，将初始配置拷贝出来。
创建容器```docker run -itd --name nginx -p 80:80  nginx:1.29.3```
复制容器配置文件到宿主机```docker cp nginx:/etc/nginx /root/nginx_conf```

第三步：删除容器，启动容器并挂载目录
```python
docker rm -f nginx
docker run -itd --name nginx -p 80:80 -v /root/nginx/nginx_web:/var/www/html -v /root/nginx/nginx_conf/nginx:/etc/nginx -v /root/nginx/nginx_logs:/var/log/nginx nginx:1.29.3
```
第四步：修改配置文件
到挂载的配置文件夹```/root/nginx/nginx_conf/conf.d```下，修改```default.conf```,或者新建```conf```文件，在这个目录下，```conf```后缀的文件都会被读取为配置文件(因为```/root/nginx/nginx_conf/nginx.conf```中配置了```include```)

```python
server {
    listen       80;
    listen  [::]:80;
    server_name  localhost;

    # # 设置正确的 MIME 类型
    # include /etc/nginx/mime.types;
    # default_type application/octet-stream;

    # #关闭动态压缩
    # gzip off; 
    # #开启gzip静态压缩功能
    # gzip_static on; 

    #access_log  /var/log/nginx/host.access.log  main;

    location / {
        root   /var/www/html;
        index  index.html index.htm;
    }

    location ~ \.js\.gz$ {
    	gzip off;
    	add_header Content-Encoding gzip;
    	default_type application/javascript;
    }

    location ~ \.wasm\.gz$ {
    	gzip off;
    	add_header Content-Encoding gzip;
    	default_type application/wasm;
    }

    location ~ \.(data|symbols\.json)\.gz$ {
    	gzip off;
    	add_header Content-Encoding gzip;
    	default_type application/octet-stream;
    }
	    
    #error_page  404              /404.html;

    # redirect server error pages to the static page /50x.html
    #
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }

    # proxy the PHP scripts to Apache listening on 127.0.0.1:80
    #
    #location ~ \.php$ {
    #    proxy_pass   http://127.0.0.1;
    #}

    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
    #
    #location ~ \.php$ {
    #    root           html;
    #    fastcgi_pass   127.0.0.1:9000;
    #    fastcgi_index  index.php;
    #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
    #    include        fastcgi_params;
    #}

    # deny access to .htaccess files, if Apache's document root
    # concurs with nginx's one
    #
    #location ~ /\.ht {
    #    deny  all;
    #}
}
```
第四步：将```.html```文件放入宿主机的```nginx_web```文件夹中。

第五步：重启docker
```docker restart nginx```