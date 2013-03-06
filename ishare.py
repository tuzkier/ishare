#-*- coding:utf-8 -*-

import httplib,urllib

class ishare_client():

    def __init__(self):
        self.cookie = "PHPSESSID=c8e48ba1ed61c47336c4efc9439b0b74; usrmd=usrmdins362; STAT_AB_vdisk=vdisk#A#12eb2fa783cb6834ad708fc3ef336b51#1; ishare_favor=test; U_TRS1=00000034.4b3246a1.510538e3.47d2dbad; U_TRS2=00000034.4b4446a1.510538e3.06d23d4a; UOR=login.sina.com.cn,ishare.iask.sina.com.cn,; Apache=3527444945648.3125.1359296812425; SINAGLOBAL=3527444945648.3125.1359296812425; FSINAGLOBAL=3527444945648.3125.1359296812425; ULV=1359296813941:1:1:1:3527444945648.3125.1359296812425:; SUS=SID-2807797220-1359298050-GZ-i1tkx-533f875d5700e1b9de0e795e98e695fc; SUE=es%3D3f66800f358f6444228cd850fc0ee070%26ev%3Dv1%26es2%3Daa8e53fbee28cbb313e4208b88585a37%26rs0%3DmI%252F4uTjS2qhQzjeWCbfcjyt1BPPQ9uu%252BGAUixVbbs%252FJlJJiflOhKPqDPjLuHuHOS8x9fljwbjImuuPsy%252Fido5gS1rbpLzuPTTo0w3rZ2fX8cOXqy9fdEuutscrzXFu%252FSy9xL9zuSBFljriPTNodShiZjyKmZEEV871ubzISnwV8%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1359298050%26et%3D1359384450%26d%3D40c3%26i%3D95fc%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D2%26lt%3D1%26uid%3D2807797220%26user%3Dvmonit%2540163.com%26ag%3D4%26name%3Dvmonit%2540163.com%26nick%3D%25E6%2588%2591%25E5%25AE%25B6%25E7%259A%2584%25E9%2582%25A3%25E4%25B8%25AA%25E6%2591%2584%25E5%2583%258F%25E5%25A4%25B4%26sex%3D1%26ps%3D0%26email%3D%26dob%3D%26ln%3Dvmonit%2540163.com%26os%3D%26fmp%3D%26lcp%3D; ALF=1361890050; SUR=uid%3D2807797220%26user%3Dvmonit%2540163.com%26nick%3D%25E6%2588%2591%25E5%25AE%25B6%25E7%259A%2584%25E9%2582%25A3%25E4%25B8%25AA%25E6%2591%2584%25E5%2583%258F%25E5%25A4%25B4%26email%3D%26dob%3D%26ag%3D4%26sex%3D1%26ssl%3D0"
        self.base_url = "ishare.iask.sina.com.cn"
        self.down_page_url = "/download.php?fileid="
        self.referer_base = "http://ishare.iask.sina.com.cn/"
        self.connecter = httplib.HTTPConnection(self.base_url)



    def __get_header_with_cookie(self, cookie):
        return {"Referer":self.referer,"Cookie":cookie}

    def __get_header_no_cookie(self):
        return {"Referer":self.referer}

    def search(self, filter):
        pass

    def get_download_url(self,file_id):
        url = self.down_page_url + str(file_id)
        header =  {"Referer":self.referer_base}
        self.connecter.request("POST", url, headers=header)
        res = self.connecter.getresponse()
        locat = res.getheader("location")
        print res.read()
        print locat
        self.download_file(locat)


    def download_file(self, url):
        import ishare_download
        ishare_download.save2disk(url)

    def __get_ishare_download_url(self):
        pass



if __name__ == "__main__":
    ishare = ishare_client()
    ishare.get_download_url(35630056)
