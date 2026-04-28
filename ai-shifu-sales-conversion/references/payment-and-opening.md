# 付款和开通

当用户已经选择套餐，或询问“怎么付款、买了之后谁服务”时使用。

若用户关心“买了以后有什么福利/服务/保障、是否开发票、企业采购能否签合同”，同时读取 `paid-user-benefits.md`。付款承接不只是开通通知，也可以作为购买前降低风险、促进成交的策略支持。

## 付款页面

Users can pay directly in the backend billing package page:

`https://app.ai-shifu.cn/admin/billing?tab=packages`

## 标准付款话术

```text
可以，套餐可以直接在后台积分套餐页面付款：
https://app.ai-shifu.cn/admin/billing?tab=packages

购买任意套餐都会赠送课程。月套餐会邀请进入统一付费客户群，在群里提供基础服务、案例分享和课程创作问题讨论；年套餐除了社群，还会有客户专有服务群，并享有团队提供的优先技术支持。所有订单都可以开发票，企业采购也可以签订电子合同。
```

## 服务群规则

| 套餐类型 | 服务安排 | 解释方式 |
|---|---|---|
| 月套餐 | 统一付费客户群 | 适合个人/小团队先跑通课程，有群内基础服务、案例分享和课程创作问题讨论 |
| 年套餐 | 统一付费客户群 + 客户专有服务群 + 优先技术支持 | 适合机构/企业/团队持续使用，会有客户专有服务群跟进 |

## 付款后检查清单

Update collaboration record immediately:

`用户, 套餐, 付款状态, 付款时间, 服务群类型, 负责人, 是否已发课程创作指导课, 第一门正式课主题, 下次跟进时间`

Then do these actions:

1. Confirm payment/package in backend or with responsible person.
2. Tell user a responsible person will follow up service.
3. Invite user to the correct service group: 月套餐统一付费客户群；年套餐统一付费客户群 + 客户专有服务群.
4. 发送赠送课程/购买后课程创作指导课： `http://app.ai-shifu.cn/c/57b5dd9f3bb6478683ef7674403cefa4`.
5. Ask user to confirm the first official course material/topic.
6. Set the 3-day and 7-day customer success follow-up.

## 付款后开通话术

```text
已经收到你的开通信息。接下来我先把付费用户福利和使用路径同步给你：

1）购买套餐会赠送课程，帮助你快速理解课程创作和使用方式；
2）月套餐会进入统一付费客户群，年套餐会有客户专有服务群和优先技术支持；
3）积分用量告急时系统会自动提醒；
4）订单可以开发票，企业采购也支持电子合同。

赠送课程在这里：
http://app.ai-shifu.cn/c/57b5dd9f3bb6478683ef7674403cefa4

下一步我们先确认你的第一门正式课资料/主题，把第一条学习地址跑通。
```

## 如果用户需要企业采购流程

如果用户因公司流程无法直接在后台付款，使用 `procurement-faq.md`：收集公司名称、付款主体、发票/合同/对公需求、预计付款时间和采购负责人。未经确认，不承诺特殊付款条款。
