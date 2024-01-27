import gradio


def main():
    app = gradio.Interface(fn=lambda x: x, inputs='text', outputs='text')
    _, url, _ = app.launch(inline=True, inbrowser=False, prevent_thread_lock=True, quiet=True)
    return app, url


if __name__ == '__main__':
    main()
