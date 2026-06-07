from git import Repo


class GitHubMCPClient:

    def __init__(self):

        self.repo = Repo(".")

    async def search_recent_commits(
        self,
        limit: int = 5
    ):

        commits = []

        try:

            for commit in self.repo.iter_commits(
                max_count=limit
            ):

                commits.append(
                    {
                        "hash": commit.hexsha[:8],
                        "message": commit.message.strip(),
                        "author": str(commit.author),
                    }
                )

        except Exception as e:

            commits.append(
                {
                    "error": str(e)
                }
            )

        return commits