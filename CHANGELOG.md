# 🎟️ Versioning e Changelog

Cada versão segue um formato bem simples: **`tag-DD-MM-AAAA[-letra]`**.

>### 🏷️ Tags
- **`major`** 🔶 → grande avanço de tradução (seção inteira, batalha, capítulo)
- **`minor`** 🔸​ → progresso médio/pequeno, ajuste de glossário
- **`fix`** 🔧​ → correção (typo, bug, formatação)
- **`meta`** ⚙️ → infraestrutura (README, workflows, changelog, estrutura)

A data segue o nosso formato de `dia-mês-ano`, e caso **haja mais de uma mudança no mesmo dia**, usaremos a letra do alfabeto correspondente ao número de mudanças já feitas, começando pela letra **B**, seguindo até **Z**.

> O sufixo "OLD" significa apenas que as alterações durante esse período foram feitas ANTES de mudarmos o método de tradução (português sendo um novo idioma e código adaptado).

> Menções a batalhas/bosses/NPCs/lore, etc. que possam estragar a experiência ficarão marcados como spoiler.

> Seguiremos o mesmo método de changelog que o Toby Fox faz quando anuncia um na Steam. (ex: Uma batalha com um certo inimigo cinza foi traduzido.)

---

## 🔸 `minor-12-08-2026-B`

#### [CAPÍTULO 5]
- Parte da batalha contra um boss foi parcialmente traduzida. <em>(spoilers)</em>

- Parte do código que cuida da aba EQUIP (ARMADURA) foi modificado para adaptar a escala do texto do nome de armas, armaduras e habilidades que estejam grandes demais em relação às bordas da interface, isso só se aplica caso o idioma do jogo esteja em Português.

- O offset do eixo X do sprite de rolagem da página na aba foi alterado no código para em vez de 50 (padrão da versão japonesa), ser 57 (personalizado). Isso só se aplica caso o idioma do jogo esteja em Português.
<details>
<summary>Ver spoiler</summary>

A batalha da Pink foi parcialmente traduzida e polida.

</details>


## ⚙️ `meta-12-08-2026`

- Criado o `CHANGELOG.md` do projeto.

## 🔶 `major-11-08-2026`

- Toda a batalha contra o boss do capítulo 5 foi traduzida e polida.</em>

<details>
<summary>Ver spoiler</summary>

Flowery.

</details>

## ⚙️ `meta-11-08-2026-B`
- Progresso da tradução atualizado no README.

## 🔸 `minor-10-08-2026`
- Progresso na tradução e o termo Ponman traduzido no glossário. [*(Pompeão)*](https://github.com/wvntr/deltarune-ptbr/blob/dev/docs/GLOSSARIO.md#inimigos).

## ⚙️ `meta-10-08-2026-B`
- Progresso da tradução atualizado no README.

## 🔸 `minor-08-08-2026`
- Progresso na tradução e no glossário.

## 🔧 `fix-08-08-2026-B`
- Corrigido o `lang_pt.json` do Capítulo 5, que tinha sido enviado como symlink.

## ⚙️ `meta-08-08-2026-C`
- Progresso da tradução atualizado no README.

## 🔸 `minor-07-08-2026`
- Progresso na tradução, diálogos comuns foram traduzidos.

## 🔸 `minor-03-08-2026`
- Glossário atualizado e ajustado com mais itens e bosses.
- Progresso na tradução, diálogos comuns foram traduzidos.

## ⚙️ `meta-03-08-2026-B`
- `lang_pt.json` do Capítulo 5 reenviado.

## 🔧 `fix-03-08-2026-C`
- Corrigida a formatação de tabela no glossário.
- Pequeno ajuste no README.

## ⚙️ `meta-03-08-2026-D`
- Progresso da tradução atualizado no README.

## ⚙️ `meta-02-08-2026`
- Progresso da tradução atualizado no README.

## ⚙️ `meta-01-08-2026`
- Reforma na estrutura da branch e emojis adicionados ao README.

## 🔧 `fix-01-08-2026-B`
- Mais correções de tradução.

## 📈 `minor-01-08-2026-C`
- `lang_pt.json` atualizada para a versão v0.0.253 do jogo, com correções.

## 🔧 `fix-01-08-2026-D`
- Correções finais do dia.

## 🔶 `major-23-07-2026`
- Adicionado o `data.win` com o PT-BR como um novo idioma selecionável no jogo.

## ⚙️ `meta-14-07-2026-OLD`
- Revisão do README.

## 🔸 `minor-13-07-2026-OLD`
- Reorganizada a estrutura de arquivos e traduzidas as linhas 19063–19262 do Capítulo 5; testados os hash generators e a tradução do menu.

## ⚙️ `meta-13-07-2026-B-OLD`
- Adicionadas as strings originais de cada capítulo com suas devidas estruturas, e glossário atualizado para melhor compreensão.

## ⚙️ `meta-13-07-2026-C-OLD`
- Automatizado o `hash-generator.yml` e o workflow de progresso, com a adição do `manifest.json`.

## ⚙️ `meta-07-07-2026-OLD`
- Primeiras atualizações na estrutura de arquivos, criação do glossário e do README na `main-dev`.

## ⚙️ `meta-05-07-2026-OLD`
- Início do projeto: criados o `capitulo_5.json`, o `glossario.json` e a estrutura inicial da tradução.

---
