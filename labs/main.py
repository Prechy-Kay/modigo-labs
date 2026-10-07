def merge_tags(tags1, tags2):
    return tags1 | tags2


merge_tags(set(), {"a", "b"})
merge_tags({"x"}, set())
merge_tags(set(), set())