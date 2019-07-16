# -*- coding: utf-8 -*-
import wechatsogou
from wechatsogou import WechatSogouConst

# 直连
ws_api = wechatsogou.WechatSogouAPI()
"""
    # 验证码输入错误的重试次数，默认为1
    ws_api = wechatsogou.WechatSogouAPI(captcha_break_time=3)
    
    # 所有requests库的参数都能在这用
    # 如 配置代理，代理列表中至少需包含1个 HTTPS 协议的代理, 并确保代理可用
    ws_api = wechatsogou.WechatSogouAPI(proxies={
        "http": "127.0.0.1:8888",
        "https": "127.0.0.1:8888",
    })
    
    # 如 设置超时
    ws_api = wechatsogou.WechatSogouAPI(timeout=0.1)
"""


def get_gzh_info(gzh_name):
    """
    获取公众号基本信息
    """
    result = ws_api.get_gzh_info(gzh_name)
    result_dict = {
        # 最近10条群发页链接
        'profile_url': result['profile_url'],
        # 头像
        'headimage': result['headimage'],
        # 名称
        'wechat_name': result['wechat_name'],
        # 微信id
        'wechat_id': result['wechat_id'],
        # 最近一月群发数
        'post_perm': int(result['post_perm']),
        # 最近一月阅读量
        'view_perm': int(result['view_perm']),
        # 二维码
        'qrcode': result['qrcode'],
        # 简介
        'introduction': result['introduction'],
        # 认证
        'authentication': result['authentication']
    }
    return result_dict


def gzh_search(gzh_name):
    """
    搜索公众号
    :param gzh_name: 公众号名称
    :return: 公众号列表
    """
    gzh_list = ws_api.search_gzh(gzh_name)
    return gzh_list


def article_search(gzh_name):
    """
    搜索公众号文章
    :param gzh_name: 公众号名称
    :return: 文章列表
    """
    articles = ws_api.search_article(gzh_name)
    return articles


def get_article_history(gzh_name):
    """
    获取最近发表的文章
    :param gzh_name: 公众号名称
    :return: 最近文章信息
    """
    article_info = ws_api.get_gzh_article_by_history(gzh_name)
    return article_info


def get_article_hot():
    """
    解析首页热门文章，此处以美食为例
    :return: 热门文章信息
    """
    hot_article = ws_api.get_gzh_article_by_hot(WechatSogouConst.hot_index.food)
    return hot_article


def get_keyword_suggest_article(keywords):
    """
    获取关键字联想公众号
    :param keywords: 关键词
    :return: 公众号列表
    """
    result = ws_api.get_sugg(keyword=keywords)
    return result


if __name__ == '__main__':
    info = get_gzh_info("深圳本地宝")
    print(info)


