# Linux Screen 介绍与使用教程
Screen 是 Linux/Unix 系统中一个强大的终端多路复用器（terminal multiplexer），它允许用户在一个物理终端上创建、访问和控制多个终端会话。即使网络连接中断，Screen 能保持会话活跃，让用户重新连接后继续工作，是远程服务器管理的必备工具。

## 安装
```python
# Debian/Ubuntu
sudo apt update && sudo apt install screen

# CentOS/RHEL
sudo yum install screen

# Fedora
sudo dnf install screen

# macOS (使用Homebrew)
brew install screen
```

## 基本使用
```python
# 1. 启动，启动后会进入一个新的 Screen 会话，界面与普通终端相似。
screen

# 2. 名会话 
screen -S 会话名
# 例如
screen -S development


# 3. 退出 Screen（不终止会话）
按下 Ctrl + a，然后按 d（detach）
这会将 Screen 会话置于后台，但所有进程继续运行。

# 4. 列出所有运行中的会话
screen -ls

# 重新连接到指定会话
screen -r 会话ID或会话名
# 例如
screen -r 12345
screen -r development

# 5. 完全终止 Screen 会话
在 Screen 会话内，直接输入 exit 命令或按 Ctrl + d 可以完全退出并终止会话。
```

## 快捷键
```python
四、常用快捷键
Screen 的命令通常以 Ctrl + a 作为前缀，然后跟另一个命令键：

会话管理
Ctrl + a, d - 分离(detach)当前会话
Ctrl + a, k - 终止当前窗口（确认后）
Ctrl + a, \ - 终止所有窗口并退出 Screen
窗口管理
Ctrl + a, c - 创建新窗口
Ctrl + a, n - 切换到下一个窗口
Ctrl + a, p - 切换到上一个窗口
Ctrl + a, 0-9 - 切换到指定编号的窗口（0-9）
Ctrl + a, w - 显示窗口列表
Ctrl + a, " - 以菜单方式列出所有窗口
Ctrl + a, A - 重命名当前窗口
分屏功能
Ctrl + a, S - 水平分割当前区域
Ctrl + a, | - 垂直分割当前区域
Ctrl + a, Tab - 在不同区域间切换
Ctrl + a, X - 关闭当前区域
Ctrl + a, Q - 关闭除当前区域外的所有区域
其他实用命令
Ctrl + a, ? - 显示帮助和所有快捷键
Ctrl + a, [ - 进入复制/滚动模式（使用方向键或PgUp/PgDn滚动）
Ctrl + a, ] - 粘贴最近复制的内容
Ctrl + a, > - 写入屏幕日志
Ctrl + a, :screen -L - 启动日志记录
```