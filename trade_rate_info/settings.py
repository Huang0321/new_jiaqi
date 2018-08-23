import pymysql


# 创建数据库连接对象
connect = pymysql.connect(host='localhost',
                          port=3306,
                          user='root',
                          password='123456',
                          db='jiaqi',
                          cursorclass=pymysql.cursors.DictCursor)


# 配置api_key 和 api_secret
KEY_SECRET = {
    'okex': ('6a689877-06c6-48b3-a4e2-5ce3b5931cc4', '3028064C9FA41F4C97070E7681FA9888'),
    'bittrex': ('d92a7f5fa0ad45589eaa2b7e6eb73457', '2f44fcd470584dfcbb5b71b5ca34583c')
}


# 静态价格,便于计算交易市值, 单位：￥
BTC_VALUE = 43773
ETH_VALUE = 1916
USDT_VALUE = 6.86

SYMBOL = 'NEO/USDT'

# 设置交易正反向利差
RATE_1 = 0.0035
RATE_2 = 0.0035