import httpx
import os
from typing import List, Dict
from pathlib import Path
from .config import GITHUB_TOKEN, GITHUB_REPO, GITHUB_DOCS_PATH

class GitHubDocsFetcher:
    def __init__(self):
        self.token = GITHUB_TOKEN
        self.repo = GITHUB_REPO
        self.docs_path = GITHUB_DOCS_PATH
        self.base_url = "https://api.github.com"
        
    async def fetch_docs(self) -> List[Dict[str, str]]:
        """Fetch all documentation files from the GitHub repository."""
        if not self.token or not self.repo:
            raise ValueError("GitHub token and repo must be configured")
            
        headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        docs = []
        async with httpx.AsyncClient() as client:
            # Get repository tree
            tree_url = f"{self.base_url}/repos/{self.repo}/git/trees/main"
            response = await client.get(f"{tree_url}?recursive=1", headers=headers)
            response.raise_for_status()
            
            tree = response.json()
            
            # Find documentation files - restrict to gittalker/ directory only
            allowed_extensions = (
                ".md", ".txt", ".rst", ".py", ".json", ".yaml", ".yml"
            )
            doc_files = [
                item for item in tree["tree"]
                if item["path"].startswith("gittalker/")
                and item["type"] == "blob"
                and item["path"].endswith(allowed_extensions)
            ]
            
            # Fetch content for each file
            for file_info in doc_files:
                try:
                    content_url = f"{self.base_url}/repos/{self.repo}/contents/{file_info['path']}"
                    content_response = await client.get(content_url, headers=headers)
                    content_response.raise_for_status()
                    
                    file_data = content_response.json()
                    
                    # Decode base64 content
                    import base64
                    content = base64.b64decode(file_data["content"]).decode("utf-8")
                    
                    docs.append({
                        "path": file_info["path"],
                        "content": content,
                        "url": file_data["html_url"]
                    })
                    
                except Exception as e:
                    print(f"Error fetching {file_info['path']}: {e}")
                    continue
        
        return docs
    
    def save_docs_locally(self, docs: List[Dict[str, str]]) -> None:
        """Save documentation files locally for caching."""
        docs_dir = Path("docs")
        docs_dir.mkdir(exist_ok=True)
        
        for doc in docs:
            # Create safe filename
            safe_path = doc["path"].replace("/", "_")
            file_path = docs_dir / safe_path
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(doc["content"])
    
    def chunk_content(self, content: str, chunk_size: int = 1000) -> List[str]:
        """Split content into chunks for RAG processing."""
        # Simple chunking by sentences/paragraphs
        paragraphs = content.split("\n\n")
        chunks = []
        current_chunk = ""
        
        for paragraph in paragraphs:
            if len(current_chunk + paragraph) < chunk_size:
                current_chunk += paragraph + "\n\n"
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = paragraph + "\n\n"
        
        if current_chunk:
            chunks.append(current_chunk.strip())
            
        return chunks