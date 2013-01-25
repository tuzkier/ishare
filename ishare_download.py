import httplib,urllib

def run():
    conn = httplib.HTTPConnection("ishare.iask.sina.com.cn")
    #http://ishare.iask.sina.com.cn/download/explain.php?fileid=35590273
    cookies= "SINAGLOBAL=00000025.61e02c4e.4f7e85ab.8ca527d1; U_TRS1=00000025.709640c2.5100fe00.5edf796b; PHPSESSID=eea954af4cef677e20d3514f2da092b3; STAT_AB_vdisk=vdisk#A#32c0259444b278f9ae07e1210cc53030#1; UOR=login.sina.com.cn,ishare.iask.sina.com.cn,; Apache=3945132980588.8237.1359081827903; FSINAGLOBAL=00000025.61e02c4e.4f7e85ab.8ca527d1; ULV=1359081831002:1:1:1:3945132980588.8237.1359081827903:; ishare_ifdown_35590600=1; ishare_ifdown_35594553=1; usrmd=usrmdins363; U_TRS2=0000004f.6d2c5186.5101f5f5.61978b03; SUS=SID-2807797220-1359104582-GZ-u62je-168c3c118017e98c00e61c73dd42bac6; SUE=es%3Df6299e11a0b61e8e3ecd5ca948735e9e%26ev%3Dv1%26es2%3D3b78d77c092b858d7b66805980868aa9%26rs0%3DPeqmmfSvvc33pZYqHzQjsubAnSLq6NtQsiBLEoKGu6dcZ%252F2XOcY0V4IyDdotklBa6KFO6BGjVKTj6jzfcy6xUwDDZ6PeiGG01HLVnzSS8cbXsTMfKA0AfwMg0qh86TLuIvihjvNRfIe27HaHmAb5yNluagVA8Ls12r4%252FCfYOBZg%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1359104582%26et%3D1359190982%26d%3D40c3%26i%3Dbac6%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D2%26lt%3D1%26uid%3D2807797220%26user%3Dvmonit%2540163.com%26ag%3D4%26name%3Dvmonit%2540163.com%26nick%3D%25E6%2588%2591%25E5%25AE%25B6%25E7%259A%2584%25E9%2582%25A3%25E4%25B8%25AA%25E6%2591%2584%25E5%2583%258F%25E5%25A4%25B4%26sex%3D1%26ps%3D0%26email%3D%26dob%3D%26ln%3Dvmonit%2540163.com%26os%3D%26fmp%3D%26lcp%3D; ALF=1361696582; SUR=uid%3D2807797220%26user%3Dvmonit%2540163.com%26nick%3D%25E6%2588%2591%25E5%25AE%25B6%25E7%259A%2584%25E9%2582%25A3%25E4%25B8%25AA%25E6%2591%2584%25E5%2583%258F%25E5%25A4%25B4%26email%3D%26dob%3D%26ag%3D4%26sex%3D1%26ssl%3D0"

    headers = {"Referer":"http://ishare.iask.sina.com.cn","Cookie":cookies}
    conn.request("POST","/download.php?fileid=35595998",headers = headers)
    res = conn.getresponse()
    print res.read()
    resheaders = res.getheaders()
    print resheaders
    for r in resheaders:
        if r[0] == "location":
            print r[1]
    conn.close()

