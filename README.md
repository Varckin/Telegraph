## ![Telegraph API Logo](https://telegra.ph/favicon.ico) Telegraph API library | Telegra.ph

`Telegra.ph` is a minimalist publishing tool that allows you to create richly formatted posts and push them to the Web in just a click. Telegraph posts also get beautiful Instant View pages on Telegram.

## API Methods
### Account Management
* **createAccount**: *Create a new Telegraph account.*
* **editAccountInfo**: *Update your account details (name, author name, etc.).*
* **getAccountInfo**: *Retrieve account info such as the number of pages.*
* **revokeAccessToken**: *Reset your access token if compromised.*
### Page Management
* **createPage**: *Create a new page with title and content.*
* **editPage**: *Update an existing page with new content.*
* **getPage**: *Retrieve the content and metadata of a specific page.*
* **getPageList**: *List all pages for the authenticated account.*
### Analytics
* **getViews**: *Get the view count for a specific article over time.*

Here's the translated and formatted content for GitHub:

## Supported HTML Tags for Formatting Content in Telegraph API

The Telegraph API allows you to format content using various HTML tags when creating or editing pages. Below is a list of available tags and examples of how to use them:

### Available Tags

- **`a`** — Link

  Attributes: `href` (URL of the external resource).
  
  Example:
  ```json
  {"tag": "a", "attrs": {"href": "https://example.com"}, "children": ["Example"]}
  ```

- **`aside`** — Sidebar

  Example:
  ```json
  {"tag": "aside", "children": ["Sidebar note"]}
  ```

- **`b`** — Bold text

  Example:
  ```json
  {"tag": "b", "children": ["This is bold text"]}
  ```

- **`blockquote`** — Blockquote

  Example:
  ```json
  {"tag": "blockquote", "children": ["This is a blockquote"]}
  ```

- **`br`** — Line break

  Example:
  ```json
  {"tag": "br"}
  ```

- **`code`** — Code block

  Example:
  ```json
  {"tag": "code", "children": ["print('Hello, world!')"]}
  ```

- **`em`** — Italic text

  Example:
  ```json
  {"tag": "em", "children": ["This is italic text"]}
  ```

- **`figcaption`** — Figure caption

  Example:
  ```json
  {"tag": "figcaption", "children": ["This is a figure caption"]}
  ```

- **`figure`** — Figure block

  Example:
  ```json
  {
      "tag": "figure",
      "children": [
          {"tag": "img", "attrs": {"src": "https://example.com/image.jpg"}},
          {"tag": "figcaption", "children": ["Caption for the image"]}
      ]
  }
  ```

- **`h3`** — Heading level 3

  Example:
  ```json
  {"tag": "h3", "children": ["Heading level 3"]}
  ```

- **`h4`** — Heading level 4

  Example:
  ```json
  {"tag": "h4", "children": ["Heading level 4"]}
  ```

- **`hr`** — Horizontal line

  Example:
  ```json
  {"tag": "hr"}
  ```

- **`i`** — Italic text

  Example:
  ```json
  {"tag": "i", "children": ["Italic text"]}
  ```

- **`iframe`** — Embed external content (e.g., YouTube video)

  Attributes: `src` (URL of the embedded content).

  Example:
  ```json
  {"tag": "iframe", "attrs": {"src": "https://www.youtube.com/embed/dQw4w9WgXcQ"}}
  ```

- **`img`** — Image

  Attributes: `src` (URL of the image).

  Example:
  ```json
  {"tag": "img", "attrs": {"src": "https://example.com/image.jpg"}}
  ```

- **`li`** — List item

  Example:
  ```json
  {"tag": "li", "children": ["List item"]}
  ```

- **`ol`** — Ordered list (numbered)

  Example:
  ```json
  {
      "tag": "ol",
      "children": [
          {"tag": "li", "children": ["First item"]},
          {"tag": "li", "children": ["Second item"]}
      ]
  }
  ```

- **`p`** — Paragraph

  Example:
  ```json
  {"tag": "p", "children": ["This is a paragraph"]}
  ```

