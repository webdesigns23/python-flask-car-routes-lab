from flask import Flask
app = Flask(__name__)

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

@app.route('/')
def index():
	return "Welcome to Flatiron Cars"

@app.route('/<string:model>')
def model(model):
	model_lower = model.lower()
	existing_models_lower = [model.lower() for model in existing_models]
	if model_lower in existing_models_lower:
		return f"Flatiron {model.capitalize()} is in our fleet!"
	else:
		return f"No models called {model} exists in our catalog"


if __name__ == '__main__':
	app.run(port=5555, debug=True)