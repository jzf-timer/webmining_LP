# -*- coding: utf-8 -*-
import requests
import scrapy
import xlwt
from lxml import etree


class LpSpider(scrapy.Spider):
    name = 'LP'
    allowed_domains = ['www.liepin.com']

    start_urls = ['www.liepin.com']



    def start_requests(self):
        allinfo=[]
        #以下是关于上海的循环
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'}
        for i in range(9):
            SHurl='https://www.liepin.com/zhaopin/?compkind=&dqs=020&pubTime=&pageSize=40&salary=&compTag=&sortFlag=15&degradeFlag=0&compIds=&subIndustry=&jobKind=&industries=&compscale=&key=%E6%96%B0%E5%AA%92%E4%BD%93%E8%BF%90%E8%90%A5&siTag=qkuPMtyyPWyGJLVm3Ykn1A%7Er3i1HcfrfE3VRWBaGW6LoA&d_sfrom=search_fp&d_ckId=c51a068c5cb658f7f4040175ba945596&d_curPage=2&d_pageSize=40&d_headId=4107d9372116a7333a50ba34629aa075&curPage={}'.format(i)
            response=requests.get(SHurl,headers=headers)
            # print(response.text)
            response=etree.HTML(response.text)
                                #//*[@id="sojob"]/div[3]/div/div[1]/div[1]/ul/li/div/div[1]
            divs=response.xpath('//*[@id="sojob"]/div[3]/div/div[1]/div[1]/ul/li/div')#div列表
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
        #以下是深圳的循环
            SZurl='https://www.liepin.com/zhaopin/?compkind=&dqs=050090&pubTime=&pageSize=40&salary=&compTag=&sortFlag=15&degradeFlag=0&compIds=&subIndustry=&jobKind=&industries=&compscale=&key=%E6%96%B0%E5%AA%92%E4%BD%93%E8%BF%90%E8%90%A5&siTag=qkuPMtyyPWyGJLVm3Ykn1A%7E-nQsjvAMdjst7vnBI-6VZQ&d_sfrom=search_fp&d_ckId=d2ad9da103fc2aeeabc169d685a2fdfd&d_curPage=0&d_pageSize=40&d_headId=4107d9372116a7333a50ba34629aa075&curPage={}'.format(i)
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
        #以下是重庆地区的循环
            if i == 8:
                continue
            CQurl='https://www.liepin.com/zhaopin/?compkind=&dqs=040&pubTime=&pageSize=40&salary=&compTag=&sortFlag=15&degradeFlag=0&compIds=&subIndustry=&jobKind=&industries=&compscale=&key=%E6%96%B0%E5%AA%92%E4%BD%93%E8%BF%90%E8%90%A5&siTag=qkuPMtyyPWyGJLVm3Ykn1A%7EDnIK07pheM0dUfyGVexLMQ&d_sfrom=search_fp&d_ckId=c706a5381914b6c01150e2841750acbd&d_curPage=0&d_pageSize=40&d_headId=4107d9372116a7333a50ba34629aa075&curPage={}'.format(i)
            response = requests.get(CQurl, headers=headers)
            response1 = etree.HTML(response.text)
            divs = response1.xpath('//*[@id="sojob"]/div[3]/div/div[1]/div[1]/ul/li/div')  # div列表
            if divs==[]:
                continue
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
        f = xlwt.Workbook()
        sheet1 = f.add_sheet('sheet1', cell_overwrite_ok=True)
        style = xlwt.XFStyle()
        style.num_format_str = 'yyyy/mm/dd'
        alignment = xlwt.Alignment()
        alignment.horz = xlwt.Alignment.HORZ_CENTER
        alignment.vert = xlwt.Alignment.VERT_CENTER
        style.alignment = alignment
        table_title = ['工作标题', '薪资', '地区', '学历', '经验', '公司']
        for c in range(len(table_title)):
            sheet1.write(0, c, table_title[c], style)
        # print(data_list)
        for x in range(len(allinfo)):
            for y in range(len(allinfo[x])):
                sheet1.write(x + 1, y, str(allinfo[x][y]), style)
        f.save(r'./猎聘新媒体运营.xls')
        response = scrapy.Request('https://www.liepin.com', headers=headers, callback=self.parse)
        # response.meta['hao'] = hao  # Request.meta中的特殊关键字，其中的传参方法
        yield response

    def parse(self, response):
        pass

