import openai

openai.api_key = "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"

models = openai.Model.list()
for model in models['data']:
    print(model['id'])