


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            no_hash = line.replace("#", "", 1)
            result = no_hash.strip()
            return result
    raise Exception("No H1 Title Found")