def login():
    conn = httplib.HTTPConnection("ishare.iask.sina.com.cn")

    cookies = "SINAGLOBAL=00000025.61e02c4e.4f7e85ab.8ca527d1; U_TRS1=00000025.709640c2.5100fe00.5edf796b; U_TRS2=00000025.e4b14ffb.5101f161.a452b429; UOR=login.sina.com.cn,ishare.iask.sina.com.cn,; Apache=3945132980588.8237.1359081827903; FSINAGLOBAL=00000025.61e02c4e.4f7e85ab.8ca527d1; ULV=1359081831002:1:1:1:3945132980588.8237.1359081827903:"
    headers = {"Cookie":cookies,"Referer":"http://ishare.iask.sina.com.cn/login/login_div.php?w=400&h=230&url=%2Fishare%2Fbrowse_file.php%3Ffileid%3D35594553&msg=%B8%C3%D7%CA%C1%CF%D0%E8%D2%AA%B5%C7%C2%BC%BA%F3%D6%A7%B8%B6+2+%B7%D6%3Ca+href%3D%22%2Fhelp%2Fjfgz.html%22+target%3D%22_blank%22%3E%BB%FD%B7%D6%3C%2Fa%3E%B2%C5%C4%DC%CF%C2%D4%D8"}
    conn.request("GET","/login/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack&sudaref=ishare.iask.sina.com.cn&retcode=101&reason=%B5%C7%C2%BC%C3%FB%BB%F2%C3%DC%C2%EB%B4%ED%CE%F3",headers=headers)
    res = conn.getresponse()
    print res.read()


