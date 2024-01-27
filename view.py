import gradio
import webview
import threading
import time
import queue


server_name="127.0.0.1"
server_port=7860

    
    
def main():
    url = f"http://{server_name}:{server_port}"
    # url = "https://pywebview.flowrl.com/guide/"
    webview.create_window('Hello world', url)
    webview.start()
    raise SystemExit(0)
    
    
if __name__ == '__main__':
    main()