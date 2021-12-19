from ..crawler.spider import Spider


def test_example():
    a = 123
    assert isinstance(a, int)
    assert a == 123


def test_clear_html_tags():
    text = "<p>testing</p>"
    output = Spider.clear_html_tags(text)
    assert output == "testing"
