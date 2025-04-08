from app.agent import app


sample_text = """
"""

state_input = {"text": sample_text}

result = app.invoke(state_input)

print("Classification:", result["classification"])
print("\nEntities:", result["entities"])
print("\nSummary:", result["summary"])