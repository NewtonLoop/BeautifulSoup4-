# 应用BS4爬取庆余年全本小说
选择网站 :  http://www.aixiawx.com/16/16039
## 1. 逻辑
+ 应用for循环遍历网页中所有url
+ 运用正则表达式筛选所需url  
 经分析网页得知, 含有小说内容的url中都有/16/16039/*, 使用正则表达式筛选出所需url
 + 打开筛选url, 提取内容, 存入文档
 ## 2.难点
 + 资源未正确释放  
一开始运行时程序常无故暂停, 无报错, 经百度后在打开url语句后添加  
 **with urllib.request.urlopen(url, timeout=30) as rep:**  
 **rep.read()**  
 保证资源的释放
 + DNS解析出现问题  
 先后更换阿里\谷歌公共DNS, 爬取最远的一次使用的是阿里的223.5.5.5
 ## 注 : 小说名
 + 文件名为YuNianTest+重新试验次数

 powershell 运行截图  
 ![powershell运行截图.png](https://i.loli.net/2020/07/30/U5pMn1SRCItTVxD.png)  
 网页解析截图  
 ![网页解析截图.png](https://i.loli.net/2020/07/30/zEPhpMTjI29AsNO.png)