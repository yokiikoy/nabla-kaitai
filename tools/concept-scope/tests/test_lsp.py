"""End-to-end test for the LSP server over TCP."""

import json
import socket
import subprocess
import sys
import time
import pytest


class TestLSPServer:
    def _start_server(self, port: int):
        proc = subprocess.Popen(
            [
                sys.executable,
                str(
                    __import__("pathlib").Path(__file__).resolve().parents[1]
                    / "lsp_server.py"
                ),
                "--tcp",
                "--port",
                str(port),
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        time.sleep(1.5)
        return proc

    def _send_msg(self, sock, msg):
        data = json.dumps(msg).encode()
        header = f"Content-Length: {len(data)}\r\n\r\n".encode()
        sock.sendall(header + data)

    def _recv_msg(self, sock, timeout=3):
        sock.settimeout(timeout)
        header = b""
        while b"\r\n\r\n" not in header:
            chunk = sock.recv(1)
            if not chunk:
                return None
            header += chunk
        header_str = header.decode()
        content_length = 0
        for line in header_str.split("\r\n"):
            if line.lower().startswith("content-length:"):
                content_length = int(line.split(":", 1)[1].strip())
        body = b""
        while len(body) < content_length:
            chunk = sock.recv(content_length - len(body))
            if not chunk:
                return None
            body += chunk
        return json.loads(body)

    def test_dx_square_violation(self, tmp_path):
        """Test that didOpen with dx^2 text triggers diagnostics."""
        port = 21001
        proc = self._start_server(port)

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(("127.0.0.1", port))
            sock.settimeout(5)

            # Initialize
            root = str(__import__("pathlib").Path(__file__).resolve().parents[3])
            self._send_msg(
                sock,
                {
                    "jsonrpc": "2.0",
                    "id": 1,
                    "method": "initialize",
                    "params": {
                        "processId": None,
                        "capabilities": {},
                        "rootUri": f"file://{root}",
                    },
                },
            )
            resp = self._recv_msg(sock)
            assert resp is not None
            assert "id" in resp

            self._send_msg(sock, {"jsonrpc": "2.0", "method": "initialized", "params": {}})
            time.sleep(0.3)

            # Create a test file with dx^2 violation
            test_file = tmp_path / "test.md"
            test_file.write_text("測定すると dx^2 が得られる。\n")

            with open(test_file) as f:
                content = f.read()

            self._send_msg(
                sock,
                {
                    "jsonrpc": "2.0",
                    "method": "textDocument/didOpen",
                    "params": {
                        "textDocument": {
                            "uri": f"file://{test_file}",
                            "languageId": "markdown",
                            "version": 1,
                            "text": content,
                        }
                    },
                },
            )

            # Collect publishDiagnostics
            diag_msg = None
            for _ in range(10):
                msg = self._recv_msg(sock)
                if msg and msg.get("method") == "textDocument/publishDiagnostics":
                    diag_msg = msg
                    break
                if msg:
                    pass  # Other notification

            assert diag_msg is not None, "No publishDiagnostics received"
            diagnostics = diag_msg["params"]["diagnostics"]
            assert len(diagnostics) >= 1
            assert any(d.get("code") == "notation-contract-dx-square" for d in diagnostics)

            # Shutdown
            self._send_msg(sock, {"jsonrpc": "2.0", "id": 2, "method": "shutdown"})
            time.sleep(0.2)
            self._send_msg(sock, {"jsonrpc": "2.0", "method": "exit"})
            sock.close()
        finally:
            proc.kill()
            proc.wait()

    def test_clean_text_no_diagnostics(self, tmp_path):
        """Test that clean text produces no diagnostics."""
        port = 21002
        proc = self._start_server(port)

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(("127.0.0.1", port))
            sock.settimeout(5)

            root = str(__import__("pathlib").Path(__file__).resolve().parents[3])
            self._send_msg(
                sock,
                {
                    "jsonrpc": "2.0", "id": 1, "method": "initialize",
                    "params": {"processId": None, "capabilities": {}, "rootUri": f"file://{root}"},
                },
            )
            self._recv_msg(sock)
            self._send_msg(sock, {"jsonrpc": "2.0", "method": "initialized", "params": {}})
            time.sleep(0.3)

            test_file = tmp_path / "clean.md"
            test_file.write_text("---\nchapter: 4\norder: 40\n---\n\n外微分 d により、形式の次数が1つ上がる。\n")

            with open(test_file) as f:
                content = f.read()

            self._send_msg(
                sock,
                {
                    "jsonrpc": "2.0",
                    "method": "textDocument/didOpen",
                    "params": {
                        "textDocument": {
                            "uri": f"file://{test_file}",
                            "languageId": "markdown",
                            "version": 1,
                            "text": content,
                        }
                    },
                },
            )

            diag_msg = None
            for _ in range(10):
                msg = self._recv_msg(sock)
                if msg and msg.get("method") == "textDocument/publishDiagnostics":
                    diag_msg = msg
                    break

            assert diag_msg is not None, "No publishDiagnostics received"
            diagnostics = diag_msg["params"]["diagnostics"]
            assert len(diagnostics) == 0, f"Expected no diagnostics, got {diagnostics}"

            self._send_msg(sock, {"jsonrpc": "2.0", "id": 2, "method": "shutdown"})
            time.sleep(0.2)
            self._send_msg(sock, {"jsonrpc": "2.0", "method": "exit"})
            sock.close()
        finally:
            proc.kill()
            proc.wait()

    def test_hover_response(self, tmp_path):
        """Test that hover returns concept info."""
        port = 21003
        proc = self._start_server(port)

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(("127.0.0.1", port))
            sock.settimeout(5)

            root = str(__import__("pathlib").Path(__file__).resolve().parents[3])
            self._send_msg(
                sock,
                {
                    "jsonrpc": "2.0", "id": 1, "method": "initialize",
                    "params": {
                        "processId": None,
                        "capabilities": {},
                        "rootUri": f"file://{root}",
                    },
                },
            )
            self._recv_msg(sock)
            self._send_msg(sock, {"jsonrpc": "2.0", "method": "initialized", "params": {}})
            time.sleep(0.3)

            # Create a test file with a known concept
            test_file = tmp_path / "ch04.md"
            test_file.write_text("---\nchapter: 4\norder: 40\n---\n\nホッジ・スターについて考える。\n")

            with open(test_file) as f:
                content = f.read()

            # Open the document
            self._send_msg(
                sock,
                {
                    "jsonrpc": "2.0",
                    "method": "textDocument/didOpen",
                    "params": {
                        "textDocument": {
                            "uri": f"file://{test_file}",
                            "languageId": "markdown",
                            "version": 1,
                            "text": content,
                        }
                    },
                },
            )

            # Read away publishDiagnostics (at most 3 messages before timeout)
            sock.settimeout(1.0)
            for _ in range(3):
                try:
                    msg = self._recv_msg(sock, timeout=1.0)
                    if msg is None:
                        break
                except (TimeoutError, socket.timeout):
                    break
            sock.settimeout(5)

            # Send hover request at position of "ホッジ・スター"
            # The content after frontmatter: line 5 (blank), line 6 (the actual text)
            # LSP uses 0-based line numbers for the full document including frontmatter
            line = "ホッジ・スターについて考える。"
            col = line.find("ホッジ・スター")
            content_line_num = 5  # line 0-3: frontmatter, line 4: blank, line 5: target

            self._send_msg(
                sock,
                {
                    "jsonrpc": "2.0",
                    "id": 10,
                    "method": "textDocument/hover",
                    "params": {
                        "textDocument": {"uri": f"file://{test_file}"},
                        "position": {"line": content_line_num, "character": col + 3},  # middle of word
                    },
                },
            )

            hover_msg = None
            for _ in range(10):
                msg = self._recv_msg(sock)
                if msg and msg.get("id") == 10:
                    hover_msg = msg
                    break

            assert hover_msg is not None, "No hover response"
            assert "result" in hover_msg
            assert hover_msg["result"] is not None, "Hover result is None"
            contents = hover_msg["result"].get("contents", {})
            if isinstance(contents, dict):
                value = contents.get("value", "")
            else:
                value = str(contents)
            assert "ホッジ・スター" in value or "hodge_star" in value

            self._send_msg(sock, {"jsonrpc": "2.0", "id": 2, "method": "shutdown"})
            time.sleep(0.2)
            self._send_msg(sock, {"jsonrpc": "2.0", "method": "exit"})
            sock.close()
        finally:
            proc.kill()
            proc.wait()
