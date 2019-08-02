# Jenkins 基础使用分享

## Jenkins是什么？
1. 持续自动地构建、测试、部署软件项目
2. 监控一些定时执行的任务


pipeline syntax  流水线语法生成器，写流水线时尽量用这个去写，（和可以➕JIRA comment or Artifactory comment）

replay  重跑，编辑调试pipeline代码，直接要验证。（不用git 提交，可以直接用replay）

JOB_NAME 

1. 不要建自由风格的项目，选pipeline和multi pipeline
2. jenkins file 传到git代码，需要构建的分支传，不需要的分支不传。