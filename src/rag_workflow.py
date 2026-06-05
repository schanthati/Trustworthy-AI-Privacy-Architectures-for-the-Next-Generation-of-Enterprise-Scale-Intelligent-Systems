"""
Trustworthy AI Architecture
Retrieval-Augmented Generation (RAG) Workflow
Author: Sasibhushan Rao Chanthati
"""

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


class EnterpriseRAG:

    def __init__(self):
        self.embedding_model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def build_vector_index(self, documents):

        embeddings = self.embedding_model.encode(documents)

        index = faiss.IndexFlatL2(
            embeddings.shape[1]
        )

        index.add(
            np.array(embeddings).astype("float32")
        )

        return index

    def retrieve_context(
        self,
        query,
        documents,
        index,
        top_k=3
    ):

        query_embedding = self.embedding_model.encode(
            [query]
        )

        distances, indices = index.search(
            np.array(query_embedding).astype("float32"),
            top_k
        )

        return [documents[i] for i in indices[0]]


if __name__ == "__main__":

    docs = [
        "AI Governance Policy",
        "Enterprise Security Controls",
        "Responsible AI Framework"
    ]

    rag = EnterpriseRAG()

    index = rag.build_vector_index(docs)

    results = rag.retrieve_context(
        "AI compliance requirements",
        docs,
        index
    )

    print(results)
