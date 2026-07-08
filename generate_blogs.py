"""
Generate blog article HTML pages from articles.json.
Articles with full content are rendered inline.
Articles without content (empty content array) show an archive notice.
"""
import json
import os
import math
import html as html_module

# ── HTML Template ──
# Shared structure for all blog pages
PAGE_TOP = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | Alfie Njeru</title>
  <meta name="description" content="{description}" />
  <link rel="stylesheet" href="../css/style.css" />
</head>
<body>
  <div class="glow-orb glow-orb--gold"></div>
  <div class="glow-orb glow-orb--blue"></div>

  <nav class="navbar" id="navbar">
    <div class="container">
      <a href="../index.html" class="nav-logo">
        <div class="logo-icon">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm0 2.18l7 3.12v4.7c0 4.83-3.23 9.36-7 10.57-3.77-1.21-7-5.74-7-10.57V6.3l7-3.12z"/><path d="M12 7a3 3 0 00-3 3v1H8v5h8v-5h-1v-1a3 3 0 00-3-3zm1 4h-2v-1a1 1 0 112 0v1z"/></svg>
        </div><span>the-<span>infosec</span></span>
      </a>
      <div class="nav-links" id="navLinks">
        <a href="../index.html">Home</a>
        <a href="../about.html">About</a>
        <a href="../index.html#tools">Tools</a>
        <a href="../index.html#blog" class="active">Blog</a>
        <a href="../contact.html" class="nav-cta">Hire Me</a>
      </div>
      <button class="nav-toggle" id="navToggle" aria-label="Toggle menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </nav>

  <article class="blog-article">
    <div class="container">
      <div class="article-header reveal">
        <div class="article-meta">
          <span class="article-date">{date}</span>
          {reading_time_html}
        </div>
        <h1>{title}</h1>
        {tags_html}
      </div>
      <div class="article-content reveal reveal-delay-1">
        <p class="lead" style="font-size: 20px; color: var(--gold-500);">{description}</p>
"""

ARCHIVE_NOTICE = """
        <div class="archive-notice" style="background: rgba(255,255,255,0.03); padding: 32px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05); margin-top: 48px;">
          <h3 style="margin-top: 0;">Archive Notice</h3>
          <p>This article was originally published on the legacy WordPress blog. The content is currently preserved in archive format.</p>
          <p>You can view the original snapshot, complete with any images and comments, on the Wayback Machine:</p>
          <a href="{archive_url}" target="_blank" rel="noopener" class="btn btn-primary" style="display: inline-flex; margin-top: 16px;">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" style="width: 20px; height: 20px; margin-right: 8px;"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6M15 3h6v6M10 14L21 3"/></svg>
            View Full Archive
          </a>
        </div>
"""

ORIGINALLY_PUBLISHED = """
        <div style="margin-top: 64px; padding-top: 32px; border-top: 1px solid rgba(255,255,255,0.08); font-size: 14px; color: var(--gray-500);">
          Originally published on <a href="{archive_url}" target="_blank" rel="noopener" style="color: var(--gold-500);">the-infosec.com</a>
        </div>
"""

PAGE_BOTTOM = """
      </div>
      <div class="article-nav reveal reveal-delay-2">
        <a href="../index.html#blog" class="back-to-blog">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
          Back to all articles
        </a>
      </div>
    </div>
  </article>

  <footer class="footer">
    <div class="container">
      <div class="footer-content">
        <div class="footer-brand">
          <div class="logo-icon">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4z"/></svg>
          </div>
          <span>the-infosec</span>
        </div>
        <div class="footer-links">
          <a href="../index.html">Home</a>
          <a href="../about.html">About</a>
          <a href="../index.html#tools">Tools</a>
          <a href="../contact.html">Contact</a>
        </div>
        <div class="footer-social">
          <a href="https://www.linkedin.com/in/alfrednjeru" target="_blank" rel="noopener" aria-label="LinkedIn"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg></a>
          <a href="https://github.com/XalfiE" target="_blank" rel="noopener" aria-label="GitHub"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg></a>
          <a href="https://twitter.com/alfienjeru" target="_blank" rel="noopener" aria-label="X (Twitter)"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg></a>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 Alfie Njeru | the-infosec.com &middot; Securing Digital Solutions</p>
      </div>
    </div>
  </footer>
  <script src="../js/main.js"></script>
