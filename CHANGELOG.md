# 🎟️ Versioning e Changelog 
> ## [ALERTA DE SPOILER]

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

## 🔶 `major-25-08-2026`

#### [CAPÍTULO 5]
- Diversos polimentos foram feitos para aperfeiçoar a combinação da fala com a personalidade do personagem.

- Progresso significativo no processo de tradução.

- Todas as batalhas com **Netskie**, **Tesourete (Sheary)**, **Folhinha (Leafling)** e **Shi** foram traduzidas.

- Algumas mensagens foram polidas.

- Batalha da Aqua foi polida.

- Alguns diálogos de FLORES foram corrigidos, pois possuem uma formatação única e agora estão perfeitamente alinhadas na textbox (isso vale somente até a Netskie Climb).

- Ninjouro foi alterado para Shinobisouro no glossário para manter a consistência original.

### [ALTERAÇÕES NO CÓDIGO]
> Com o avanço da tradução, vi que diversas partes próximas da metade do Capítulo 5 são **EXTREMAMENTE MANUAIS** e **hardcoded**, portanto, listaremos as alterações feitas no código aqui *(a versão Inglesa e Japonesa permanecem intactas e inalteradas)*.

- Todo o layout da loja da primeira lanchonete foi reestruturado para ser mais consistente e condizente com a nossa língua, com todos os elementos perfeitamente alinhados em relação aos outros.

  <img width="320" height="240" alt="Image" src="https://github-production-user-asset-6210df.s3.amazonaws.com/103546534/641057730-be53d0e9-0e6e-45f7-a024-751c996ae959.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20260825%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260825T165709Z&X-Amz-Expires=300&X-Amz-Signature=7f204355a9f20c97d3bbfa2784d1fa26c59f40aa29a9b909214a9f41425756c3&X-Amz-SignedHeaders=host&response-content-type=image%2Fpng"/>


  <img width="320" height="240" alt="Image" src="https://github-production-user-asset-6210df.s3.amazonaws.com/103546534/641067152-979afd0e-44f4-403c-9311-9a961a61110d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20260825%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260825T171704Z&X-Amz-Expires=300&X-Amz-Signature=a298bf66b2c6f5772c95fef6f247784afe0848a3d26fd08b4a98da636e3c417c&X-Amz-SignedHeaders=host&response-content-type=image%2Fpng"/>

<br></br>

- Um pequeno aperfeiçoamento foi feito no menu em o nome do capítulo está traduzido e as mensagens em cima dos arquivos são agora centralizadas, semelhante a versão japonesa.

  <img width="329" height="240" alt="Image" src="https://github-production-user-asset-6210df.s3.amazonaws.com/103546534/641061141-788a9dae-65b0-44f7-aaa3-1e8d79a8a3b7.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20260825%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260825T170354Z&X-Amz-Expires=300&X-Amz-Signature=2b244a6fd7fde51fb54f62c2f849491c71a2c5c7af0a086377d9189bf1cf4d9b&X-Amz-SignedHeaders=host&response-content-type=image%2Fpng"/>

<br></br>

- As caixas diálogo da inimiga "Sheary (Tesourete)" durante uma batalha foram realinhados e escalados para os textos traduzidos realmente estarem dentro da caixa, o balão de fala dela não centraliza o texto sozinho pois ele não interage com o writer por algum motivo, as coordenadas do texto E do balão são manualmente definidas no código.

### [PROBLEMAS CONHECIDOS]

- Devido a bagunça que a `lang_pt.json` nativamente é (*sim, oficialmente*), algumas partes do fim/metade do capítulo já foram traduzidas e outras não, portanto, todos os diálogos que são de uma das FLORES que vierem **após a Netskie Climb (Escalada Netskie)** ainda estarão quebrados, porém legíveis, isso se deve ao fato de que não chegamos ainda nessa parte e apenas traduzimos esses diálogos avançados de forma rápida no início do processo de tradução (estamos traduzindo na ordem de progressão do jogo).

### [REPOSITÓRIO]

- `hash-generator.yml` foi corrigido e agora funciona corretamente, isso será importante in-game futuramente.

> Essa atualização foi feita em apenas **1 dia**, **sozinho**, esperem por atualizações maiores, pois temos mais integrantes na equipe agora!

---
## 🔶 `major-13-08-2026`

#### [CAPÍTULO 5]
- O sprite `spr_face_single_susie_alt_bushes` agora possui sua variante própria para a versão Portuguesa (`spr_face_single_susie_alt_bushes_pt`). Isto só se aplica caso o idioma atual seja o Português.

- Uma **grande** quantidade de equipamentos e armas foram traduzidas. <em>(spoilers)</em>

- Pequenos polimentos e correções em diálogos variados para se adaptarem ao clima de cada cena e ambiente.

- Algumas mensagens do Ralsei e Susie ao equiparem armaduras/armas foram traduzidas.

- As abas de Magia e Armadura foram adaptadas para caso um certo personagem esteja no grupo.

<details>
<summary>Ver spoiler</summary>

#### [ARMAS/EQUIPAMENTO]

- FiberScarf → Cachecol de Fibra
- AutoAxe → Machado Automático
- JusticeAxe → Machado da Justiça
- ToxicAxe → Machado Tóxico
- Gingerguard → GengiGuarda 
- ShadowMantle → Manto das Sombras
- MechaSaber → Sabre Mecânico
- Jevilstail → Cauda do Jevil
- TennaTie → GravaTenna
- TrueTie → Gravata Verdadeira
- B.ShotBowtie → Gravata Manda Chuva
- FrayedBowtie → Gravata Velha
- Winglade → Faca Turca
- JingleBlade → Espada Natalina

> Para ver tudo que foi traduzido, vá até o [glossário](https://github.com/wvntr/deltarune-ptbr/blob/dev/docs/GLOSSARIO.md)

#### [ITENS]

- ButJuice → MordoSuco
- ExecBuffet → Buffet Executivo
- DeluxeDinner → Jantar Luxuoso
- RenasciMenta *(já traduzida, anteriormente "ReviveMint")* → Menta Revitalizante
- Revive Dust → Pó Revitalizante
- Revive Glow → Brilho Revitalizante
- Darkburger → Hambúrguer Sombrio

> Para ver tudo que foi traduzido, vá até o [glossário](https://github.com/wvntr/deltarune-ptbr/blob/dev/docs/GLOSSARIO.md)

### [OUTRO]

- As abas de Armaduras e Magia foram adaptadas para caso o Flowery esteja no grupo.

</details>

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
