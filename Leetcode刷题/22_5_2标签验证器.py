# 如果当前的字符为 \texttt{<}<，那么需要考虑下面的四种情况：
#
# 如果下一个字符为 \texttt{/}/，那么说明我们遇到了一个结束标签。我们需要定位下一个 \texttt{>}> 的位置 jj，
# 此时 \textit{code}[i+2..j-1]code[i+2..j−1] 就是该结束标签的名称。我们需要判断该名称与当前栈顶的名称是否匹配，
# 如果匹配，说明名称的标签已经闭合，我们需要将当前栈顶的名称弹出。同时根据规则 11，我们需要保证整个 \textit{code}code
# 被闭合标签包围，因此如果栈中已经没有标签，但是 jj 并不是 \textit{code}code 的末尾，那么说明后续还会有字符，它们不被闭合标签包围。
#
# 如果下一个字符为 \texttt{!}!，那么说明我们遇到了一个 \text{cdata}cdata，我们需要继续往后读 77 个字符，判断其是否为
# \texttt{[CDATA[}[CDATA[。在这之后，我们定位下一个 \texttt{]]>}]]> 的位置 jj，此时 \textit{code}[i+9..j-1]code[i+9..j−1]
# 就是 \text{cdata}cdata 中的内容，它不需要被解析，所以我们也不必进行任何验证。需要注意的是，根据规则 11，栈中需要存在至少一个开放的标签。
#
# 如果下一个字符为大写字母，那么说明我们遇到了一个开始标签。我们需要定位下一个 \texttt{>}> 的位置 jj，
# 此时 \textit{code}[i+2..j-1]code[i+2..j−1] 就是该开始标签的名称。我们需要判断该名称是否恰好由 11 至 99 个大写字母组成，
# 如果是，说明该标签合法，我们需要将该名称放入栈顶。
#
# 除此之外，如果不存在下一个字符，或者下一个字符不属于上述三种情况，那么 \textit{code}code 是不合法的。



class Solution:
    def isValid(self, code: str) -> bool:
        tags = []
        i, n = 0, len(code)
        while i < n:
            if code[i] != "<":
                if not tags:
                    return False
                i += 1
                continue
            if i == n - 1:
                return False
            if code[i + 1] == "/": # 结束标签
                j = code.find(">", i)
                if j == -1:
                    return False
                tagname = code[i + 2: j]
                if not tags or tags[-1] != tagname:
                    return False
                tags.pop()
                i = j + 1
                if not tags and i != n:
                    return False
            elif code[i + 1] == "!": # cdata
                if not tags:
                    return False
                cdata = code[i + 2: i + 9]
                if cdata != "[CDATA[":
                    return False
                j = code.find("]]>", i)
                if j == -1:
                    return False
                i = j + 1
            else: #开始标签
                j = code.find(">", i)
                if j == -1:
                    return False
                tagname = code[i + 1: j]
                if not 1 <= len(tagname) <= 9 or not all(ch.isupper() for ch in tagname):
                    return False
                tags.append(tagname)
                i = j + 1

        return not tags
