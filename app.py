import gradio

server_name = '127.0.0.1'
server_port = 7860


def main():
    app = gradio.Interface(fn=lambda x: x, inputs='text', outputs='text')
    _, url, _ = app.launch(
        inline=True,
        inbrowser=False,
        server_name=server_name,
        server_port=server_port,
    )


if __name__ == '__main__':
    main()
