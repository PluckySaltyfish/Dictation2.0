# -*- coding:utf-8 -*-

class phrase():
    def __init__(self,zh,en,test,right,id):
        self.zh = zh
        self.en = en
        self.test = test
        self.right = right
        self.id = id

    def is_true(self,ans):
        res = self.en == ans
        if res:
            self.right += 1
        self.test += 1
        return res

def custom_key(x):
    ans = 0
    if x.test == 0:
        ans += 5
    else:
        if x.test < 10:
            ans += 1 / x.test * 4
        mistake = 1 - x.right/x.test
        ans += mistake
    return ans