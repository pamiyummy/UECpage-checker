def overwrite_txt(text: str) -> None:
    """txt_path先のテキストファイルに、textを上書きする。

    Args:
        text (str): テキストファイルに上書きする文字列
    """
    txt_path = './content.txt'
    f = open(txt_path, 'w', encoding='UTF-8')
    f.write(text)
    f.close()


def read_txt(txt_path: str) -> str:
    """txt_path先のテキストファイルの内容を文字列で返す。

    Args:
        txt_path (str): テキストファイルのパス

    Returns:
        str: テキストファイルの内容
    """
    f = open(txt_path, 'r', encoding='UTF-8')
    text = f.read()
    f.close()
    return text
