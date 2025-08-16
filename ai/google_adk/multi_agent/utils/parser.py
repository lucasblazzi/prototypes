import frontmatter


def load_md(path: str) -> dict:
    post = frontmatter.load(path)
    meta = post.metadata
    return meta

