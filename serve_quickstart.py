# File name: serve_quickstart.py
import ray
import requests

from starlette.requests import Request
from ray import serve
from transformers import pipeline
from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI()


@serve.deployment(num_replicas=2, ray_actor_options={"num_cpus": 0.5, "num_gpus": 0})
@serve.ingress(app)
class Translator:
    def __init__(self):
        # Load model
        self.model = pipeline("translation_en_to_fr", model="t5-small")

    @app.post("/translator")
    def translate(self, text: str) -> str:
        # Run inference
        model_output = self.model(text)

        # Post-process output to return only the translation text
        translation = model_output[0]["translation_text"]

        return translation

    async def __call__(self, http_request: Request) -> str:
        english_text: str = await http_request.json()
        return self.translate(english_text)


translator_app = Translator.bind()
