import json
from pathlib import Path

class NodeCognitionEngine:
    def __init__(self, metadata_path, suggestions_path):
        self.metadata_path = Path(metadata_path)
        self.suggestions_path = Path(suggestions_path)
        self.metadata = self._load_json(self.metadata_path)
        self.suggestions = self._load_json(self.suggestions_path)

    def _load_json(self, path):
        if not path.exists():
            return {}
        with open(path, 'r') as file:
            return json.load(file)

    def _save_json(self, path, data):
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)

    def update_metadata(self, key, value):
        self.metadata[key] = value
        self._save_json(self.metadata_path, self.metadata)

    def add_suggestion(self, suggestion):
        if "suggestions" not in self.suggestions:
            self.suggestions["suggestions"] = []
        self.suggestions["suggestions"].append(suggestion)
        self._save_json(self.suggestions_path, self.suggestions)

    def evaluate_suggestions(self):
        evaluations = []
        for suggestion in self.suggestions.get("suggestions", []):
            trust_delta = self._simulate_trust_evaluation(suggestion)
            evaluations.append((suggestion, trust_delta))
        return evaluations

    def _simulate_trust_evaluation(self, suggestion):
        return 1 if "clarity" in suggestion.lower() else -1

# Example Usage:
# engine = NodeCognitionEngine('Nodes/Node_0001/metadata.json', 'Nodes/Node_0001/peer_suggestions.json')
# engine.update_metadata("status", "active")
# engine.add_suggestion("Improve clarity in definition X.")
# print(engine.evaluate_suggestions())
