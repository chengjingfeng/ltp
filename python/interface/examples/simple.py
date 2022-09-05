from ltp import LTP


def legacy():
    ltp = LTP("LTP/legacy")
    result = ltp(
        ["他叫汤姆去拿外衣。", "树上停着一些小鸟。先飞走了19只，又飞走了15只。两次共飞走了多少只小鸟？"],
        tasks=["cws", "pos", "ner"],
    )
    ltp.add_word("汤姆去")
    print(result.cws)
    print(result.pos)
    print(result.ner)


def neural():
    ltp = LTP("LTP/tiny")
    ltp.add_word("汤姆去")

    # 未分词的文本
    result = ltp.pipeline(
        ["他叫汤姆去拿外衣。", "韓語：한국의 단오", "树上停着一些小鸟。先飞走了19只，又飞走了15只。两次共飞走了多少只小鸟？"],
        tasks=["cws", "pos", "ner", "srl", "dep", "sdp"],
    )
    print(result.cws)
    print(result.pos)
    print(result.ner)
    print(result.srl)
    print(result.dep)
    print(result.sdp)

    # 已经分词的文本
    result = ltp.pipeline(
        [["他", "叫", "汤姆", "去", "拿", "外衣", "。"], ["가을동", "叫", "1993", "年", "的", "Ameri", "·"]],
        # 注意这里移除了 "cws" 任务
        tasks=["pos", "ner", "srl", "dep", "sdp"],
    )
    print(result.pos)
    print(result.ner)
    print(result.srl)
    print(result.dep)
    print(result.sdp)

    # Batched 未分词的文本
    result = ltp(
        ["他叫汤姆去拿外衣。", "韓語：한국의 단오", "树上停着一些小鸟。先飞走了19只，又飞走了15只。两次共飞走了多少只小鸟？"],
        tasks=["cws", "pos", "ner", "srl", "dep", "sdp"],
    )
    print(result.cws)
    print(result.pos)
    print(result.ner)
    print(result.srl)
    print(result.dep)
    print(result.sdp)


def main():
    # legacy()
    neural()


if __name__ == "__main__":
    main()
