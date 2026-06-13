# markdfetch

A lightweight Python library for fetching web pages and extracting content as Markdown, plain text, or structured links.

## Features

* Fetch web pages with a simple API
* Convert HTML to Markdown
* Extract plain text from web pages
* Extract links with URL and anchor text
* Exclude unwanted HTML tags before processing
* Include only specific HTML tags before processing
* Support for custom request headers and timeouts
* Automatic resolution of relative URLs
* CSS selector support
* Optional link deduplication
* Automatic retry handling

## Installation

```bash
pip install markdfetch
```

## Quick Start

```python
import markdfetch

page = markdfetch.fetch("https://example.com")

print(page.markdown())
```

## Fetch a Page

```python
import markdfetch

page = markdfetch.fetch("https://example.com")

print(page.status_code)
print(page.url)
```

## Convert HTML to Markdown

```python
page = markdfetch.fetch("https://example.com")

markdown = page.markdown()

print(markdown)
```

## Exclude HTML Tags

Remove unwanted sections before converting to Markdown.

```python
page = markdfetch.fetch("https://example.com")

markdown = page.markdown(
    exclude=["nav", "footer"]
)

print(markdown)
```

## Include Specific HTML Tags

Extract content only from selected tags.

```python
page = markdfetch.fetch("https://example.com")

markdown = page.markdown(
    include=["article"]
)

print(markdown)
```

## Combine Include and Exclude

```python
page = markdfetch.fetch("https://example.com")

markdown = page.markdown(
    include=["article"],
    exclude=["nav", "footer"]
)

print(markdown)
```

## Extract Plain Text

```python
page = markdfetch.fetch("https://example.com")

text = page.text()

print(text)
```

## Extract Links

```python
page = markdfetch.fetch("https://example.com")

links = page.links()

print(links)
```

Example output:

```python
[
    {
        "url": "https://example.com/about",
        "text": "About Us"
    },
    {
        "url": "https://example.com/contact",
        "text": "Contact"
    }
]
```

## Skip Empty Links

```python
page = markdfetch.fetch("https://example.com")

links = page.links(skip_empty=True)
```

## Extract Content Using CSS Selectors

Target specific elements using CSS selectors.

```python
page = markdfetch.fetch("https://example.com")

markdown = page.markdown(
    selector="article"
)

print(markdown)
```

You can use any valid CSS selector:

```python
page.markdown(selector=".content")
page.markdown(selector="#main")
page.markdown(selector="article.post")
```

## Extract Text Using CSS Selectors

Extract plain text from specific sections of a page.

```python
page = markdfetch.fetch("https://example.com")

text = page.text(
    selector=".content"
)

print(text)
```

## Extract Unique Links

Remove duplicate URLs from the extracted links.

```python
page = markdfetch.fetch("https://example.com")

links = page.links(
    unique=True
)

print(links)
```


## Roadmap

Planned features:

* Async support via httpx
* Proxy support
* Metadata extraction

## License

MIT License
