from ..crawler.spider import Spider


def test_example():
    a = 123
    assert isinstance(a, int)
    assert a == 123


def test_clear_html_tags():
    text = "<p>testing</p>"
    output = Spider.clear_html_tags(text)
    assert output == "testing"


def test_explode():
    text = "testing.abc，這是測試 字串"
    output = Spider.explode(text)
    assert list(output) == ['testing', 'abc', '這是', '測試', '字串']
