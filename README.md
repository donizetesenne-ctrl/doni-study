# 📸 Doni Study — PWA (App no Celular)

App que instala no celular como app nativo. Tira foto de qualquer coisa
e gera material de estudo completo usando Google Gemini (gratuito).

## ⚡ Como Instalar no Celular (5 minutos)

### Passo 1 — Pegar chave do Google Gemini (grátis)

1. Acesse: https://aistudio.google.com/apikey
2. Clique em "Create API Key"
3. Copie a chave (começa com `AIza...`)

### Passo 2 — Ligar o servidor no PC

```bash
cd "C:\Users\Donizete Senne\Desktop\Doni estudos\pwa"
python serve.py
```

Vai mostrar algo como:
```
🖥️  PC:      http://localhost:8080
📱 Celular: http://192.168.1.100:8080
```

### Passo 3 — Abrir no celular

1. Certifique que PC e celular estão na **mesma WiFi**
2. No celular, abra o **Chrome** ou **Edge**
3. Digite o endereço que apareceu (ex: `http://192.168.1.100:8080`)
4. Cole sua chave de API no campo que aparece

### Passo 4 — Instalar como App

- **Chrome**: Menu (⋮) → "Instalar app" ou "Adicionar à tela inicial"
- **Edge**: Menu (…) → "Adicionar ao telefone"
- **Samsung Internet**: Menu → "Adicionar à tela inicial"

Pronto! O ícone **📸 Doni Study** aparece na sua home como um app normal.

## 📱 Como Usar

1. Abra o app
2. Toque em "📷 Tirar Foto ou Escolher Imagem"
3. Tire foto do caderno/livro/quadro/tela
4. Toque em "🧠 Gerar Material de Estudo"
5. Espere 5-15 segundos
6. Material completo aparece! Pode copiar ou compartilhar.

## 🆓 Custo

- **Google Gemini**: gratuito (limite de ~50 imagens/dia no tier free)
- Sem necessidade de cartão de crédito
- Sem instalação de app de loja

## 🌐 Alternativa: Hospedar Online (sem precisar de PC ligado)

Se quiser usar SEM o PC ligado, pode hospedar grátis:

### Opção A — GitHub Pages (mais fácil)
1. Crie um repositório no GitHub
2. Faça upload da pasta `pwa/`
3. Settings → Pages → Source: main, folder: / (root)
4. Acesse: `https://seu-usuario.github.io/seu-repo`

### Opção B — Netlify (1 clique)
1. Acesse: https://app.netlify.com/drop
2. Arraste a pasta `pwa/` inteira
3. Pronto! Recebe um link HTTPS

### Opção C — Vercel
1. Instale: `npm i -g vercel`
2. Na pasta pwa: `vercel`
3. Segue os passos

Com HTTPS real, o PWA instala automaticamente sem precisar do servidor local.

## 📁 Arquivos do PWA

```
pwa/
├── index.html         ← app completo (HTML + CSS + JS)
├── manifest.json      ← configuração de instalação
├── sw.js              ← service worker (cache offline)
├── serve.py           ← servidor local para testar
├── generate_icons.py  ← gera os ícones PNG
└── icons/
    ├── icon-192.png   ← ícone do app
    └── icon-512.png   ← ícone splash screen
```

## 🔧 Funcionalidades

- ✅ Instala como app no celular
- ✅ Funciona offline (interface cached)
- ✅ Câmera direta ou galeria
- ✅ Histórico dos últimos 20 estudos
- ✅ Copiar e compartilhar resultado
- ✅ Design dark mode (confortável)
- ✅ Funciona com QUALQUER assunto
- ✅ Zero dependências externas (só HTML/JS)
