## API接口
1. 接口地址：https://api.bztup.com/v1/words
2. 请求方式：POST
3. 请求格式：application/json
4. 返回格式: JSON
5. 请求参数说明：
 1). word: 抖口令  例子：#在抖音，记录美好生活##热门 #办公室 #搞笑 凡事还是得多挣扎一下，也许还有好事发生😌@抖音小助手 http://v.douyin.com/BNtvpQ/ 复制此链接，打开【抖音短视频】，直接观看视频！
 2). aweme_id: 抖音视频id 6714101618352131339

6. 返回参数格式

 1) 如果response status code = 201, 则返回刚插入的那条数据
    {
        "word": "#在抖音，记录美好生活##热门 #办公室 #搞笑 凡事还是得多挣扎一下，也许还有好事发生😌@抖音小助手 http://v.douyin.com/BNtvpQ/ ",
        "video": "6714101618352131339"
    }
 2) 如果 response status code = 422, 则表示数据参数有误
    [
        {
            "field": "word",
            "message": " word need include \"v.douyin.com\" "
        }
    ]
 3) 如果response status code = 403, 则表示该ip禁止访问
    {
        "name": "Forbidden",
        "message": "Login Required",
        "code": 0,
        "status": 403,
    }

注意：请根据响应码进行相关处理

