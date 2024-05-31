import os
from scrapegraphai.graphs import SearchGraph
from dotenv import load_dotenv

load_dotenv()

# Define the configuration for the graph
graph_config = {
    "llm": {
        "model": "groq/gemma-7b-it",
        "api_key": os.getenv("GROQ_API_KEY"),
        "temperature": 0
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "base_url": "http://localhost:11434",  # set ollama URL arbitrarily
    },
    "max_results": 5,
}

# Create the SearchGraph instance
search_graph = SearchGraph(
    prompt="List me the latest papers for ai in radiology",
    config=graph_config
)

# Run the graph
result = search_graph.run()
print(result)