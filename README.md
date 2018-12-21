# TechFort


## api接口文档

### USER（用户）

>  地址开头 'user/'

#### 登录

- 地址

  > user/login

- POST

- 输入
  - username
  - password

- 返回

  - 自动将sesson带入

#### 注册

- 地址

  > user/reg/

- POST

- 请求内容

  - username
  - password

- 返回

  - 注册成功，response

#### 注销

- 地址

  > user/logout

- POST

- 请求内容

  - 无

- 返回

  - 注销成功，response

#### 重设密码

- 地址

  > user/setpwd

- POST

- 请求内容

  - username
  - password
  - newpassword

- 返回

  - 修改成功，response



### Portal

#### 获取文章列表

- 地址

  > portal

- get

- 返回

  - json

####  获取文章

- 地址

  > portal/arti/

- get

- 请求

  - id

- 返回

  - json

#### 获取标签(开发中)

- 地址

  > portal

- get

- 返回

#### 创建文章

- 地址

  > portal

- get

- 返回

#### 搜索（目前只提供标题搜索）

- 地址

  > portal/search

- post

- 请求

  - key

- 返回

  - json

#### 根据用户ID获取文章

- 地址

  > portal/getbyid

- post

- 请求

  - searchUserId

- 返回