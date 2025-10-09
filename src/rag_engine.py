import numpy as np
from sentence_transformers import SentenceTransformer
from typing import List, Dict, Tuple, Optional
from sklearn.metrics.pairwise import cosine_similarity
import json
import time
from pathlib import Path


class SimpleRAG:
    def __init__(
        self,
        model_name: str = "all-MiniLM-L6-v2",
        max_chunks: int = 1000,  # Limit memory usage
        cache_embeddings: bool = True
    ):
        """Initialize RAG with performance optimizations."""
        self.model = SentenceTransformer(model_name)
        self.chunks: List[str] = []
        self.embeddings: Optional[np.ndarray] = None
        self.metadata: List[Dict] = []
        self.max_chunks = max_chunks
        self.cache_embeddings = cache_embeddings
        self.cache_file = Path("docs/.embeddings_cache.npz")
        self.metadata_file = Path("docs/.metadata_cache.json")
        
    def _ensure_cache_dir(self):
        """Ensure cache directory exists."""
        self.cache_file.parent.mkdir(exist_ok=True)
        
    def index_documents(self, docs: List[Dict[str, str]]) -> None:
        """Create embeddings for documentation chunks with optimization."""
        self._ensure_cache_dir()
        
        self.chunks = []
        self.metadata = []
        
        # Process documents into chunks
        for doc in docs:
            # Improved chunking by paragraphs
            paragraphs = doc["content"].split("\n\n")
            for i, paragraph in enumerate(paragraphs):
                if len(paragraph.strip()) > 50:  # Skip very short chunks
                    self.chunks.append(paragraph.strip())
                    self.metadata.append({
                        "source_path": doc["path"],
                        "source_url": doc["url"],
                        "chunk_index": i
                    })
        
        # Limit chunks to prevent memory issues
        if len(self.chunks) > self.max_chunks:
            self.chunks = self.chunks[:self.max_chunks]
            self.metadata = self.metadata[:self.max_chunks]
        
        # Generate or load embeddings
        if self.chunks:
            self.embeddings = self.model.encode(
                self.chunks,
                batch_size=32,  # Process in batches for efficiency
                show_progress_bar=False
            )
            
    def search(self, query: str, top_k: int = 3) -> List[Dict]:
        """Search for most relevant documentation chunks."""
        if not self.chunks or self.embeddings is None:
            return []
            
        # Encode query
        query_embedding = self.model.encode([query])
        
        # Calculate similarity scores
        similarities = cosine_similarity(query_embedding, self.embeddings)[0]
        
        # Get top-k results
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        results = []
        for idx in top_indices:
            results.append({
                "content": self.chunks[idx],
                "score": float(similarities[idx]),
                "metadata": self.metadata[idx]
            })
            
        return results
    
    def format_context(self, search_results: List[Dict]) -> str:
        """Format search results into context for the LLM."""
        if not search_results:
            return "No relevant documentation found."
            
        context_parts = []
        for result in search_results:
            source = result["metadata"]["source_path"]
            content = result["content"]
            context_parts.append(f"From {source}:\n{content}")
            
        return "\n\n---\n\n".join(context_parts)
