"""
config - 

Author: kayotin
Date 2024/2/28
"""
# 问卷链接
url = "https://www.wjx.cn/vm/P8aop40.aspx"

# 做多少份
epochs = 38
# 题项比例，确保选项数量和数组长度一致
prob = {
    1: [1, 0],
    2: [1, 0],
    3: [1, 0],
    4: [1, 0],
    5: [1, 0],
    6: [1, 0],
    7: [1, 0],
    8: [1, 0],
    9: [1, 0],
    10: [1, 0],
    11: [1, 0],
    12: [1, 0],
    13: [1, 0],
    14: [1, 0],
    15: [1, 0, 0, 0],

}
# 简答题题库
answerList = {
    6: ["123", "12"]
}
# IP API提取链接 https://xip.ipzan.com/ 这个每周都有几百个免费的IP代理领取
api = "https://service.ipzan.com/core-extract?num=1&no=20240228220128183994&minute=10&repeat=1&pool=quality&secret=lqeop7k8is0l12"
# User-Agent库
UA = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
      "Mozilla/5.0 (Linux; Android 10; SEA-AL10 Build/HUAWEISEA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4313 MMWEBSDK/20220805 Mobile Safari/537.36 MMWEBID/9538 MicroMessenger/8.0.27.2220(0x28001B53) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
      "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/045913 Mobile Safari/537.36 V1_AND_SQ_8.8.68_2538_YYB_D A_8086800 QQ/8.8.68.7265 NetType/WIFI WebP/0.3.0 Pixel/1080 StatusBarHeight/76 SimpleUISwitch/1 QQTheme/2971 InMagicWin/0 StudyMode/0 CurrentMode/1 CurrentFontScale/1.0 GlobalDensityScale/0.9818182 AppId/537112567 Edg/98.0.4758.102",
      ]