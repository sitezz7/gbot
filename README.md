# grass 第二季超稳定无限多开脚本 由 志贤说 开源

- 微信：caba_9527
- b 站：志贤说 [点击跳转](https://space.bilibili.com/87933252)
  https://space.bilibili.com/87933252
- 实际运行效果视频
  [大厂开发 Grass 二期、nodepay 最强稳定脚本开发运行效果来了！！！零撸空投领取，depin 项目合集](https://www.bilibili.com/video/BV1xrByYMEYL/?spm_id_from=333.999.0.0)
  https://www.bilibili.com/video/BV1xrByYMEYL/?spm_id_from=333.999.0.0

# 注册

没有注册的朋友可以走我的邀请链接支持一下：[grass 注册](https://app.getgrass.io/register/?referralCode=BAR6o8kdfGr5p5d)

# 使用方法

## 1、没有开发环境和经验的朋友可以不用往下看了，直接加我微信：caba9527，发整套压缩包给你，运行起来就完事了

## 2、有开发经验的往下看

1. 下载项目

   ```
   git clone https://github.com/GzGod/grass-bot
   ```

2. 下载完了之后使用命令行工具进入项目文件夹
   window 系统直接在打开文件窗口的地址栏输入 cmd 回车，你会看到打开了一个黑框

3. 在黑框里输出一下命令，进入 grass-bot 文件夹：

   ```shell
   cd grass-bot
   ```

4. 然后安装所需的库：（没有 python 环境请先安装 python，自行搜索）

   ```shell
   python -m pip install -r requirements.txt
   ```

5. 用你电脑的浏览器打开 grass 的 dashborad，也就是展示积分的那个页面，然后打开浏览器控制台，输入以下代码，复制 userId

   ```javascript
   copy(JSON.parse(localStorage.getItem("userId")))
   ```

   这行代码会自动将用户 ID 复制到你的剪贴板，所以你只需将其粘贴到 `userid.txt` 文件中 6. 配置代理
   打开 proxies.txt 文件，将你代理的 ip 和端口填入，格式如下：

   ```
   协议://用户名1:密码1@ip1:端口1
   协议://用户名2:密码2@ip2:端口2
   ```

   比如 http 协议的：

   ```
   http://awsgsdf:3xus22sx@42.101.201.4:1006
   http://awsgsdf:3xus22sx@31.151.231.82:1007
   ```

   或者 socks5 协议的：

   ```
   socks5://awsgsdf:3xus22sx@42.101.201.4:1006
   socks5://awsgsdf:3xus22sx@31.151.231.82:1007
   ```

6. 运行脚本

   ```bash
   python main.py
   ```

7. 运行效果
   ![alt text](image.png)

# 联系作者

有问题加我微信：caba9527
