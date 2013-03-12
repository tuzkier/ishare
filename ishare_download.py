import httplib,urllib,urllib2
import os

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


def get_random_file_name():
    return "random"

def get_file_name(url):
    file_name_index = url.find("fn=")
    if file_name_index == -1:
        return get_random_file_name()
    return url[file_name_index + 3:]

def save2disk(url, local_file_name = None):

    file_name = ""
    req = urllib2.Request(url)
    r = urllib2.urlopen(req)
    if local_file_name == None and r.info().has_key('Content-Disposition'):
        # If the response has Content-Disposition, we take file name from it
        localName = r.info()['Content-Disposition'].split('filename=')[1]
        if localName[0] == '"' or localName[0] == "'":
            file_name = localName[1:-1]
    elif local_file_name == None:
        file_name = get_file_name(url)
    if not os.path.exists("downloads"):
        os.mkdir("downloads")
    f = open("downloads/%s" %(file_name.decode("utf-8").encode("gb2312")), "wb")
    f.write(r.read())
    f.close()
    print r


if __name__ == "__main__":
    save2disk()
    #run()
    #login()