# Ruaaaaa

## 1.前端
&nbsp;&nbsp;&nbsp;&nbsp;前端的所有文件都写在Template文件夹里头，目前我已经加入了这几个文件（不一定最终就是这样），之后添加文件的话命名方式记得保持一致。

### 前端文件及用途
- RVoteSite.html：面向用户的投票界面
- RDesignSite.html：面向发起者的设计界面
- RManageSite.html：面向管理者的管理界面
- RBackground.html：统一的页面背景格局（或者改成CSS，可以再商榷，而且我不知道HTML是不是可以互相调用。。）
- RQuestionTab.html：各种问题框的设计，可以继续下分，也可以考虑写成CSS


## 2.前后端通信

&nbsp;&nbsp;&nbsp;&nbsp;前后端的通信目前一共分为这么几点：

### POST请求
- POST VoteSubmit：提交一份问卷/投票
		具体格式：
- POST CreatePoll：产生了一份问卷/投票
		具体格式：
- POST ChangePollState：在管理界面对问卷/投票的状态进行了更改
		具体格式：

### GET请求
- GET ManageSite：寻求管理界面
		具体格式：
- GET VoteSite：寻求投票界面
		具体格式：

## 3.后端
&nbsp;&nbsp;&nbsp;&nbsp;所有后端都写在Kernal里头，写后端的自己补充吧。。。。