</body>
</html>"""


def escape(text):
    """HTML-escape text for safe insertion."""
    return html_module.escape(str(text))


def estimate_reading_time(content_blocks):
    """Estimate reading time based on word count across all text blocks."""
    word_count = 0
    for block in content_blocks:
        if block.get('text'):
            word_count += len(block['text'].split())
        if block.get('items'):
            for item in block['items']:
                word_count += len(item.split())
    minutes = max(1, math.ceil(word_count / 200))
    return minutes


def render_content_blocks(blocks):
    """Convert structured content blocks to HTML."""
    html_parts = []

    for block in blocks:
        btype = block.get('type', '')

        if btype == 'heading':
            level = block.get('level', 2)
            level = max(2, min(level, 4))  # Clamp to h2-h4
            html_parts.append(f'        <h{level}>{escape(block["text"])}</h{level}>')

        elif btype == 'paragraph':
            text = block.get('html', escape(block.get('text', '')))
            if text.strip():
                html_parts.append(f'        <p>{text}</p>')

        elif btype == 'code':
            lang = escape(block.get('language', 'text'))
            code_text = escape(block.get('text', ''))
            html_parts.append(f'        <pre><code class="language-{lang}">{code_text}</code></pre>')

        elif btype == 'image':
            src = block.get('src', '')
            alt = escape(block.get('alt', ''))
            if src:
                html_parts.append(f'        <figure><img src="{escape(src)}" alt="{alt}" loading="lazy" /></figure>')

        elif btype == 'list':
            tag = 'ol' if block.get('ordered') else 'ul'
            items_html = '\n'.join(f'          <li>{escape(item)}</li>' for item in block.get('items', []))
            html_parts.append(f'        <{tag}>\n{items_html}\n        </{tag}>')

        elif btype == 'blockquote':
            html_parts.append(f'        <blockquote><p>{escape(block.get("text", ""))}</p></blockquote>')

        elif btype == 'table':
            rows = block.get('rows', [])
            if rows:
                table_html = '        <div style="overflow-x: auto; margin: 32px 0;">\n        <table style="width: 100%; border-collapse: collapse;">\n'
                for i, row in enumerate(rows):
                    cell_tag = 'th' if i == 0 else 'td'
                    cell_style = 'padding: 12px 16px; border: 1px solid rgba(255,255,255,0.1); text-align: left;'
                    if i == 0:
                        cell_style += ' background: rgba(255,255,255,0.05); font-weight: 600; color: white;'
                    cells = ''.join(f'<{cell_tag} style="{cell_style}">{escape(c)}</{cell_tag}>' for c in row)
                    table_html += f'          <tr>{cells}</tr>\n'
                table_html += '        </table>\n        </div>'
                html_parts.append(table_html)

    return '\n\n'.join(html_parts)


def render_tags(tags):
    """Render tag badges."""
    if not tags:
        return ''
    tag_items = ''.join(
        f'<span style="display: inline-block; background: rgba(202,171,87,0.1); color: var(--gold-500); '
        f'padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 500; '
        f'margin: 4px 4px 0 0; border: 1px solid rgba(202,171,87,0.2);">{escape(tag)}</span>'
        for tag in tags
    )
    return f'<div style="margin-top: 16px;">{tag_items}</div>'


def main():
    # Load articles data
    json_path = os.path.join('blog', 'articles.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        articles = json.load(f)

    full_count = 0
    stub_count = 0

    for article in articles:
        slug = article['slug']
        title = article['title']
        date = article['date']
        desc = article['description']
        archive_url = article.get('archive_url', '')
        tags = article.get('tags', [])
        content = article.get('content', [])

        has_content = len(content) > 0

        # Reading time
        if has_content:
            minutes = estimate_reading_time(content)
            reading_time_html = (
                f'<span style="color: var(--gray-400);">&#183;</span>'
                f'<span style="color: var(--gray-400);">{minutes} min read</span>'
            )
        else:
            reading_time_html = ''

        # Tags
        tags_html = render_tags(tags)

        # Build the page top
        page = PAGE_TOP.format(
            title=escape(title),
            date=escape(date),
            description=escape(desc),
            reading_time_html=reading_time_html,
            tags_html=tags_html,
        )

        # Content body
        if has_content:
            page += '\n' + render_content_blocks(content) + '\n'
            if archive_url:
                page += ORIGINALLY_PUBLISHED.format(archive_url=escape(archive_url))
            full_count += 1
        else:
            page += ARCHIVE_NOTICE.format(archive_url=escape(archive_url))
            stub_count += 1

        # Page bottom
        page += PAGE_BOTTOM

        # Write file
        filepath = os.path.join('blog', f'{slug}.html')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(page)

    print(f"Generated {len(articles)} articles:")
    print(f"  - {full_count} with full content")
    print(f"  - {stub_count} archive stubs")


if __name__ == '__main__':
    main()
