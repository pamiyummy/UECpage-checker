from extract_web import scraping
from file_io import overwrite_txt, read_txt
from line_notify import line_notify


def main() -> None:
    old_text = read_txt('./content.txt')
    new_text = scraping()

    if old_text != new_text:
        overwrite_txt(new_text)
        message = 'ページに変更があります。\nhttps://www.c1.uec.ac.jp/internal/b3/'
        line_notify(message)
        print('content.txt has changed.')
    else:
        message = 'ページに変更はありません。\nhttps://www.c1.uec.ac.jp/internal/b3/'
        line_notify(message)
        print('There is no change on the web page.')


if __name__ == '__main__':
    main()
