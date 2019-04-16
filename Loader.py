# coding=utf-8
class loader():
    def __init__(self):
        self.phrase = []
        self.len = []
        try:
            with open('config') as config:
                self.phrase = config.readline().rstrip('\n ').split()[1:]
                self.record = [x + '_rcd' for x in self.phrase]
        except Exception:
            print('配置文件错误！')
            exit()

    def load_phrase(self):
        if len(self.phrase) == 0:
            return -1
        size = 0
        en = []
        zh = []
        for i in self.phrase:
            with open(i, encoding='UTF-8') as f:
                cnt = 0
                for each_line in f:
                    each_line = each_line.rstrip('\n ')
                    if not each_line.find(' -') == -1:
                        (en_part, zh_part) = each_line.split(' -')
                        en.append(en_part)
                        zh.append(zh_part)
                        cnt += 1
                self.len.append(cnt)
                size += cnt
        print("\033[37m一共导入了\033[34m", size, "\033[37m条词组")
        return zh, en

    def load_record(self):
        test_times = []
        right_times = []
        record = self.record
        for i in range(len(record)):
            try:
                line = 0
                with open(record[i]) as f:
                    for each_line in f:
                        s = each_line.rstrip('\n ')
                        if len(s) != 0:
                            t, r = s.split()
                            test_times.append(int(t))
                            right_times.append(int(r))
                            line += 1
                while line < self.len[i]:
                    line += 1
                    test_times.append(0)
                    right_times.append(0)

            except FileNotFoundError:
                with open(record[i], 'w') as f:
                    for j in range(self.len[i]):
                        f.write('0 0\n')
                        test_times.append(0)
                        right_times.append(0)

        return test_times, right_times

    def store_record(self, test, right):
        rcd = self.record
        last = 0
        for i in range(len(rcd)):
            with open(rcd[i], 'w') as f:
                for j in range(self.len[i]):
                    f.write('%s %s\n' % (test[last + j], right[last + j]))
                last += self.len[i]

