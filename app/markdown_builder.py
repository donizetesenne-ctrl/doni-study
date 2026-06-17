# markdown_builder.py
from datetime import datetime


def build_study_material(analysis: dict, image_name: str) -> str:
    lines = []
    assunto = analysis.get("assunto", "Material de Estudo")
    nivel = analysis.get("nivel", "intermediario")
    emoji = {"basico": "🟢", "intermediario": "🟡", "avancado": "🔴"}.get(nivel, "🟡")

    lines.append(f"# 📚 {assunto}\n")
    lines.append(f"> Gerado de: `{image_name}` | {datetime.now().strftime('%d/%m/%Y %H:%M')} | {emoji} {nivel.capitalize()}\n")
    lines.append("---\n")

    for i, t in enumerate(analysis.get("topicos", []), 1):
        lines.append(f"## {i}. {t.get('titulo', '')}\n")
        if t.get("conceito"): lines.append(f"**Conceito:** {t['conceito']}\n")
        if t.get("formula"): lines.append(f"```\n{t['formula']}\n```\n")
        if t.get("exemplo"): lines.append(f"**Exemplo:**\n```\n{t['exemplo']}\n```\n")
        if t.get("dica"): lines.append(f"> 💡 {t['dica']}\n")
        if t.get("aplicacao_real"): lines.append(f"🌍 **Na vida real:** {t['aplicacao_real']}\n")
        lines.append("---\n")

    exercicios = analysis.get("exercicios", [])
    if exercicios:
        lines.append("## 🏋️ Exercícios\n")
        for i, ex in enumerate(exercicios, 1):
            d = {"facil": "⭐", "medio": "⭐⭐", "dificil": "⭐⭐⭐"}.get(ex.get("dificuldade"), "⭐⭐")
            lines.append(f"**{i}.** {ex.get('enunciado', '')} {d}\n")
            lines.append(f"<details><summary>Resposta</summary>\n\n{ex.get('resposta', '')}\n</details>\n")

    if analysis.get("resumo_rapido"):
        lines.append(f"\n## 📋 Resumo\n{analysis['resumo_rapido']}\n")
    if analysis.get("proximo_passo"):
        lines.append(f"\n## ➡️ Próximo Passo\n{analysis['proximo_passo']}\n")

    lines.append("\n---\n*Gerado por Doni Study Generator 📸*")
    return "\n".join(lines)
