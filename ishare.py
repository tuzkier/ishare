#-*- coding:utf-8 -*-

import httplib,urllib
from html import search_result
class ishare_client():

    def __init__(self):
        self.cookie = ""
        self.base_url = "ishare.iask.sina.com.cn"
        self.search_url = "http://ishare.iask.sina.com.cn/search.php?key=%s&format=%s"
        self.down_page_url = "/download.php?fileid="
        self.referer_base = "http://ishare.iask.sina.com.cn/"
        self.connecter = httplib.HTTPConnection(self.base_url)


    def __get_header_with_cookie(self):
        return {"Referer":self.referer,"Cookie":self.cookie}

    def __get_header_no_cookie(self):
        return {"Referer":self.referer}

    def reset_cookie(self):
        self.connecter.request("GET",self.referer_base)
        res = self.connecter.getresponse()
        header_list = res.getheaders()
        for header in header_list:
            if header[0] == "set-cookie":
                self.cookie = header[1]
        print res.getheaders()
        print self.cookie

    def search(self, filter, type=""):
        self.reset_cookie()
        if filter == None or filter == "":
            return
        header =  {"Referer":self.referer_base,"Cookie":self.cookie}
        self.connecter.request("GET", self.search_url %(filter, type), headers=header)
        print self.search_url %(filter, type)
        res = self.connecter.getresponse()
        r = res.read()
        #print r
        return r


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
    #ishare.reset_cookie()
    result = ishare.search("test","pdf")
    r = search_result()
    r.feed(result)
    r.show_result()
    #ishare.get_download_url(35630056)
