import httpx
import os
import json
import time
from typing import List, Dict
from pathlib import Path
from .config import GITHUB_TOKEN, GITHUB_REPO, GITHUB_DOCS_PATH


class GitHubDocsFetcher:
    def __init__(self, cache_ttl: int = 3600):  # 1 hour cache
        self.token = GITHUB_TOKEN
        self.repo = GITHUB_REPO
        self.docs_path = GITHUB_DOCS_PATH
        self.base_url = "https://api.github.com"
        self.cache_ttl = cache_ttl
        self.cache_file = Path("docs/.docs_cache.json")
        self._ensure_cache_dir()
        
    def _ensure_cache_dir(self):
        """Ensure cache directory exists."""
        self.cache_file.parent.mkdir(exist_ok=True)
        
    def _is_cache_valid(self) -> bool:
        """Check if cache is still valid."""
        if not self.cache_file.exists():
            return False
            
        cache_age = time.time() - self.cache_file.stat().st_mtime
        return cache_age < self.cache_ttl
        
    def _load_cache(self) -> List[Dict[str, str]]:
        """Load docs from cache."""
        try:
            with open(self.cache_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
            
    def _save_cache(self, docs: List[Dict[str, str]]) -> None:
        """Save docs to cache."""
        try:
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(docs, f, ensure_ascii=False, indent=2)
        except IOError:
            pass  # Continue without caching if file operations fail
        
    async def fetch_docs(self) -> List[Dict[str, str]]:
        """Fetch all documentation files from the GitHub repository."""
        # Check cache first
        if self._is_cache_valid():
            cached_docs = self._load_cache()
            if cached_docs:
                return cached_docs
                
        # Fetch fresh data
        docs = await self._fetch_docs_from_github()
        
        # Cache the results
        self._save_cache(docs)
        
        return docs
        
    async def _fetch_docs_from_github(self) -> List[Dict[str, str]]:
        """Fetch docs from GitHub API."""
        if not self.token or not self.repo:
            raise ValueError("GitHub token and repo must be configured")
            
        headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        docs = []
        timeout = httpx.Timeout(30.0)  # 30 second timeout
        
        async with httpx.AsyncClient(timeout=timeout) as client:
            # Get repository tree
            tree_url = f"{self.base_url}/repos/{self.repo}/git/trees/main"
            response = await client.get(
                f"{tree_url}?recursive=1",
                headers=headers
            )
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
                    content_url = (
                        f"{self.base_url}/repos/{self.repo}/contents/"
                        f"{file_info['path']}"
                    )
                    content_response = await client.get(
                        content_url,
                        headers=headers
                    )
                    content_response.raise_for_status()
                    
                    file_data = content_response.json()
                    
                    # Decode base64 content
                    import base64
                    content = base64.b64decode(
                        file_data["content"]
                    ).decode("utf-8")
                    
                    docs.append({
                        "path": file_info["path"],
                        "content": content,
                        "url": file_data["html_url"]
                    })
                    
                except (httpx.HTTPError, KeyError, ValueError) as e:
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