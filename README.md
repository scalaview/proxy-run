
### 开始
```shell
  virtualenv .
  source bin/activate
  pip install -r requirements.txt
  python runproxy.py
```


### 当后面更新了包以后需要更新require 文件

``` shell
  pip freeze > requirements.txt
```