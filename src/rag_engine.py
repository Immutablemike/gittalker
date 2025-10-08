import numpy as np
from sentence_transformers import SentenceTransformer
from typing import List, Dict, Tuple
from sklearn.metrics.pairwise import cosine_similarity


class SimpleRAG:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """Initialize RAG with a lightweight sentence transformer model."""
        self.model = SentenceTransformer(model_name)
        self.chunks: List[str] = []
        self.embeddings: np.ndarray = None
        self.metadata: List[Dict] = []
        
    def index_documents(self, docs: List[Dict[str, str]]) -> None:
        """Create embeddings for documentation chunks."""
        self.chunks = []
        self.metadata = []
        
        for doc in docs:
            # Simple chunking by paragraphs
            paragraphs = doc["content"].split("\n\n")
            for i, paragraph in enumerate(paragraphs):
                if len(paragraph.strip()) > 50:  # Skip very short chunks
                    self.chunks.append(paragraph.strip())
                    self.metadata.append({
                        "source_path": doc["path"],
                        "source_url": doc["url"],
                        "chunk_index": i
                    })
        
        # Generate embeddings for all chunks
        if self.chunks:
            self.embeddings = self.model.encode(self.chunks)
            
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