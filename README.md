<div align="center">
    <h1 align="center">wechat-public-account-push</h1>

[![GitHub Stars](https://img.shields.io/github/stars/JsonMs/wechat-live-push?style=flat)](https://github.com/JsonMs/wechat-live-push/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/JsonMs/wechat-live-push?style=flat)](https://github.com/JsonMs/wechat-live-push/network/members)
[![GitHub Issues](https://img.shields.io/github/issues/JsonMs/wechat-live-push?style=flat)](https://github.com/JsonMs/wechat-live-push/issues)

</div>

**本项用于学习微信测试号给用户推送每日元气播报，让每天都是元气满满的一天🎉**

**如果这个项目很有意思，帮忙右上角点个 star✨**

**如果有任何需要帮助可以提[issues](https://github.com/JsonMs/wechat-live-push/issues)**


# 推送成果
<img width="400" height="600" src="https://github.com/JsonMs/wechat-live-push/assets/50287117/3a1e22ac-4389-44ee-811e-6e00585da18c"/>

# 准备工作
1.微信公众号接口测试账号[申请](https://github.com/JsonMs/wechat-live-push/assets/50287117/3a1e22ac-4389-44ee-811e-6e00585da18c)

拿到appId、appsecret、userId、templateId
<img width="1078" alt="image" src="https://github.com/JsonMs/wechat-live-push/assets/50287117/077738e1-2fb4-4ed3-86ef-982c16755cbf">
<img width="1095" alt="image" src="https://github.com/JsonMs/wechat-live-push/assets/50287117/5d8179c4-a83a-452e-8832-ed66f657b5e4">
<img width="1098" alt="image" src="https://github.com/JsonMs/wechat-live-push/assets/50287117/b6f08206-7857-4614-b4dd-b90b5659e58b">

2.申请和风天气密钥[控制台](https://console.qweather.com/#/console)

拿到weatherKey
<img width="1621" alt="image" src="https://github.com/JsonMs/wechat-live-push/assets/50287117/1fd4a62e-b3be-4928-81c2-f0bd45957988">

3.申请天行数行[控制台](https://www.tianapi.com/console/)
<img width="1245" alt="image" src="https://github.com/JsonMs/wechat-live-push/assets/50287117/0447293b-388f-48cd-815b-d34cfca2cb11">

# 如何部署

1.Fork到本地仓库
<img width="1602" alt="image" src="https://github.com/JsonMs/wechat-live-push/assets/50287117/7562aed8-53c8-44ff-9300-da715ca95e1c">

2.配置定时任务的需要的密钥，可参照本代码配置自行配置
<img width="1500" alt="image" src="https://github.com/JsonMs/wechat-live-push/assets/50287117/bfebe4ff-1afe-47a7-b711-6f855c7959eb">

3.设置定时任务时间

目前脚本默认执行时间为**每天的 北京时间上午 07:30**

⚠️ 代表国际标准时间4点0分，北京时间需要+8小时，代表北京时间中午12点运行
<img width="1026" alt="image" src="https://github.com/JsonMs/wechat-live-push/assets/50287117/1325b5f7-d880-4ae6-911f-1d7fa4eb6419">

🪁 可使用https://crontab.guru帮助配置
![image](https://github.com/JsonMs/wechat-live-push/assets/50287117/ce6f3921-5921-4411-8815-54527420383c)


4.最后运行
<img width="1666" alt="image" src="https://github.com/JsonMs/wechat-live-push/assets/50287117/437ef4d0-9f74-459b-ab9c-09b94003bbd1">