- **`pre`** — Preformatted text (used for code blocks)

  Example:
  ```json
  {"tag": "pre", "children": ["print('Hello, world!')"]}
  ```

- **`s`** — Strikethrough text

  Example:
  ```json
  {"tag": "s", "children": ["Strikethrough text"]}
  ```

- **`strong`** — Strong emphasis (usually bold text)

  Example:
  ```json
  {"tag": "strong", "children": ["Strong emphasis text"]}
  ```

- **`u`** — Underlined text

  Example:
  ```json
  {"tag": "u", "children": ["Underlined text"]}
  ```

- **`ul`** — Unordered list (bulleted)

  Example:
  ```json
  {
      "tag": "ul",
      "children": [
          {"tag": "li", "children": ["List item 1"]},
          {"tag": "li", "children": ["List item 2"]}
      ]
  }
  ```

- **`video`** — Embed video

  Attributes: `src` (URL of the video).

  Example:
  ```json
  {"tag": "video", "attrs": {"src": "https://example.com/video.mp4"}}
  ```

### Example Article Using Various Tags

```json
[
    {"tag": "h3", "children": ["Article Heading"]},
    {"tag": "p", "children": ["This is a paragraph with ", {"tag": "strong", "children": ["bold text"]}, "."]},
    {"tag": "ul", "children": [
        {"tag": "li", "children": ["First list item"]},
        {"tag": "li", "children": ["Second list item"]}
    ]},
    {"tag": "figure", "children": [
        {"tag": "img", "attrs": {"src": "https://example.com/image.jpg"}},
        {"tag": "figcaption", "children": ["Caption for the image"]}
    ]},
    {"tag": "blockquote", "children": ["This is a blockquote."]},
    {"tag": "iframe", "attrs": {"src": "https://www.youtube.com/embed/dQw4w9WgXcQ"}}
]
```

This list of tags allows you to create diverse pages with text, images, videos, links, and other elements.

## Available types
All types used in the Telegraph API responses are represented as JSON-objects. Optional fields may be not returned when irrelevant.

### Account
This object represents a Telegraph account. 

- `short_name` (String)

  Account name, helps users with several accounts remember which they are currently using. Displayed to the user above the "Edit/Publish" button on Telegra.ph, other users don't see this name.
- `author_name` (String)

  Default author name used when creating new articles.
- `author_url` (String)

  Profile link, opened when users click on the author's name below the title. Can be any link, not necessarily to a Telegram profile or channel.
- `access_token` (String)

  Optional. Only returned by the createAccount and revokeAccessToken method. Access token of the Telegraph account.
- `auth_url` (String)

  Optional. URL to authorize a browser on telegra.ph and connect it to a Telegraph account. This URL is valid for only one use and for 5 minutes only.
- `page_count` (Integer)

  Optional. Number of pages belonging to the Telegraph account.
---

### PageList
This object represents a list of Telegraph articles belonging to an account. Most recently created articles first.

- `total_count` (Integer)
  
  Total number of pages belonging to the target Telegraph account.
- `pages` (Array of Page)
  Requested pages of the target Telegraph account.
---

### Page
This object represents a page on Telegraph.

- `path` (String)

  Path to the page.
- `url` (String)

  URL of the page.
- `title` (String)

  Title of the page.
- `description` (String)

  Description of the page.
- `author_name` (String)

  Optional. Name of the author, displayed below the title.
- `author_url` (String)

  Optional. Profile link, opened when users click on the author's name below the title.  Can be any link, not necessarily to a Telegram profile or channel.
- `image_url` (String)

  Optional. Image URL of the page.
- `content` (Array of Node)

  Optional. Content of the page.
- `views` (Integer)

  Number of page views for the page.
- `can_edit` (Boolean)

  Optional. Only returned if access_token passed. True, if the target Telegraph account can edit the page.
---

### PageViews
This object represents the number of page views for a Telegraph article.

- `views` (Integer)
  
  Number of page views for the target page.