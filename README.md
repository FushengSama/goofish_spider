# Goofish Spider 项目文档

## 项目简介
该项目为个人编写的从闲鱼获取商品信息的脚本(仅供学习交流使用)。

## 系统要求
- Python 3.10+
- MySQL数据库


## 安装部署

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 数据库配置
在'config.yaml'文件中配置脚本任务信息，
'dbconfig.yaml'为数据库配置信息


### 3. 运行爬虫
```bash
python src/main.py
```

## 使用示例

### 基本爬取
```python
from spider2Database import getConfigFromYaml,start_with_config

if __name__=="__main__":
    config=getConfigFromYaml("config.yaml")
    start_with_config(config)
```
### 配置mysql数据库
```bash
./scripts/dockerStartMysql.sh

```

提供了"createDatabase.sql"创建数据表


配置dbconfig.yaml文件中的数据库信息
```yaml
-db_config:
  user: "root"
  passwd: "123456"
  host: "localhost"
  port: 3306
  database: "spiderTest"
```