def save2disk():
    conn = httplib.HTTPConnection("ishare.iask.sina.com.cn")
    cookies = "UOR=www.google.com.hk,blog,; vjuids=cd3a11d25.137a65e6a3a.0.635c0bf5; ALLYESID4=0012060112471535134536; mvsign=v%3DN%28ST%2A%23R%60I2A%5E6%5BV%40iBu5; FSINAGLOBAL=00000025.b4215d8f.4fc8267b.f3fa0ff6; SINAGLOBAL=00000043.2eb3db0.50889ec1.8fa3fcd3; SINA_NEWS_CUSTOMIZE_city=%u676D%u5DDE; aesurveynum480=3; aesurveynum487=2; lxlrtst=1354869250_o; STAT_AB_vdisk=vdisk#A#e6029f57096daef66a721ccbe34805c2#1; U_TRS2=00000011.6d0c4961.5100c735.5ff591c7; Apache=00000016.34f52860.5100c74f.6691b7ad; SessionID=b20q1i381ct4qok19h3q5kolq1; ; PHPSESSID=c74c9fece81e0cd95746c3edbaf37ac2; usrmd=usrmdins169; ishare_ifdown_35590288=1; cookie_download_tag=415621793; ishare_ifdown_35590273=1; ishare_ifdown_35590189=1; ishare_ifdown_35590182=1; ishare_ifdown_35590960=1; ishare_ifdown_35590600=1; ULV=1359083988393:106:7:3:00000016.34f52860.5100c74f.6691b7ad:1358819871847; vjlast=1359083995; ArtiFSize=14; lxlrttp=1359068396; U_TRS1=00000028.81da2a3f.51010d11.45737080; ULOGIN_IMG=gz-7f458d6642708898f3f8687b8ba8176f8703; SUS=SID-1688520453-1359105078-GZ-f7bth-fd1e3607fee57a9c5d26337e6414de2e; ALF=1361697078; SUR=uid%3D1688520453%26user%3Dwhb4d12%2540gmail.com%26nick%3Dtuzkier%26email%3D%26dob%3D1989-7-20%26ag%3D4%26sex%3D1%26ssl%3D0; SUE=es%3D3247fdd0db5aeb8d56b6b1336dff90d1%26ev%3Dv1%26es2%3D4c347b130b4c8c133883f9ed2cd7b8f4%26rs0%3DshIcUdHB2X3e2wrf0%252BgToLLdVoW1bqVsfcYWbg7lWOE1PoOnL6Tjzp0EQECWxYycoICJUgCQkfAGtzny2efS9CNGK1boQIcEhiwlMzIuOfs%252B1Wvu4w26dQdS0Is3Ls1Fj5gu73lvAWIv1%252BlNj5uNvTBJjPpDSYbmvvVX6brwH84%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1359105078%26et%3D1359191482%26d%3D40c3%26i%3Dbac6%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D0%26lt%3D1%26uid%3D1688520453%26user%3Dwhb4d12%2540gmail.com%26ag%3D4%26name%3Dwhb4d12%2540gmail.com%26nick%3Dtuzkier%26sex%3D1%26ps%3D0%26email%3D%26dob%3D1989-7-20%26ln%3D%26os%3D%26fmp%3D%26lcp%3D2011-06-30%252023%253A55%253A24"

    param = urllib.urlencode({'fileid': '35595908'})
    header = {"Cookie":cookies,"Referer":"http://ishare.iask.sina.com.cn/f/35596299.html","X-Requested-With":"XMLHttpRequest","Content-Length":"15","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Accept":"*/*","        Accept-Charset/":"GBK,utf-8;q=0.7,*;q=0.3","Accept-Encoding":"gzip,deflate,sdch","Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4"}
    conn.request("POST","/vdisk/savevdisk.php?action=save",param, headers=header)
    res = conn.getresponse()
    print res.read()

    cookies2 = "lzstat_uv=5939562481280418154|2893156; saeut=202.91.247.37.1343355140609251; CNZZDATA3212592=cnzz_eid=46435862-1345782021-http%253A%252F%252Fweibo.com%252Ftuzkier&ntime=1346044918&cnzz_a=0&retime=1346044924509&sin=http%253A%252F%252Fweibo.com%252Ftuzkier&ltime=1346044924509&rtime=1; __utma=15428400.1429628126.1357615037.1357615037.1357615037.1; __utmz=15428400.1357615037.1.1.utmcsr=blog.sina.com.cn|utmccn=(referral)|utmcmd=referral|utmcct=/s/profile_1534596801.html; _s_tentry=login.sina.com.cn; Apache=95913929399.10292.1359005512055; ULV=1359005512063:109:25:6:95913929399.10292.1359005512055:1358991715905; SINAGLOBAL=95913929399.10292.1359005512055; un=whb4d12@gmail.com; WBStore=9a5f4a8352d9b9c1|; SSOLoginState=1359105078; SUE=es%3D9d83229b195859910c43548b17e12442%26ev%3Dv1%26es2%3D77779e2c3be7ceb28724412a4c56056f%26rs0%3DiZd3YukaROmOBktEeh%252FGQgvdsbWx5H4ol56XPiGBYzauFXD0424LqeQDJ5Ub7IE7MPSIDqjG2zHhVg1JF9RQN1DO4b22PoQPHhw%252FvdPFKR6%252B31e8GujS4BCZrT2kmjFl2BB9GpzER8%252FvzHGZAK8q0viYmwhujkHCqif1Rci7ofU%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1359105084%26et%3D1359191484%26d%3Dc909%26i%3D06c1%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D2%26uid%3D1688520453%26user%3Dwhb4d12%2540gmail.com%26ag%3D4%26name%3Dwhb4d12%2540gmail.com%26nick%3Dtuzkier%26fmp%3D%26lcp%3D2011-06-30%252023%253A55%253A24; SUS=SID-1688520453-1359105084-JA-xiz9j-d3216c014a92edd958f3323315d0bac6; ALF=1361697078; v=5; wvr=5; __utma=18712062.1377118063.1359105049.1359105049.1359105049.1; __utmb=18712062.5.10.1359105049; __utmc=18712062; __utmz=18712062.1359105049.1.1.utmcsr=ishare.iask.sina.com.cn|utmccn=(referral)|utmcmd=referral|utmcct=/f/35596299.html; UOR=weibo.com,weibo.com,#ishare.iask.sina.com.cn"
    conn2 = httplib.HTTPConnection("vdisk.weibo.com")
    header = {"Cookie":cookies2,"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
    conn2.request("GET","/file/info?fid=412045498",headers=header)
    res2 = conn2.getresponse()
    print res2.read()


if __name__ == "__main__":
    save2disk()
    #run()
    #login()