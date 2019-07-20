# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 20:01:14 2019

@author: RAJARAJESHWARI
"""

import nltk
import xlsxwriter
import xlrd
from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))
workbook = xlsxwriter.Workbook(r'D:\PAPERS\raji\100_excel.xlsx') 
worksheet = workbook.add_worksheet()
file=open(r'D:\PAPERS\raji\100.txt','rt',encoding="utf8")
file2=open(r'D:\PAPERS\raji\100_modified.txt','wt',encoding="utf8")
f=file.readlines()

end='EOF'

for i in f:
    if i in ['\r\n','\n']:
     print(end,file=file2)

    else:
     print(i,file=file2)
     
file.close()
file2.close()

deletelist=["2011","2014","plays","35","100","400","2015","113","28","11","500","49","34","us","72","7th","h","34","14","assess","fraction","objective","factor","used","use","chronic","red","wine","treat","form","mechanism","remain","renewed","morbidity","Background","attenuated","moratlity","prevent","Type","aims","observation","population","Algerian","describe","behaviour","fundamental","feature","constraint","features","constraints","test","ususlly","burden","elusive",'hyperglycemia','diabetes',"clinics","excercise","benefits","benefit","monitoring","presenting","unclear","remains","main","death","types","901","836","leaf","indica","extracts","therapy","avoided","widely","used","continuous","analysis","exceeding","126",'type',"major","human","assessing","G","142","reason","millions","complicated","issues","relative",'OBJECTIVE','large','diagosed','diagnose',"used","unit",'1972','This','daily','Institute',"12","A",'Therefore','evidence','define','Americans','continues','strategy','review','defined','obtain','We','proposes','reference','For','article','Beach','3','26','The','In','45','1860','2','While','4','three','10','Very','overall','There','diagnosis','There','Today','1860','South','130','recently','partner','partners',"'",'"',"schedule","scheduled","schedules","took","neck","iui","trigger","eat","grain",'whole','quit','smoke','possible','possibilities','possibility','happen','took','taken','face','pound','light','remove','removed','30','40','lefts','left','two','13','2ww','food','meal','pap','smear','endocrinologist','reproduction','cm','temp','line','thick','lost','recent','chart','wii','fit','cut','situations','situation','peoples','people','situated','saw','situation','next','step','bad','hurt','line','appointment','appointed','minute','minutes','-',"'",'happy','happiness','sad','many','related','specialist','appt','dr','improve','improved','improves','refer','refers','glass','wedding','marriage','married','news','exciting','excited','found','scale','number','tuesday','result','forever','final','thought','term','manage','nature','change','track','fire','turbo','appreciate','appreciated','thank','thanks','bed','rest','sex','drive','soul','cyster','fun','little','give','inform','everyday','nothing','clear','use','book','read','shave','done','crave','craving','sweet','insurance','pay','paid','whatever','find','cover','sure','drill','cry','cried','crying','tear','tears','dinner','breakfast','site','names','name','fun','little','actual','ok','find','finds','whatever','pay','give','inform','develop','fine','yesterday','surprise','surprises','actually','done','excited','super','arm','unprotected','unprotect',"0.0",'rollers','everything','god','trust','count','ask','question','soulcysters','boys','boy','girls','girl','away','pass','fridays','saturdays','sunday','sundays','post','thread','class','school','due','date','play','trick','live','life','least','dont','doesnt','bless','keep','prayer','great','fiance','background','never','site','coaster','roller','comment','post','plans','planning','plan','friday','saturday','buys','buy','around','luck','wish','try','tried','way','breakfast','lunch','dinner','buy','cancel','comment','however','god','faith','job','area','come','son','boy','girl','boyfriend','breakfast','lunch','dinner','alright','amount','decide','baby','babies','angel','apart','april',"0.0",'10am','1st','2nd','2005','advice','advise','alone','along','alot','still','fingers','finger','crossed','cross','anyone','everyone','anything','january','september','october','week','month','polycyst','syndrome','syndrom','shot','doctor','wanna','wan','na','born','morning','morn','woke','every','single','singl','night','hello','doctor','tried','try','right','2008','2009','not',"n't",'anyone',"'ll",'favorite','week','motiv','oh','well','wait','take','pcos','pco','say','think','round','first','something','december','decemb','month','gonna','ndividual.asp','favourite','share','without','help','could','put','website','call','friend','came','better','make','work','good','leader','thing','really','load','','need','long','info','nature','please','look','said','went','even','though','today','anyone','else','side','want','blog','always','bottle','also','back','new','august','know','start','stop','told','want','got','families','family','lol','7/3-7/4',"n't",'video','may','2013','2016','-','ago','last','2007', 'since','manage', 'gid=54257','individual.asp', 'www.sparkpeople.com/myspark/groups_i','af', 'day', 'see','ca', 'day', 'go','husband','almost', 'feel', 'like','go', 'much', 'see','old', 'year','day', 'get', 'hope', 'time',"im","i've","hi,",'abl',"can't", 'one',",","-","3","1","2","4","5","6","7","8","9","10","i'v","\n","one...so","i'd","'d",'nan','jan','feb','mar','apr','you','hi','have','was',"'ve","'m",'would','will','are','were','n','not','be','http','your','coz','don',"'s",'had','it','am','we','on',"i'm","i","...","its","it's","me",'\ni', '(06:44)','be','some','to','have','has','with','to','out','be','www.mypcos.info',"BACKGROUND","CONCLUSION","CONCLUSIONS","Furthermore","Here","However","METHODS","Moreover","Our","RESULTS","These","To","administration","aim","aimed","either","fed","functions","Diabetes","since","OBJECTIVES","substantially","place","important","development","T2D","compared","significantly","studies","using","significant","associated","treatment","metabolic","effect","role","development","diabetic","mechanism","induced","fully","understood","Glucose-6-phosphate dehydrogenase","G6PD","critical","maintaining","NADPH","cofactor","antioxidant","system","Here", "we", "hypothesized","ubiquitination", "degradation","injured","podocytes","reactive", "oxygen", "species", "(ROS)", "accumulation","expression","both", "patients", "rodents","activity","mice","rats","rat", "Overexpressing","reversed", "redox","imbalance","apoptosis", "palmitate","Inhibition","small", "interfering", "RNA", "podocyte","apoptosis","G6PD-deficient", "Interestingly", "mRNA","expression","mediated","ubiquitin","proteasome", "pathway", "We", "found", "von Hippel-Lindau (VHL) protein","E3","ubiquitin", "ligase","subunit", "directly", "bound","ubiquitylating", "K366","K403", "summary", "our", "data","suggest","induces","VHL E3 ubiquitin ligase","leads", "ROS accumulation","-Wang, M., Hu, J., Yan, L., Yang, Y., He M., Wu, M., Li, Q., Gong, W., Yang, Y., Wang, Y., Handy, D. E., Lu, B., Hao, C., Wang, Q., Li, Y., Hu, R., Stanton, R. C., Zhang, Z","contributes","predit","current","study","determine","effects","responses","factors","contributions","pathways","effects","examined","studied","changes","although","Although","demonstration","enhancement","augumented","response","alteration","result","results","compensation","T2DM","urgent","established","protocol","European","joint","consensus","Beacuse","inhibition","AND","rates","care","agree","often","present","several","natural","discussions","content","among","future","target","targeting","live","explore","link","comprised","management","among","various","carried","January","Febrary","March","April","May","June","July","August","September","October","November","December","month","verify","whether","state","flash","several","including","Within","purpose","trait","based","Prussian","Blue","Green","Red","years","year","bark","mouse","record","clinic","Denmark","Washington","With","PAID","primarily","Patients","Aim","AIM","AIMS","novel","aggravtion","BAT","Little","little","known","Known","T","It","fueled","HYPERGLYCEMIA","Hyperglycemia","Since","since","15","50","2017","2018","invloved","principle","key","aged","age","20","65","white","rice","barley","principal","Several","II","arises","basis","might","diverse","Recent","shown","occurs","expansive","checkpoint","frequency","characterized","elevated","assumed","552","370","2030","de","nono","novo","Recently","DR","recently","TYPE","closely","linked","link","reported","pioneering","Both","regulate","comman","man","His","via","CAD","surgical"]
               

f2=open(r'D:\PAPERS\raji\100_modified.txt','rt',encoding="utf8")
filee2=open(r'D:\PAPERS\raji\100_modified_2.txt','wt',encoding="utf8")
f1=f2.read()
s=[]
tokens=nltk.word_tokenize(f1)
for i in tokens:
    if i.isalnum()==True and i not in stop_words:
        if i not in deletelist:
            s.append(i)
    
r=1
c=1

for o in s:
 if o not in['EOF']:
  worksheet.write(r,c,o)
  filee2.write(o+" ")
  c=c+1
 else:
  r=r+2
  c=1
print("end")
filee2.close()
workbook.close()