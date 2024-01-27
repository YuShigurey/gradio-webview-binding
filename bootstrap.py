import gradio

import app
import view


def main():
    # Open the server
    server: gradio.Interface
    server, url = app.main()

    # Open the client view
    view.main(url)

    # After view.main() returns, the server is closed.
    server.close()


if __name__ == '__main__':
    main()
