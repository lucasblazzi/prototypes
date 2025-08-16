import frontmatter


def load_dict_md(path: str) -> dict:
    post = frontmatter.load(path)
    meta = post.metadata
    return meta


def load_raw_md(path: str) -> str:
    post = frontmatter.load(path)
    content = post.content
    metadata_text = "\n".join(f"{k}: {v}" for k, v in post.metadata.items())
    result = content or metadata_text
    return result
