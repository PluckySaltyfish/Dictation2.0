#!/Users/plucky/Plucky/Python/venv/bin/python
# coding=utf-8
import Loader
import phrase
import random

def dictate():
    # load
    loader = Loader.loader()

    res = loader.load_phrase()
    if res == -1:
        print('短语表为空！')
        exit()
    zh, en = res
    test, right = loader.load_record()
    # generate
    phrz_lst = []
    for i in range(len(zh)):
        phrz = phrase.phrase(zh[i], en[i], test[i], right[i], i)
        phrz_lst.append(phrz)

    random.shuffle(phrz_lst)
    phrz_lst = sorted(phrz_lst, key=phrase.custom_key,reverse=True)

    print("输入要测试的词组数量：\033[34m")
    try:
        lines = int(input())
        while not (lines > 0 and lines < len(zh) + 1):
            print("\033[37m输入范围内数字！")
            print("输入要测试的词组数量：\033[34m")
            lines = int(input())
        phrz_lst = phrz_lst[:lines]
        random.shuffle(phrz_lst)

        print("\n\033[32m--start--\033[37m")
        cnt = 0
        wrong = []
        ans = []
        for i in phrz_lst:
            print("\n\033[0m%s\033[34m"%(i.zh))
            answer = input().rstrip()
            if not i.is_true(answer):
                cnt += 1
                wrong.append(i)
                ans.append(answer)

        print("\n\033[32m--end--\033[37m")

        grade = 100 * (1 - cnt / lines)
        print("\n\033[37m最终成绩：\033[32m %.2f"%grade)

        if not len(wrong) == 0:
            print("\033[31m错误：")

        for i in range(len(wrong)):
            print("\033[37m%s\t\033[32m%s"%(wrong[i].zh,wrong[i].en))
            print("\033[37mYour answer:\t\033[31m",ans[i])

        print('\033[0m')

        for i in phrz_lst:
            test[i.id] = i.test
            right[i.id] = i.right
        loader.store_record(test,right)

    except ValueError:
        print("\033[37m输入数字！")

    except KeyboardInterrupt:
        print('\n\033[34mBye~')


if __name__ == '__main__':
    dictate()
