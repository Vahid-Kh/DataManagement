import funcTxtAnalytics as ff
import urllib.request, urllib.parse
import matplotlib.pyplot as plt
from wordcloud import WordCloud
wordstring = 'it was the best of times it was the worst of times '
wordstring += 'it was the age of wisdom it was the age of foolishness'

wordlist = wordstring.split()

wordfreq = []
# for w in wordlist:
#     wordfreq.append(wordlist.count(w))

# wordfreq = [wordlist.count(w) for w in wordlist]  # a list comprehension
# print("Pairs\n" + str(list(zip(wordlist, wordfreq))))
"""url = 'https://www.lens.org/lens/patent/119-821-849-121-092/fulltext'
url = 'https://www.lens.org/images/patent/US/20190360639/A1/US_2019_0360639_A1.pdf'
url = 'https://ph.parker.com/dk/da/safety-exhaust-valve-p33-series-pneumatic-division-europe'
print(url)
response = urllib.request.urlopen(url)
print(ff.printtext(response))
html = response.read()
text = ff.stripTags(html).lower()
print(text)"""



text = """
3m Innovative Properties Co3	
3m Innovative Properties Co4	
3m Innovative Properties Company1	
8 Rivers Capital LLC4	
Aavid Thermalloy LLC2	
Aavid Thermalloy LLC2	
Abb Power Grids Switzerland Ag2	
Abb Schweiz Ag1	
Abb Schweiz Ag2	
Adeia Semiconductor Bonding Tech INC2	
Advanced Micro Devices INC1	
Advanced Micro Devices INC2	
Advanced Micro Devices INC6	
Aecorsis B V1	
Agency Science Tech & Res2	
Agency Science Tech & Res3	
Ahr Energy Spa1	
Air Liquide American1	
Air Liquide2	
Aitaisi Thermal System Res and Development Shanghai 	
Aleees EArk (Cayman) 	
Aleees EArk Cayman 	
Anhui Jianghuai Automobile  Corp 	
Anhui Jianghuai Songz Air Conditioning 	
Anhui Vocational & Technical College1	
Anhui Weihong Electronic Tech 	
Anhui Zhonghe Tongyuan Tech 	
Antpool Tech Limited2	
Aofu Auto Parts Heat System Tech Branch1	
Apple INC1	
Applied Materials INC3	
Aptiv Tech 	
Aptiv Tech 	
Aquafair Ab3	
Arctic Impulse Oy2	2
Arista Networks INC1	
Asia Vital Components 	
At & S Austria Tech & Systemtechnik Ag2	
At & S Austria Tech & Systemtechnik Ag4	
Austria Tech & System Tech1	
Austria Tech & System Tech3	
Autonetworks Technologies 	
Bae Systems Plc1	
Baidu Us 	
Baidu Usa LLC7	
Bamford Excavators 	
BarNv2	
Basic Semiconductor 	
Bayerische Motoren Werke Ag1	
Beierbian  	
Beijing Anxing Gaoke New Energy Dev 	
Beijing Anxing Gaoke New Energy Dev 	
Beijing Billion Wharton Science and Tech 	
Beijing Deepcool Ind 	
Beijing Ecoso Energy Tech 	
Beijing Electric Vehicle 	
Beijing Herui Energy Storing Tech 	2
Beijing Inst Petrochem Tech1	
Beijing Inst Petrochem Tech1	
Beijing Institute of Space Mech & Electricity2	
Beijing Institute Tech2	
Beijing Jingyi Automation Equipment 	
Beijing Ruijie Networks 	
Biadi Semiconductor 	
Biber Catharina1	
Bitmain Tech INC3	
Bitmaintech Pte 	
Blueocean Ningbo Tech 	
Boe Technology  	
Bollinger Motors INC2	
Booz Allen Hamilton INC1	
Booz Allen Hamilton INC2	
Breakthrough Electrical Tianjin Company3	3
Bu Yingqiong1	
Byd 	6
Carrier Corp10	
Carrier Corp3	
Cccc Fhdi Eng 	
Ccic  Gongxin Security Tech 	
Celestica Technology Consultancy Shanghai 	
Celestica Technology Consultancy Shanghai 	
Changjiang Electronics Tech Management 	
Changsha Anmuquan Intelligent Tech 	
Changzhou Engineering Technology Institute of Jiangsu Univ1	
Changzhou Langjie Electronics 	
Changzhou Tianmu Intelligent Tech 	
Changzhou Weihan Thermal Control Tech 	
Chart INC4	
Chen Hanlin1	
Chen Nan3	
Chen Yunshui3	
Chengdu Bus 	
Chengdu Gongjue Microelectronics 	
Chengdu Sailisi Tech 	
Chengdu Sailisi Tech 	
Chery Automobile 	
Chery New Energy Automobiles 	
China Automotive Eng Res Inst1	
China Faw  Corp2	
China Faw  Corp3	
China Inf Technology Designing Consulting Inst 	
China Nat Petroleum Corp1	
China Petroleum & Chem Corp Qingdao Safety Eng Inst3	
China Petroleum & Chem Corp3	
China Petroleum Logging 	
China Ship Scient Res Ct1	
China Unicom4	
Chinese Spaceflight Department Industrial Flight Tech Research Institute Chinese Spaceflight Hawk El2	
Chipmore Tech Corporation Limited2	
Chongqing Changan New Energy Automobile Tech 	
Chongqing Jinkang Sailisi New Energy Automobile Design Inst 	
Chongqing Konka Optoelectronic Tech Res Inst 	
Chongqing Livan Automobile R&d Inst 	
Chongqing Pingwei Entpr 	
Chongqing Sailisi New Energy Automobile Design Inst 	
Chu Wei Ming1	
Chuneng New Energy 	
CisTech INC2	
Cistet Electrical Equipment Company1	
Climate Master INC4	
Climaveneta Chatunion Refrigeration Equipment Shanghai 	
Cn Elect Tech No 14 Res Inst2	
Cn Elect Tech No 14 Res Inst2	
Commissariat Energie Atomique3	
Contemporary Amperex Technology 	
Contemporary Amperex Technology 	
Cooler Master Tech INC1	
Cosemitech Shanghai 	
Crrc Zhuzhou Inst 	
Cssc Huangpu Wenchong Shipbuilding 	
Daewoo Shipbuilding & Marine9	
Daikin Europe Nv1	
Daikin Europe Nv6	
Daikin Ind 	
Daikin Ind 5	
Daikin Ind 	
Dana Canada Corp1	
Dawning Information Ind Beijing 	
Deeia INC5	
Deep Sea Tech Science Taihu Laboratory1	
Deere & Co2	
Deere & Co2	
Dell Products Lp4	
Delta Design INC1	
Denso Corp1	
Denso Corp1	
Denso Corp19	
Denso Corp3	
Denso Corp3	
Denso Corp5	
Dier Company1	
Dimaag Ai INC1	
Domain Electric  Nanjing 	
Dongfeng Automobile  Stock Company1	
Dongfeng Mahle Thermal Systems 	
Dongfeng Motor Corp1	
Dongfeng Motor  	
Dongguan Zhongzhi Electronic Technology 	
Dongke Semiconductor Anhui 	
Doowon Climate Control 	
Draexlmaier Lisa Gmbh2	
Dugen Laser Tech Suzhou 	
Dugen Laser Tech Suzhou 	
Dunan Env Tech 	
Dupont Eric3	
East West Mfg LLC1	
East West Mfg LLC1	
EIce Kaelte Gmbh1	
Edwards Vacuum LLC1	
Edwards Vacuum LLC2	
Efficiency for Lng Applications S L2	
Electric Power Res Inst State Grid Jibei Electric Power 	
Electrical Equipment Branch Fujian Nanping Minyan Electric Power Construction 	
Electrical Equipment Branch of Fujian Nanping Minyan Electric Power Construction 	
Electronics & Telecommunications Res Inst1	
Emc Ip Holding LLC1	
Emerson Climate Technologies3	
Enermotion INC1	
Engie1	
Enn Science & Tech Dev 	
Envision Power Tech Jiangsu 	
Esametal S R L3	
Evergrande New Energy Automobile Invest Holdings  	
Exxonmobil Upstream Res Co2	
Facebook INC1	
Fan Yuehong1	
Fang Zhi Qiang1	
Faw Benteng Car 	
Faw Jiefang Automotive Co1	
Fawer Automotive Parts Company1	
Fed Gosudarstvennoe Byudzhetnoe Nauchnoe Uchrezhdenie Fed Nauchnyj Agroinzhenernyj Tsentr Vim Fgbnu1	
Fenda Tech 	
Fluid & Thermal Man S L1	
Ford Global Tech LLC4	
Forehope Electronic Ningbo 	
Foshan H&d Automation 	
Foshan Kuangmi Tech 	
Foshan Third Peoples Hospital Foshan Mental Health Center1	
Foshan Wandaye Machinery 	
Foshan Yeling Shidai Tech 	
Foxconn Tech 	
Fuao Automotive Parts 	
Fuao Zhiyan Shanghai Automobile Tech 	
Fuji Electric 5	
Fujian Weiyi Tech 	
Fujitsu General 	
Fujitsu 	
Fujitsu 	
Fuqing Kailian Electronic Tech 	
Fushu Seret Environmental Prot Science 	
Fushun Seperate Environmental Protection Tech 	
Ganzhou Xunkang Electronic Tech 	
Gaz Transport & Technigaz2	
Gaztransport Et Technigaz12	
Ge Grid Solutions LLC1	
Geely Automobile Res Institute Ningbo 	
Geely Holding  3	
Geely Holding  	
Gen Electric2	
Gentherm INC2	
Giga Computing Tech 	
Gm Global Tech Operations LLC1	
Gm Global Tech Operations LLC3	
Goodman Global  INC2	
Google INC1	
Google LLC2	
Google LLC4	
Google LLC4	
Grasschain Tech Pty 	
Great Team Backend Foundry Dongguan 	
Great Wall Motor 	
Great Wall Motor 	
Gree Electric Appliances INC Zhuhai2	
Gree Electric Appliances INC Zhuhai26	
Gree Electric Appliances INC Zhuhai3	
Gree Electric Appliances INC Zhuhai7	
Gree Electric Appliances Wuhan 	
Guandong Midea Hvac Equipment2	
Guangdong Changnengda Tech Development 6	
Guangdong Changnengda Tech Development 	
Guangdong Giwee Tech 	
Guangdong Guangda New Energy Tech 	
Guangdong Hui Core Semiconductor 	
Guangdong Huixin Semiconductor 	
Guangdong Midea Refrigeration Equipment 	
Guangdong Midea White Home Appliance Tech Innovation Center 	
Guangdong Shenling Env Systems 	
Guangdong Xinjuneng Semiconductor 	
Guangdong Yingwei Fluid Control Tech 	
Guangdong Yourui Electronic Tech 	
Guangdong Zhongde Haotai Energy Equipment 	
Guangdong Zhuhai Supervision Testing Inst of Quality & Metrology2	
Guangzhou Automobile  Co1	
Guangzhou Inst Energy Conversion Cas2	
Guangzhou Wide Ind 	
Guangzhou Xiaopeng Motors Tech 	
Guangzhou Xpeng Automobile Tech 	
Gupta Sanjay2	
Haier Smart Home 	
Haier Smart Home 	
Hamfop Tech LLC2	
Hamilton Sundstrand Corp1	
Hanganu Dan Alexandru3	
Hangzhou International Science and Technology Innovation Center of Zhejiang Univ1	
Hangzhou International Science and Technology Innovation Center of Zhejiang Univ5	
Hangzhou Lvneng New Energy Auto Parts 	
Hangzhou Ruihao Electric Appliance 	
Hangzhou Sanhua Inst 	
Hangzhou Sanhua Inst 	
Hangzhou Sanhua Res Inst 	
Hangzhou Sanhua Res Inst 	
Hangzhou Yunku Intelligent Tech 	
Hangzhou Zhuobang Env Equipment 	
Hanon Automotive Components 	
Hanon Systems8	
Haoli Electromechanical Suzhou 	
Harbin Inst Technology1	
Heatcraft Refrigeration Products LLC17	
Heatscape Com INC2	
Hefei General Machinery Res Inst 	
Hefei Swan Refrigeration Tech6	
Hefei Wenxuan New Energy Tech 	
Hella Gmbh & Kgaa1	
Henan Derry New Energy Automobile 	
Henan Longxiang Electric 	
Highview Entpr 	
Hitachi Energy 	
Hitachi Energy Switzerland Ag2	
Hongfujin Prec Electronics Tianjin 	
Hongfujin Prec Electronics Tianjin 	
Huaneng Clean Energy Res Inst1	
Huatian Tech Nanjing 	
Huawei Digital Energy Tech Limited Company1	
Huawei Digital Power Tech 	
Huawei Digital Power Tech 	
Huawei Digital Power Tech 	
Huawei Digital Power Tech 	
Huawei Tech 1	
Huawei Tech 	
Huawei Tech 	
Huaxiang Xiangneng Tech 	
Hubei Water Blue Sky Combined Gas Company1	
Hubei Yingfu Electric Power 	
Huizhou Eve Energy 	
Hunan Guoxin Semiconductor Tech 	
Hunan Zhihaohang Precision Tech 	
Hyundai Motor 5	
Hyundai Motor 7	
Hyundai Motor 	
Hyundai Motor 	
Hyundai Motor Gompany1	
Hyundai Wia Corp1	
Iat Automobile Technology 	
Ibm11	
Ibm7	
Iceotope  	
Im Motors Tech 	
Imec Vzw2	
Ind Tech Res Inst2	
Infineon Technologies Ag16	
Infineon Technologies Ag3	
Inner Mongolia Beike Jiaoda Robot 	
Inner Mongolia Xingyang Tech 	
Inst Electrical Eng Cas2	
Inst Microelectronics Cas3	
Inst Microelectronics Cas3	
Inst of Electrical Engineering of Chinese Academy of Sciences2	
Institute of Environment Friendly Materials and Occupational Health Anhui Univ of Science & Technolo1	
Intel Corp1	
Intel Corp17	
Intel Corp9	
Jiai Joint Type Consultation1	
Jiangsu Fengying Tech 	
Jiangsu Huaqiang New Energy Tech 	
Jiangsu Junze Electric 	
Jiangsu New Special Transf Technology Corp 	
Jiangsu Su Cheng  	
Jiangsu Tenesun Heat Pump Co4	
Jiangsu Zhongguancun Science and Tech Industrial Park Energy Saving and Environmental Protection Res1	
Jiangsu Zhongjiao Electrical 	
Jiangsu Zhongke Xinyuan Semiconductor Tech 	
Jiangxi Rucol Refrigeration Tech 	
Jiangyin Gelanfu Heat Energy Tech 	
Jiaxing Dynaheim Intelligent Tech 	
Jidu Tech 	
Jiebei Automobile Company1	
Jing Jin Electric Tech 	
Jingjiang Donglei Motor 	
Jingzhou Chutai New Energy Tech 	
Jinjiang Yuanjian Trade 	
Jinlong Motor Air Conditioner 	
Jiuquan Iron & Steel  Co2	
Jmj Korea 2	
Johnson Controls Tech Co1	
Johnson Controls TyIp Holdings Llp2	
Kawasaki Heavy Ind 	
Ke Lirong1	
Kelvin New Energy Tech 	
Keppel Offshore & Marine Tech Ct Pte 	
Kia Corp14	
Kia Corp4	
Kia Corp7	
Kia Motors Corp13	
Kia Motors Corp3	
Kia Motors Corp8	
Kia Motors Gorporation1	
Kidde Tech INC2	
Kim Bong Suck3	
Kim Su Min2	
Knorr Bremse Australia Pty 	
Knorr Bremse Rail Vehicle System Enterprise Man Beijing 	
Koninklijke Philips Nv2	
Konvekta Ag2	
Korea Gas Corp1	
Korea Inst Mach & Materials1	
Korea Inst Mach & Materials1	
Korea Shipbuilding & Offshore Eng 	
Kunshan Tongchuan Copper Industry Tech 	
Lair Liquide Sa Pour Letude Et L’exploitation Des Procedes Georges Claude1	
Leyton Automobile Part Suzhou Company1	
Lg Electronics INC32	
Lg Energy Solution 	
Li Canfeng2	
Liaoning Shenghong Tech 	
Liku New Energy Tech Shanghai 	
Liku New Energy Tech Shanghai 	
Lincheng Power Supply Branch Company State Grid Hebei Electric Power Company1	
Liu Changzhi3	
Liu Yingjie2	
Liu Zhanyu2	
Liupanshui Xingtai Transf 	
Liuzhou Yizhou Automobile Air Conditioner 	
Luzhou Power Supply of Sichuan Electric Power Corp1	
Maanshan Haoyuan Electronic 	
Mahle Int Gmbh1	
Mahle Int Gmbh2	
Manche Electronics 	
Marazzo Christopher1	
Marelli Cabin Comfort Japan Corp2	
Marelli Corp2	
Mbgsholdings Pty 	
Meidensha Electric Mfg 	
Microsoft Technology Licensing LLC3	
Microsoft Technology Licensing LLC5	
Microsoft Technology Licensing LLC6	
Midea  	
Midea  	
Mind Electronics Appliance 	
Mitsubishi Electric Corp5	
Mitsubishi Electric Corp7	
Mitsubishi Electric Corp9	
Mitsubishi Heavy Ind 	
Mitsubishi Shipbuilding 	
Nanjing Canatal Data Ct Env Tech 	
Nanjing Tica Climate Solutions 	
Nanping Electric Power Supply Company of State Grid Fujian Electric Power Company2	
Nantong Meijile Refrigeration Equipment 	
Nanyang Ruiguang Transf 	
Nat Ct Advanced Packaging Ncap China11	
National Energy Longyuan Blue Sky Energy Saving Tech Limited Company2	
Nec Corp2	
Nec Corp4	
Nec Corp5	
Ningbo Geely Automobile Res & Development 	
Ningbo Hrale Plate Heat Exchanger 	
Nio Anhui Holding 	
Nokia Technologies Oy4	
Nomen Calvet Juan Eusebio3	
Nooter/eriksen INC1	
Nooter/eriksen INC2	
North Integrated Circuit Tech Innovation Center Beijing 	
Oh Seoung Jae1	
Ovh4	
Panasonic Cold Machine System Dalian 	
Panasonic Ip Man Corp3	
Parity2	
Parker Hannifin Corp2	
Pearl Haige Electric Appliance 	
Pinjie Electronic Suzhou 	
Qi Yuan2	
Qiang Xinqi3	
Qingdao Haier Air Conditioner Electric 	
Qingdao Haier Air Conditioner General Corp 	
Qingdao Haier Air Conditioning Electronic 	
Qingdao Hisense Hitachi Air Conditioning Sys 	
Qingdao Longertek New Energy Equipment 	
Quanta Associates Lp1	
Raytheon Co2	
Raytheon Co4	
Regascold Gmbh2	
Romeo Systems Tech LLC2	
Rondane Teknologi As1	
Samsung Electronics 	
Samsung Electronics 	
Sanhua Holding  	
Sanyhe Internat Holdings Co2	
Sdaac Automotive Air Conditioning Systems 	
Seiko Epson Corp1	
Shaanxi Heavy Duty Automobile2	
Shandong Hangyu Jili Electronics 	
Shanghai Aerospace Smart Energy Tech 	
Shanghai Aviation Ind  	
Shanghai Dajun Technologies INC4	
Shanghai Daozhi Tech 	
Shanghai Eisdakk Automobile Air Conditioning System Company2	
Shanghai Fuludi Fluid Tech 	
Shanghai Gas Engineering Design & Res 	
Shanghai Iluvatar Corex Semiconductor 	
Shanghai Mengyun Holographic Tech 	
Shanghai Ruizhaote New Energy Tech 	
Shanghai Satake Cool Heat & Control Technique 	
Shanghai Sus Environment 	
Shanghai Xianfang Semiconductor 	
Shanqian Zhuhai Medical Tech 	
Shenyang General Electric Reactor Mfg 	
Shenzhen Auto Electrical High Voltage Electric 	
Shenzhen Chengpeng Electronics 	
Shenzhen Envicool Tech 	
Shenzhen Envicool Tech 	
Shenzhen Haixin Electronic Tech 	
Shenzhen Huaqiang Zhilian Tech 	
Shenzhen Jingxin Semiconductor Seal and Testing 	
Shenzhen Mcquay Air Conditioning 	
Shinwa Controls 	
Shuguang Energy Saving Tech Beijing 	
Sichuan Energy Internet Research Institute of Tsinghua Univ1	
Sichuan Qinhong Electric 	
Sida Xinneng Beijing Energy Saving Tech 	
Siemens Ag1	
Siemens Energy Global Gmbh & Kg2	
Sinatov Stanislav1	
Singapore Lng Corp Pte 	
Sinop Univ Rektorlugu1	
Sk Hynix INC3	
Slon Magnetic Separator Tech 	
Smc Corp2	
Socpra Sciences Et Genie Sec1	
Softbank Corp6	
Songz Automobile Air Conditioning 	
Southwest China Res Inst Electronic Equipment4	
State Grid Corp China2	
State Grid Fujian Electric Power Co2	
State Grid Hebei Electric Power Supply 	
Subaru Corp4	
Sugon Data Infrastructure Innovation Tech Beijing 	
Suixi Power Supply Company of State Grid Anhui Electric Power 	
Sumitomo Electric Industries1	
Sumitomo Wiring Systems1	
Sunonwealth Electric Machine Ind 	
Sunten Electric Equipment 	
Suzhou Blackshields Env 	
Suzhou Blackshields Env 	
Suzhou Inspur Intelligent Tech 	
Suzhou Suqing Safe Issuing Environmental Science and Tech Limited Company2	
Suzhou Tongfu Chaowei Semiconductor 	
Suzhou Zhongrui Hongxin Semiconductor 	
Systemex Energies INC1	
T C Ankara Univ Rektorlugu1	
Taiwan Semiconductor Mfg 	
Technical Inst Physics & Chemistry Cas1	
Technical Inst Physics & Chemistry Cas6	
Technip France1	
Thero New Material Tech 	
Tinless Commercial Power Transf Limited Company1	
Tmgcore LLC1	
Tno3	
Tongfu Microelectronics 	
Toyota Eng & Mfg North America4	
Toyota Ind Corp3	
Toyota Motor 	
Toyota Motor Corp6	
Trane Int INC3	
Tsinghua Tongfang Artificial Env 	
Uchicago Argonne LLC2	
Univ Beihang3	
Univ China Mining & Tech1	
Univ China Petroleum East China1
Univ Dalian Tech12	
Univ Dalian Tech3	
Univ Guangdong Ocean2	
Univ Guilin Electronic Tech4	
Univ Harbin Eng8	
Univ Hubei Minzu1	
Univ Jiangsu Science & Tech1	
Univ Jilin2	
Univ Jilin3	
Univ Kunming Science & Technology3	
Univ Nanjing Science & Tech1	
Univ Science & Technology China1	
Univ Shandong Science & Tech1	
Univ Shandong3	
Univ Shanghai Jiaotong2	
Univ Shanghai Jiaotong2	
Univ Shanghai Jiaotong4	
Univ Shanghai Jiaotong5	
Univ Shanghai Technology2	
Univ Sichuan2	
Univ Sichuan4	
Univ Southwest Jiaotong2	
Univ Tianjin2	
Univ Tongji3	
Univ Tsinghua4	
Univ Tsinghua4	
Univ United Arab Emirates8	
Univ Valencia Politecnica	
Univ Wuhan Tech4	
Univ Xi an Jiaotong3	
Univ Xi an Jiaotong3	
Univ Xi an Jiaotong4	
Univ Xi an Jiaotong5	
Univ Xi an Jiaotong6	
Univ Xian Polytechnic2	
Univ Xidian2	
Univ Zhejiang Technology2	
Univ Zhengzhou2	
Upmem	
Valeo Systemes Thermiques3	
Valeo Systemes Thermiques6	
Vaviri Pty 	
Veck Tianjin 	
Volvo Truck Corp2	
Waertsilae Finland Oy1	
Waertsilae Gas Solutions Norway As1	
Wang Ziyue1	
Wga Water Global Access S L4	
Wga Water Globall Access S L1	
Wieland Provides S R L2	
Wong Lee Wa2	
Wuhu Yijianghaichuang High Tech Intelligent Air Conditioning 	
Wuxi Fangsheng Heat Exchanger 	
Wuxi Honghu Microelectronics 	
Wuxi Laide Tech 	
Wuyi County Daxiang Electronics 	
Xian Inst Optics & Prec Mechanics Cas4	
Xingtai Power Supply Branch of State Grid Hebei Electric Power Co1	
Xinjiang Goldwind Science & Tech 	
Xinjiang Sheng Sheng 	
Yancheng Xinfeng Microelectronic 	
Yangzhou Hongming Electric 	
Yantai Ebara Air Conditioning Equipment 	
Yili Xintian Coal Chemical Ind 	
Yixing Xingyi Special Transf 	
Young in Biotech 
Zhang Kairong3	
Zhao He3	
Zhao Yan3	
Zhao Yaohua3	
Zhejiang Jianxiang 	
Zhejiang Jimaike Microelectronics 	
Zhejiang Jizhi New Energy Automobile Tech 	
Zhejiang King 
Zhejiang Lab7	
Zhejiang Liankong Tech 	
Zhejiang Xp Testing Tech 	
Zhejiang Zeekr Intelligent Tech 	
Zhenghai  	
Zhengxing Hydrogen Electric Tech Zhengzhou 	
Zhiji Automobile Tech 	
Zhongke Thermal Control Fujian Intelligent Tech 
Zhuhai Access Semiconductor 	
Zte Corp	
Zte Corp4	
Zuta Core 
한국가스공사	"""



text = text.replace(" ","")


wordlist = ff.stripNonAlphaNum(text)
fullwordlist = ff.stripNonAlphaNum(text)
wordlist = ff.removeStopwords(fullwordlist, ff.stopwords)
dictionary = ff.wordListToFreqDict(wordlist)
sorteddict = ff.sortFreqDict(dictionary)

# for s in sorteddict: print(str(s))
for s in sorteddict:
    if s[0] >= 1:
        print(str(s))


wordcloud = WordCloud(width=2400, height=3840, background_color='black',
                      prefer_horizontal=1, min_font_size=5).generate(text)

plt.figure('General wordcloud', figsize=(8, 16), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()





