# mdfetch

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

## Installation

```bash
pip install mdfetch
```

## Quick Start

```python
import mdfetch

page = mdfetch.fetch("https://example.com")

print(page.markdown())
```

## Fetch a Page

```python
import mdfetch

page = mdfetch.fetch("https://example.com")

print(page.status_code)
print(page.url)
```

## Convert HTML to Markdown

```python
page = mdfetch.fetch("https://example.com")

markdown = page.markdown()

print(markdown)
```

## Exclude HTML Tags

Remove unwanted sections before converting to Markdown.

```python
page = mdfetch.fetch("https://example.com")

markdown = page.markdown(
    exclude=["nav", "footer"]
)

print(markdown)
```

## Include Specific HTML Tags

Extract content only from selected tags.

```python
page = mdfetch.fetch("https://example.com")

markdown = page.markdown(
    include=["article"]
)

print(markdown)
```

## Combine Include and Exclude

```python
page = mdfetch.fetch("https://example.com")

markdown = page.markdown(
    include=["article"],
    exclude=["nav", "footer"]
)

print(markdown)
```

## Extract Plain Text

```python
page = mdfetch.fetch("https://example.com")

text = page.text()

print(text)
```

## Extract Links

```python
page = mdfetch.fetch("https://example.com")

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
page = mdfetch.fetch("https://example.com")

links = page.links(skip_empty=True)
```

## Roadmap

Planned features:

* Async support via httpx
* curl_cffi backend
* Proxy support
* Retry handling
* Link deduplication
* CSS selector support
* Metadata extraction

## License

MIT License
