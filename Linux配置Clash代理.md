# Linux配置Clash代理
## 参考网站
```https://github.com/nelvko/clash-for-linux-install?tab=readme-ov-file```

## 一键安装
```python
git clone --branch master --depth 1 https://gh-proxy.com/https://github.com/nelvko/clash-for-linux-install.git \
  && cd clash-for-linux-install \
  && sudo bash install.sh
```

## clash命令
```python
Usage: 
  clashctl COMMAND [OPTIONS]

Commands:
    on                    开启代理
    off                   关闭代理
    proxy                 系统代理
    ui                    面板地址
    status                内核状况
    tun                   Tun 模式
    mixin                 Mixin 配置
    secret                Web 密钥
    update                更新订阅
    upgrade               升级内核

Global Options:
    -h, --help            显示帮助信息
```


## 启动停止命令
```python
clasctl on
😼 已开启代理环境

clashctl off
😼 已关闭代理环境
```