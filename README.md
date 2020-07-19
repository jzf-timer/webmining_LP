# 20春_Web数据挖掘_期末项目

#  
> (数据加值宣言：本项目产出按XXX及XXX挖掘的关于YYY(例子: NPS)工作的数据，以解决NPS就业需求及特性的就业分析问题)
> 注. 需达成评价表格PRD1.考核内容：＂作者成功地把数据产品对加值（总结解决什么问题）的精确丶专业及中肯地总结表述于第一段"
* 运用 scrapy框架 挖取猎聘网中，两个经济特区城市 深圳和上海 的”外加新一线城市重庆的“新媒体运营人员”职位的详情页内容，并生成excel表格。有薪资-工作要求-学历-年龄等基本信息。

数据加值: 得到一线城市中具有代表性的新媒体运营人员职业的信息，解决数据分析师方向职业需求，得知薪资-要求等概况（相同或差异）



# 数据最小可用产品
> (MVP的数据加值)：需达成评价表格PRD2.考核内容：＂作者成功地具体表述数据产品的数据类型及内容如何构成最小可用产品MVP的核心价值（具体什么数据解决什么问题）
*  得到两个经济特区城市 深圳和上海和重庆这个最近发展迅速的新媒体运营职业的信息，解决新媒体运营方向职业需求，得知薪资-要求等概况（相同或差异）。让想要去一线或者新一线城市就职新媒体运营的人群可以知道需要什么样的条件，薪资概况等等。可以更加有目的性的寻找职位，并且增加一定的求职成功概率。

# 挖掘Query参数
 Query参数包括：1. Jobtitle 职称 2. Salary 工资 3. Area 地区 4.  AcademicDegree 学历 5.Experience 经验 6.Company 公司
   
 ||1.薪资|2.地区|3.学历|4.经验|5.公司名称|6.工作标题|
|  ----  | ----  |  ----  | ----  |  ----  | ----  | ----  |
| 0  |  10-15k·12薪|上海-徐泾 |本科及以上 | 3-5年 | 上海麦巢农业科技发展有限公司 |新媒体运营总监  |   

 ``` SZurl='https://www.liepin.com/zhaopin/?compkind=&dqs=050090&pubTime=&pageSize=40&salary=&compTag=&sortFlag=15&degradeFlag=0&compIds=&subIndustry=&jobKind=&industries=&compscale=&key=%E6%96%B0%E5%AA%92%E4%BD%93%E8%BF%90%E8%90%A5&siTag=qkuPMtyyPWyGJLVm3Ykn1A%7E-nQsjvAMdjst7vnBI-6VZQ&d_sfrom=search_fp&d_ckId=d2ad9da103fc2aeeabc169d685a2fdfd&d_curPage=0&d_pageSize=40&d_headId=4107d9372116a7333a50ba34629aa075&curPage={}'.format(i)
            response = requests.get(SZurl, headers=headers)
            response1 = etree.HTML(response.text)
            divs = response1.xpath('//*[@id="sojob"]/div[3]/div/div[1]/div[1]/ul/li/div')  # div列表
            print(divs)
            for div in divs:
                Jobtitle = div.xpath('./div[1]/h3/a/text()')  # 工作标题
                Jobtitle = Jobtitle[0].replace('\r', '').replace('\n', '').replace('\t', '')
                Salary = div.xpath('./div[1]/p[1]/span[1]/text()')  # 薪资
                Area = div.xpath('./div[1]/p[1]/a/text()')  # 地区
                # print(Area)
                if Area != []:
                    AcademicDegree = div.xpath('./div[1]/p[1]/span[2]/text()')  # 学历
                    Experience = div.xpath('./div[1]/p[1]/span[3]/text()')  # 经验
                    Company = div.xpath('./div[2]/p/a/text()')  # 公司
                else:
                    Area = div.xpath('./div[1]/p[1]/span[2]/text()')  # 地区
                    AcademicDegree = div.xpath('./div[1]/p[1]/span[3]/text()')  # 学历
                    Experience = div.xpath('./div[1]/p[1]/span[4]/text()')  # 经验
                    Company = div.xpath('./div[2]/p/a/text()')  # 公司
                print(Jobtitle, Salary[0], Area[0], AcademicDegree[0], Experience[0], Company[0])
                allinfo.append([Jobtitle, Salary[0], Area[0], AcademicDegree[0], Experience[0], Company[0]])
 ```  
    
