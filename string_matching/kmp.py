# Knuth Morris Pratt
# https://www.youtube.com/watch?v=EL4ZbRF587g
# Time complexity:
# - Preprocessing - O(m)
# - Search - O(n)

from typing import List


def prefix_offsets(pattern: str) -> List[int]:
    ret = [0] * (len(pattern) + 1)
    ret[0] = -1
    prefix_len = 0
    i = 1
    while i < len(pattern):
        # Prefix repeats itself in the pattern
        if pattern[prefix_len] == pattern[i]:
            prefix_len += 1
            i += 1
            ret[i] = prefix_len
        # Pattern and the prefix no longer is equal
        elif prefix_len > 0:
            prefix_len = ret[prefix_len]
        else:
            i += 1
            ret[i] = 0
    
    return ret


def kmp_search(text: str, pattern: str) -> List[int]:
    matches: List[int] = []
    offsets = prefix_offsets(pattern)

    t, p = 0, 0  # text and pattern positions
    while t < len(text):
        # Pattern and text matches, increment indices, and if match, report it
        if pattern[p] == text[t]:
            t += 1
            p += 1
            if p == len(pattern):
                matches.append(t - p)
                # We found the string, can offset by maximum length
                p = offsets[p]
        # Pattern doesn't match, find the amount by what we can offset the most to the right
        else:
            p = offsets[p]
            if p < 0:
                t += 1
                p += 1

    return matches


if __name__ == "__main__":
    print(kmp_search("xyzabcxyzhudrhudryxyzabcxyz", "xyzabcxyz"))