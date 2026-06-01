from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class RaskPreviewHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        if path.rstrip("/") == "/index.html":
            path = "/index.html"
        if path.rstrip("/") == "/index.html/editor":
            path = "/index.html"
        elif path.startswith("/index.html/assets/"):
            path = path.removeprefix("/index.html")
        elif path.startswith("/index.html/editor/assets/"):
            path = path.removeprefix("/index.html/editor")
        return super().translate_path(path)


if __name__ == "__main__":
    server = ThreadingHTTPServer(("", 4599), RaskPreviewHandler)
    print("Serving Rask preview at http://127.0.0.1:4599/")
    server.serve_forever()
