from pathlib import Path


class FilesystemMCPClient:

    def __init__(self):
        self.server_name = "filesystem-mcp"

    async def read_file(
        self,
        file_path: str
    ):

        path = Path(file_path)

        if not path.exists():
            return {
                "status": "error",
                "message": "File not found"
            }

        return {
            "status": "success",
            "content": path.read_text(
                encoding="utf-8"
            )
        }

    async def search_logs(
        self,
        directory: str
    ):

        return {
            "status": "success",
            "directory": directory
        }