# 思路方法及具体执行  

1. 确定好要解决的问题——“老一线城市”和新一线代表城市中的新媒体运营职业详情，了解行业具体发展情况，观察薪资差异以及工作要求难度的差异。

2. 选取猎聘网为数据挖掘——www.liepin.com  

3. 用scrapy框架爬取相关的城市新媒体运营职位的页面链接和首页概况的年龄、薪资等基本信息 

4. 用scrapy框架将上一步的各个职位招聘的详情页信息爬取形成excel表格  

5.方法选择：初始 使用request模块+xpath 是为了可以爬取现有的新媒体运营职业相关信息 然后构建单页数据和多页数据模板 供后面的scrapy框架代码提供一定基础
            后面选择scrapy框架 是为了可以更好地将老一线城市 北上广深和新一线城市中的代表城市重庆中新媒体运营人员的职业信息  
            
6.单页数据：[WebMining_final_newmedia_单页](https://github.com/jzf-timer/webmining_LP/blob/master/WebMining_final_newmedia_%E5%8D%95%E9%A1%B5.xlsx)

7 翻页数据连接：[WebMining_final_newmedia_翻页](https://github.com/jzf-timer/webmining_LP/blob/master/WebMining_final_newmedia_%E7%BF%BB%E9%A1%B5.xlsx)

8 [scrapy爬虫代码连接](https://github.com/jzf-timer/webmining_LP/blob/master/LiePing/spiders/LP.py)   

9 用scrapy框架输出表格


![avatar](/webmining_LP/output.jpg)
   
   
- 后续scrapy框架构筑时用的参数   
 
        ```
		'edu':      '//div[contains(@class,"job-info")]/p/span[@class="edu"]',  
        
        '经验':      '//div[contains(@class,"job-info")]/p/span[@class="edu"]/following-sibling::span',  
        
        '薪水':    '//div[contains(@class,"job-info")]/p/span[@class="text-warning"]',   
        
        '时间':    '//div[contains(@class,"job-info")]/p/time/@title',   
        
        '职称':    '//div[contains(@class,"job-info")]/h3/a',   
        
        '公司地点': '//div[contains(@class,"job-info")]/p/a',  
        
        '公司名称': '//div[contains(@class,"sojob-item-main")]//p[@class="company-name"]/a', 
		```    
  
# ipynb py文档链接

[request+xpath 构筑翻页数据和单页数据 ipynb链接](https://github.com/jzf-timer/webmining_LP/blob/master/%E5%A4%9A%E9%A1%B5%E6%95%B0%E6%8D%AE%E7%88%AC%E5%8F%96.ipynb)

[scrapy框架所用的spider py文件](https://github.com/jzf-timer/webmining_LP/blob/master/LiePing/spiders/LP.py)

## 数据连接    
[单页数据](https://github.com/jzf-timer/webmining_LP/blob/master/WebMining_final_newmedia_%E5%8D%95%E9%A1%B5.xlsx)

[翻页数据连接](https://github.com/jzf-timer/webmining_LP/blob/master/WebMining_final_newmedia_%E7%BF%BB%E9%A1%B5.xlsx)

[scrapy所爬取的数据](https://github.com/jzf-timer/webmining_LP/blob/master/%E7%8C%8E%E8%81%98%E6%96%B0%E5%AA%92%E4%BD%93%E8%BF%90%E8%90%A5.xls)  



# 心得总结及感谢


&gt;参考文档:
[初窥Scrapy](https://scrapy-chs.readthedocs.io/zh_CN/latest/intro/overview.html)  
[scrapinghub部署教程](https://blog.csdn.net/zjkpy_5/article/details/86646204)   
[《Learning Scrapy》（中文版）第6章 ](https://www.jianshu.com/p/441fa74d7aad)  


