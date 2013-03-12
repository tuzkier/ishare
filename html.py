#coding:utf-8
from sgmllib import SGMLParser

class search_result(SGMLParser):
    base_url = "http://ishare.iask.sina.com.cn"
    def reset(self):
        self.url_list = []
        self.flag = False
        self.can_getdata = False
        self.can_get_test = False
        self.verbatim = 0
        SGMLParser.reset(self)

    def start_div(self, attrs):
        for k, v in attrs:
            if k == "class" and v == "cb":
                self.can_getdata = True
    def end_div(self):
        if self.can_getdata:
            self.can_getdata = False

    def start_a(self, attrs):
        if not self.can_getdata:
            return
        for k, v in attrs:
            if k == "href":
                self.can_get_test = True
                self.url_list.append({"url":self.base_url + v})

    def end_a(self):
        self.can_get_test = False

    def handle_data(self, text):#处理文本
        if self.can_getdata and self.can_get_test:
            self.url_list[-1]["text"] = text

    def show_result(self):
        for u in self.url_list:
            print u["text"] + ":" + u["url"]
