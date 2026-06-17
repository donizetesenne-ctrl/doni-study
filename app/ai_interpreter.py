# ai_interpreter.py
import json
import requests

SYSTEM_PROMPT = """Você é um tutor educacional. Analise a imagem e crie material de estudo em pt-BR.
Retorne JSON:
{
    "assunto": "...",
    "nivel": "basico/intermediario/avancado",
    "topicos": [{"titulo":"...","conceito":"...","formula":"...","exemplo":"...","dica":"...","aplicacao_real":"..."}],
    "exercicios": [{"enunciado":"...","resposta":"...","dificuldade":"facil/medio/dificil"}],
    "resumo_rapido": "...",
    "proximo_passo": "..."
}
Responda APENAS com JSON válido."""


def interpret_image(image_b64: str, mime_type: str, config: dict) -> dict:
    provider = config["ai_provider"]
    if provider == "openai":
        return _call_openai(image_b64, mime_type, config)
    elif provider == "gemini":
        return _call_gemini(image_b64, mime_type, config)
    elif provider == "ollama":
        return _call_ollama(image_b64, mime_type, config)
    return None


def _parse_json(content: str) -> dict:
    content = content.strip()
    if content.startswith("```json"): content = content[7:]
    if content.startswith("```"): content = content[3:]
    if content.endswith("```"): content = content[:-3]
    return json.loads(content.strip())


def _call_openai(image_b64, mime_type, config):
    try:
        r = requests.post("https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {config['openai_api_key']}", "Content-Type": "application/json"},
            json={"model": config["openai_model"], "max_tokens": 4000, "temperature": 0.3,
                  "messages": [{"role": "system", "content": SYSTEM_PROMPT},
                               {"role": "user", "content": [{"type": "text", "text": "Analise esta imagem."},
                                {"type": "image_url", "image_url": {"url": f"data:{mime_type};base64,{image_b64}"}}]}]},
            timeout=60)
        r.raise_for_status()
        return _parse_json(r.json()["choices"][0]["message"]["content"])
    except Exception as e:
        print(f"  ❌ OpenAI: {e}")
        return None


def _call_gemini(image_b64, mime_type, config):
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{config['gemini_model']}:generateContent?key={config['gemini_api_key']}"
        r = requests.post(url, json={
            "contents": [{"parts": [{"text": SYSTEM_PROMPT + "\nAnalise esta imagem."},
                                    {"inline_data": {"mime_type": mime_type, "data": image_b64}}]}],
            "generationConfig": {"temperature": 0.3, "maxOutputTokens": 4000}}, timeout=60)
        r.raise_for_status()
        return _parse_json(r.json()["candidates"][0]["content"]["parts"][0]["text"])
    except Exception as e:
        print(f"  ❌ Gemini: {e}")
        return None


def _call_ollama(image_b64, mime_type, config):
    try:
        r = requests.post(f"{config['ollama_url']}/api/generate",
            json={"model": config["ollama_model"], "prompt": SYSTEM_PROMPT + "\nAnalise esta imagem.",
                  "images": [image_b64], "stream": False}, timeout=120)
        r.raise_for_status()
        return _parse_json(r.json().get("response", ""))
    except Exception as e:
        print(f"  ❌ Ollama: {e}")
        return None
