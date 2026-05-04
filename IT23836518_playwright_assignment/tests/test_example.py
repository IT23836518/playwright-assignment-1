from playwright.sync_api import expect


def test_example_page_has_title(page):
    page.goto("https://example.com")
    expect(page).to_have_title("Example Domain")