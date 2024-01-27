# gradio-webview-binding

A simple demo of using gradio and pywebview together, make your application **looks like** a native application.


## How to try out

1. Build a package with "hatch build -t wheel" ([hatch](https://hatch.pypa.io/latest/))
2. Install the package `pip install ./dist/gradio_webview-0.1.0-py2.py3-none-any.whl`
3. Run in shell `gradio-gui-demo` or find the corresponding executable and double click on the file

You can change the app's name in `[project.gui-scripts]` section of `pyproject.toml`.


## One step further ...

You can also pack the app into a zip pack, so that end user can use your app free from installing python.

**However, app will took about 500MB**

To perform packaging, you need to:

1. Install pyoxidizer, `pip install pyoxidizer`
2. Build the package `pyoxidizer build`
3. Find out more about `pyoxidizer` at https://pyoxidizer.readthedocs.io/en/stable/
