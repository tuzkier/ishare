import httplib

def run():
    conn = httplib.HTTPConnection("ishare.iask.sina.com.cn")
    #http://ishare.iask.sina.com.cn/download/explain.php?fileid=35590273
    cookies= "SINAGLOBAL=00000025.61e02c4e.4f7e85ab.8ca527d1; U_TRS1=00000025.709640c2.5100fe00.5edf796b; PHPSESSID=eea954af4cef677e20d3514f2da092b3; U_TRS2=00000025.e4b14ffb.5101f161.a452b429; STAT_AB_vdisk=vdisk#A#32c0259444b278f9ae07e1210cc53030#1; UOR=login.sina.com.cn,ishare.iask.sina.com.cn,; Apache=3945132980588.8237.1359081827903; FSINAGLOBAL=00000025.61e02c4e.4f7e85ab.8ca527d1; ULV=1359081831002:1:1:1:3945132980588.8237.1359081827903:; ishare_ifdown_35590600=1; ishare_ifdown_35594553=1; SUS=SID-2807797220-1359100463-GZ-3zf9g-fa2362360978ce4e19857b481197de2e; SUE=es%3D93e654924ba008c16c4038ccc7b62ee5%26ev%3Dv1%26es2%3D867eb97b8cc2491341376b41f1be9ade%26rs0%3DvSn1epSM%252FrzlWRYRII%252BtouL0QjgXFeUxP0QbEXPsTaBp2y%252BnglkCqEFMVdCJJxyxFrVplYmTHDuriHLX2qI21UFRQDJaoSV%252Fx73X1CaiTm56Bj72J0T65Cv5Qr0boDDZUPOgTINXq69eUCYYJFupnP82h0hs9E%252BB4CfbOGRbwDY%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1359100463%26et%3D1359186863%26d%3D40c3%26i%3Dde2e%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D2%26lt%3D1%26uid%3D2807797220%26user%3Dvmonit%2540163.com%26ag%3D4%26name%3Dvmonit%2540163.com%26nick%3D%25E6%2588%2591%25E5%25AE%25B6%25E7%259A%2584%25E9%2582%25A3%25E4%25B8%25AA%25E6%2591%2584%25E5%2583%258F%25E5%25A4%25B4%26sex%3D1%26ps%3D0%26email%3D%26dob%3D%26ln%3Dvmonit%2540163.com%26os%3D%26fmp%3D%26lcp%3D; usrmd=usrmdins3100"

    headers = {"Referer":"http://ishare.iask.sina.com.cn","Cookie":cookies}
    conn.request("POST","/download.php?fileid=35594557",headers = headers)
    res = conn.getresponse()
    resheaders = res.getheaders()
    print resheaders
    print resheaders[9]
    conn.close()

def login():
    conn = httplib.HTTPConnection("ishare.iask.sina.com.cn")

    cookies = "SINAGLOBAL=00000025.61e02c4e.4f7e85ab.8ca527d1; U_TRS1=00000025.709640c2.5100fe00.5edf796b; U_TRS2=00000025.e4b14ffb.5101f161.a452b429; UOR=login.sina.com.cn,ishare.iask.sina.com.cn,; Apache=3945132980588.8237.1359081827903; FSINAGLOBAL=00000025.61e02c4e.4f7e85ab.8ca527d1; ULV=1359081831002:1:1:1:3945132980588.8237.1359081827903:"
    headers = {"Cookie":cookies,"Referer":"http://ishare.iask.sina.com.cn/login/login_div.php?w=400&h=230&url=%2Fishare%2Fbrowse_file.php%3Ffileid%3D35594553&msg=%B8%C3%D7%CA%C1%CF%D0%E8%D2%AA%B5%C7%C2%BC%BA%F3%D6%A7%B8%B6+2+%B7%D6%3Ca+href%3D%22%2Fhelp%2Fjfgz.html%22+target%3D%22_blank%22%3E%BB%FD%B7%D6%3C%2Fa%3E%B2%C5%C4%DC%CF%C2%D4%D8"}
    conn.request("GET","/login/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack&sudaref=ishare.iask.sina.com.cn&retcode=101&reason=%B5%C7%C2%BC%C3%FB%BB%F2%C3%DC%C2%EB%B4%ED%CE%F3",headers=headers)
    res = conn.getresponse()
    print res.read()
if __name__ == "__main__":
    run()
    #login()