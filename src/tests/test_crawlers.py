from os import getenv

from requests import get
from scrapy.http import HtmlResponse

from src.crawler.fake_crawler import FakeCrawler
from ..crawler.dcard import Dcard
from ..crawler.gamer import Gamer
from ..crawler.ptt import PTT
from ..crawler.spider import Spider
from ..kernel import Config, Database

config = Config()
database = Database(config)


def get_response(url: str, **kwargs) -> HtmlResponse:
    headers = {"user-agent": Spider.FAKEUSERAGENT_FALLBACK}
    real_response = get(url, headers=headers, **kwargs)
    return HtmlResponse(
        status=real_response.status_code,
        url=real_response.url,
        body=real_response.text.encode('utf-8'),
        headers=real_response.headers,
        encoding='utf-8'
    )


def test_clear_html_tags():
    text = "<p>testing</p>"
    output = FakeCrawler.clear_html_tags(text)
    assert output == "testing"


def test_explode():
    text = "testing.abc，這是測試 字串"
    output = FakeCrawler(config).explode(text)
    assert list(output) == ['testing', 'abc', '這是', '測試', '字串']


def test_spider_ptt():
    url = "https://www.ptt.cc/bbs/Gossiping/M.1640008426.A.FA9.html"
    cookies = {"over18": "1"}
    response = get_response(url, cookies=cookies)
    crawler = PTT(config)
    article = crawler.capture(response)
    assert article is not None
    assert article.class_ == "Gossiping"
    assert article.tag == "問卦"
    assert article.title == "宏宏有可能把戰局緩住最後什麼都不給嗎"


def test_spider_dcard():
    if getenv("APP_ENV") == "test":
        return
    url = "https://www.dcard.tw/f/youtuber/p/237697654"
    response = get_response(url)
    crawler = Dcard(config)
    article = crawler.capture(response)
    assert article is not None
    assert article.class_ == "YouTuber"
    assert article.tag == "Unknown"
    assert article.title == "炎上關注王力宏😆"


def test_spider_gamer():
    url = "https://forum.gamer.com.tw/C.php?bsn=60076&snA=6793478"
    response = get_response(url)
    crawler = Gamer(config)
    article = crawler.capture(response)
    assert article is not None
    assert article.class_ == "場外休憩區"
    assert article.tag == "情報"
    assert article.title == "快訊！王力宏失去了一切"
