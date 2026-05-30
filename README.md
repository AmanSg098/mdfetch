# mdfetch

Fetch web pages and convert them to markdown.

```python
import mdfetch

page = mdfetch.fetch("https://example.com")
print(page.markdown())