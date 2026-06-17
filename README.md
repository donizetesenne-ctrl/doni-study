# 📸 Doni Study — Gerador de Material de Estudo por Imagem

Tira foto de **qualquer assunto** → recebe material de estudo completo com IA.

## 🌐 App no Celular (PWA)

**Link direto:** https://donizetesenne-ctrl.github.io/doni-study/

Instale: Chrome → Menu → "Instalar app"

## 📁 Estrutura do Projeto

```
Doni-Estudos/
├── index.html              ← PWA (app celular)
├── manifest.json           ← config instalação
├── sw.js                   ← service worker
├── icons/                  ← ícones do app
├── app/                    ← versão Python (desktop)
│   ├── study_generator.py  ← script principal
│   ├── ai_interpreter.py   ← IA (Gemini/OpenAI/Ollama)
│   ├── config.py           ← configuração
│   └── markdown_builder.py ← gera .md
├── modulos/                ← módulos de estudo prontos
│   ├── 01-matematica-base.md
│   ├── 02-circuitos-trifasicos.md
│   ├── 03-transformadores.md
│   ├── 04-distribuicao.md
│   └── 05-formulas-avancadas.md
├── imagens/                ← coloque fotos aqui (Python)
├── output/                 ← materiais gerados (Python)
├── requirements.txt
├── .env.example
└── serve.py                ← servidor local para teste
```

## ⚡ Uso no Celular

1. Acesse o link acima
2. Cole sua chave Gemini (grátis: https://aistudio.google.com/apikey) ou OpenAI
3. Tire foto → Material gerado!

## 💻 Uso no PC (Python)

```bash
pip install -r requirements.txt
copy .env.example .env
# Edite .env com sua chave
python app/study_generator.py imagens/foto.jpg
```

## 🔑 APIs Suportadas

| Provider | Custo | Como pegar |
|----------|-------|-----------|
| Google Gemini | Grátis (50/dia) | aistudio.google.com/apikey |
| OpenAI | ~R$0,05/foto | platform.openai.com/api-keys |
| Ollama | Grátis (local) | ollama.ai → `ollama pull llava` |
