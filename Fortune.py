import random
import time
import sys
#magnification_倍率
mag=[17,35,5,4,3,6,30]
mag_hard=[6,10,3,4,5,12,60]
mag_last=[0,0,0,0,0,0,100]
chat_list=['御言葉を信じないなら、おみくじ引く意味もないじゃないですか？','引くかと聞いたのはこちらですが...、いい加減しつこいですよ？','回数引けば大吉が出るかもとか考えてます？そんな都合のいい話はありませんよ。','新年早々こんなものに時間をかけるなんてあなたも物好きですね。']
count=0

def fortune(list):
    global count
    result = random.randint(1,100)
    if (1<=result<=list[1]):
        print('大吉です！')
    elif (list[0]+1 <=result<= list[0]+list[1]):
        print('吉です！')
    elif (list[0]+list[1]+1 <=result<= list[0]+list[1]+list[2]):
        print('半吉です！')
    elif (list[0]+list[1]+list[2]+1 <=result<= list[0]+list[1]+list[2]+list[3]):
        print('小吉です！')
    elif (list[0]+list[1]+list[2]+list[3]+1 <=result<= list[0]+list[1]+list[2]+list[3]+list[4]):
        print('末小吉です！')
    elif (list[0]+list[1]+list[2]+list[3]+list[4]+1 <=result<= list[0]+list[1]+list[2]+list[3]+list[4]+list[5]):
        print('末吉です！')
    elif (list[0]+list[1]+list[2]+list[3]+list[4]+list[5]+1 <=result<= list[0]+list[1]+list[2]+list[3]+list[4]+list[5]+list[6]):
        print('凶です！')
    count += 1

print('新年あけましておめでとうございます。')
print('今年もよろしくお願いいたします。')
time.sleep(3)
print('と、いうわけで浅草寺のおみくじを引こう！')
print('2020年の運勢はいかに...?')
time.sleep(2)
print('おみくじを引いています...')
time.sleep(3)
fortune(mag)
print('引き直しますか？')
print('引き直す：{}  やめておく：{}'.format(0,1))
key = input()
if key=='0':
    print('まさか神様の御言葉を疑っているのですか...?')
    time.sleep(1)
    print('まあいいでしょう、引き直しています...')
    time.sleep(3)
    fortune(mag_hard)
else:
    print('では改めまして、よいお年になりますように。')
    sys.exit()       
print('引き直しますか？')
print('引き直す：{}  やめておく：{}'.format(0,1))
key = input()
if key=='0':
    print('やはり神様を疑っていますね。')
    time.sleep(0.5)
    chat=random.randint(1,4)
    print(chat_list[int(chat)])
    print('引き直しています...')
    time.sleep(3)
    fortune(mag_last)
else:
    print('では改めまして、よいお年になりますように。')
    sys.exit()
while True:
    print('まだ引き直しますか？')
    print('引き直す：{}  やめておく：{}'.format(0,1))
    key = input()
    if key=='0':
        print('やはり神様を疑っていますね。')
        time.sleep(0.5)
        if count==5:
            print('あなたの執着心に敬服いたしました。')
            time.sleep(2)
            print('特別に今年の運気をUPするための方法をお教えしましょう。')
            time.sleep(2)
            print('心がけ:思い通りにならないことがればあまりこだわらずに諦めるが吉')
            time.sleep(1)
            print('これほど引き直すとは思ってもいませんでした。')
            time.sleep(1)
            print('あなたの執着心に敬服いたします。')
            time.sleep(1)
            print('今年も良い年になりますように。')
            sys.exit()
        chat=random.randint(0,3)
        print(chat_list[int(chat)])
        print('引き直しています...')
        time.sleep(3)
        fortune(mag_last)
    else:
        break
print('これほど引き直すとは思ってもいませんでした。')
print('もう少し引いてくれてもよかったんですが...')
print('では改めまして、今年も良い年になりますように。')
