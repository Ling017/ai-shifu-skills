# 付款和开通

当用户已经选择套餐，或询问“怎么付款、买了之后谁服务”时使用。

## 付款页面

Users can pay directly in the backend billing package page:

`https://app.ai-shifu.cn/admin/billing?tab=packages`

## 标准付款话术

```text
可以，套餐可以直接在后台积分套餐页面付款：
https://app.ai-shifu.cn/admin/billing?tab=packages
付款后会有负责人跟进服务。月套餐会进入全部用户服务群，年套餐会有团队专属服务群，后续会继续带你把课程做起来。
```

## 服务群规则

| 套餐类型 | 服务安排 | 解释方式 |
|---|---|---|
| 月套餐 | 全部用户服务群 | 适合个人/小团队先跑通课程，有服务群承接基础问题 |
| 年套餐 | 团队专属服务群 | 适合机构/企业/团队持续使用，会有团队专属服务群跟进 |

## 付款后检查清单

Update collaboration record immediately:

`用户, 套餐, 付款状态, 付款时间, 服务群类型, 负责人, 是否已发课程创作指导课, 第一门正式课主题, 下次跟进时间`

Then do these actions:

1. Confirm payment/package in backend or with responsible person.
2. Tell user a responsible person will follow up service.
3. Invite user to the correct service group: 月ly all-user group or yearly dedicated team group.
4. 发送购买后课程创作指导课： `http://app.ai-shifu.cn/c/57b5dd9f3bb6478683ef7674403cefa4`.
5. Ask user to confirm the first official course material/topic.
6. Set the 3-day and 7-day customer success follow-up.

## 付款后开通话术

```text
已经收到你的开通信息。接下来先把第一门正式课跑通：
1）我先发你课程创作指导课；
2）你确定第一份要做的资料/主题；
3）我们先盯到学习地址发布出来。

指导课在这里：
http://app.ai-shifu.cn/c/57b5dd9f3bb6478683ef7674403cefa4
```

## 如果用户需要企业采购流程

如果用户因公司流程无法直接在后台付款，使用 `procurement-faq.md`：收集公司名称、付款主体、发票/合同/对公需求、预计付款时间和采购负责人。未经确认，不承诺特殊付款条款。
