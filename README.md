# AutoLD
A13 机器学习训练平台
【整体背景】
在 ALL IN AI 的时代， AI 算法已经遍及各学科、 各领域的方方面面。 AI 模型的训练已成为一个常见的业务需要， 但是 AI 模型的训练对于新手来说及其困难， 模型训练者往往要考虑 GPU 服务器配置、 开发环境部署、 多个模型的管理、模型的发布等等工程因素， 而无法集中精力研究算法的改进， 于是我们的产品——分布式 AI 训练场，该项目着力解决 AI 模型训练的“模型人肉管理”、“环境人肉配置” 、“算力紧张， 训练慢” 的问题。
AI 平台主要分为“算法管理” 、 “算法商城” 、“在线训练” 、“分布式控制模组” 、 “订单管理” 等功能模块。
分布式 AI 平台为用户提供：
1. “易上手、 高可用、 高效率” 的在线机器学习模型训练；
2. “多样化” 的算法商城；
3. “全方位、 细粒度” 的算法模型和算法性能可视化；
【用户期望】
用户业务
用户选购算法模型， 确认订单并付款
选择算力配置创建训练作业， 模型的版本管理， 训练结果可视
化
根据训练任务的算力配置， 分布式调度后台集群中的算力来完
成训练任务
用户可以查看、 导出、 取消订单
登录、 注销、 切换账号、 查看基本信息、 账户余额， 个人设置，
系统设置等功能

后台业务
查看所有订单， 查询订单， 批准取消订单
管理员可以上架、 下架算法商品， 修改商品信息， 查看所有算
法商品
管理员可以监控集群状态， 配置新结点、 修改结点信息、 删除
结点


【开发说明】
前端采用 VUE 框架， 后端采用 Spring Cloud 微服务框架， 分布式技术实现采用 Docker 容器作虚拟化， 运用 Kubernetes 技术完成集群的管理和服务器调度； 服务器底层运用 Kubeflow 框架实现分布式训练， 在上层使用Spring开源 API（kubernetes-client/java） 调用底层 Kubeflow 框架来实现集成。