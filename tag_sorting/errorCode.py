# -*- coding: utf-8 -*-


class ErrorCode(object):
    """
    错误码及错误信息.
    """

    error_request_num_limit = {
        4: "集群超限额",
        17: "每天请求量超限额",
        18: "QPS超限额",
        19: "请求总量超限额",
    }

    error_4xx = {
        3: "调用的API不存在，请检查后重新尝试",
        6: "无权限访问该用户数据",
        100: "包含了无效或错误参数，请检查代码",
        282002: "编码错误，请使用GBK编码",
        282004: "请求中包含非法参数，请检查后重新尝试",
        282008: "仅支持GBK和UTF-8，其余为不支持的字符编码，请检查后重新尝试",
        282011: "未训练或未生效该接口",
        282134: "输入为空",
        282130: "当前查询无结果返回，出现此问题的原因一般为：参数配置存在问题，请检查后重新尝试",
        282131: "输入长度超限，请查看文档说明",
        282133: "接口参数缺失",
        282300: "word不在算法词典中",
        282301: "word_1提交的词汇暂未收录，无法比对相似度",
        282302: "word_2提交的词汇暂未收录，无法比对相似度",
        282303: "word_1和word_2暂未收录，无法比对相似度",
    }

    error_5xx = {
        1: "服务器内部错误，请再次请求，如果持续出现此类错误，请通过QQ群（224994340）或工单联系技术支持团队",
        2: "服务暂不可用，请再次请求，如果持续出现此类错误，请通过QQ群（224994340）或工单联系技术支持团队",
        282000: "服务器内部错误，请再次请求，如果持续出现此类错误，请通过QQ群（632426386）或工单联系技术支持团队",
    }
