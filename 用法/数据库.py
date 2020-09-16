
1，创建更改文件
python manage.py makemigrations

2. 将生成的py文件应用到数据库
python manage.py migrate

上面这种方法可以在SQL等数据库中创建与models.py代码对应的表，不需要自己手动执行SQL。



5. 清空数据库
python manage.py flush
此命令会询问是 yes 还是 no, 选择 yes 会把数据全部清空掉，只留下空表。

6. 创建超级管理员
python manage.py createsuperuser

# 按照提示输入用户名和对应的密码就好了邮箱可以留空，用户名和密码必填
# 修改 用户密码可以用：
python manage.py changepassword username


