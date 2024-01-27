import webview


def main(url):
    webview.create_window('Hello world', url)
    webview.start()


if __name__ == '__main__':
    main()
