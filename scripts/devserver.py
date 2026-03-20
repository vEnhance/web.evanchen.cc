#!/usr/bin/env python3
"""Dev server for local testing of web.evanchen.cc"""

import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LIVE = "https://web.evanchen.cc"

MOUNTPOINTS: list[tuple[str, Path]] = [
    ("/static/", REPO / "static"),
    ("/applets/", REPO / "applets"),
    ("/handouts/", REPO / "handouts"),
    ("/", REPO / "output"),
]
REDIRECT_PREFIXES = tuple(
    line.strip() for line in (REPO / "EXTDIRS").read_text().splitlines() if line.strip()
)


class Handler(SimpleHTTPRequestHandler):
    def translate_path(self, path: str) -> str:
        path = path.split("?")[0].split("#")[0]
        for prefix, directory in MOUNTPOINTS:
            if path.startswith(prefix):
                return str(directory / path[len(prefix) :])
        return str(REPO / "output" / path.lstrip("/"))

    def do_GET(self) -> None:
        for prefix in REDIRECT_PREFIXES:
            if self.path.startswith(prefix):
                self.send_response(302)
                self.send_header("Location", LIVE + self.path)
                self.end_headers()
                return
        super().do_GET()

    def log_message(self, format: str, *args: object) -> None:
        status = args[1] if len(args) > 1 else "?"
        print(f"  {status}  {self.path}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-p", "--port", type=int, default=8000, metavar="PORT")
    args = parser.parse_args()

    server = HTTPServer(("", args.port), Handler)
    print(f"Serving http://localhost:{args.port}/")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
