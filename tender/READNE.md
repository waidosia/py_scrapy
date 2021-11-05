### 说明
该框架采用python3.9，Scarpy框架进行开发，目前爬取网站为
`中国采购与招标网` `招标网`

爬取的内容为标题，发布时间及URL地址

数据存储采用MongoDB与Excel

通知方式为邮件通知

### 使用
1、安装依赖
pip install requirements.txt
2、配置参数
keyword.conf为网站对应关键字
webname.conf为网站对应名称
common/consts为常量值
3、运行run方法，等待程序跑完，查看结果

### 运行结果
1、程序运行时
![](https://pic-1300802512.cos.ap-guangzhou.myqcloud.com/zw8imnb2og-1636101442963.png)
2、excel界面
![](https://pic-1300802512.cos.ap-guangzhou.myqcloud.com/jwoumvus9p-1636104680447.png)
3、数据库界面
![](https://pic-1300802512.cos.ap-guangzhou.myqcloud.com/wr27i5410d-1636105098777.png)
4、邮件界面
![](https://pic-1300802512.cos.ap-guangzhou.myqcloud.com/8my92pr8tm-1636105180008.png)