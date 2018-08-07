## API 接口说明

`LDAP服务器配置`

```text
# 按照实际情况修改src/common.py文件中的如下配置
LDAP_HOST = 'ldap.test.com'
LDAP_BIND = 'cn=admin,dc=ldap,dc=com'
LDAP_PASS = 'admin'
baseDN = 'dc=ldap,dc=com'
```

`API启动`

```bash
cd project
python server.py --port=8080 --log_file_prefix=~/ldap_api.log
```

```text
/api/ldap_search # 获取LDAP中的用户列表
/api/add_user # 添加用户到LDAP中
/api/add_group # 创建组到LDAP中
/api/delete_user # 从LDAP中删除用户条目
/api/delete_group # 从LDAP中删除组条目
/api/modify_user # 更改LDAP中的用户的用户名
/api/modify_group # 更改LDAP中组信息
```


* `/api/ldap_search`

```shell
curl 'http://127.0.0.1:8080/api/ldap_search'
```

* `/api/add_user`

```shell
curl 'http://127.0.0.1:8080/api/add_user?user=test&group=DevOps'
```

* `/api/add_group`

```shell
curl 'http://127.0.0.1:8080/api/add_group?group=DevOps'
```

* `/api/delete_user`

```shell
curl 'http://127.0.0.1:8080/api/delete_user?user=test&group=TEST'
```

* `/api/delete_group`

```shell
curl 'http://127.0.0.1:8080/api/delete_group?group=TEST'
```

* `/api/modify_user`

```shell
curl 'http://127.0.0.1:8080/api/modify_user?user=test&group=DevOps&fullname=测试'
```

* `/api/modify_group`

```shell
curl 'http://127.0.0.1:8080/api/modify_group?user=test&group=DevOps&newgroup=TEST'
```


