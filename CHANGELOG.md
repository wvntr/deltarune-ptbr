# 🎟️ Versioning e Changelog 
> ## [SPOILERS]

Cada versão segue um formato bem simples: **`tag-DD-MM-AAAA[-letra]`**.

>### 🏷️ Tags
- **`major`** 🔶 → progresso grande
- **`minor`** 🔸​ → progresso pequeno
- **`fix`** 🔧​ → correção
- **`meta`** ⚙️ → infraestrutura

A data segue o NOSSO formato de `dia-mês-ano`, e caso **haja mais de uma mudança no mesmo dia**, usaremos a letra do alfabeto correspondente ao número de mudanças já feitas, começando pela letra **B**, seguindo até **Z**.

> O sufixo "OLD" significa apenas que as alterações durante esse período foram feitas ANTES de mudarmos o método de tradução (português sendo um novo idioma e código adaptado).

> Menções a batalhas/bosses/NPCs/lore, etc. que possam estragar a experiência ficarão marcados como spoiler.

---

## 🔶/⚙️ `major-26-08-2026`

#### [CAPÍTULO 5]
- Progresso significativo na tradução (38.75% ➔ 57.95%), este progresso em particular foi feito em 1 dia.

- Mais diálogos de flores foram traduzidos e corrigidos.

- As batalhas da dupla **Turquesa** (*Aqua*) **e Seth** e **Crá-Crá** (*Kawkaw*) foram traduzidas.

- Alguns crashes foram corrigidos.

- Algumas mensagens que precisavam ser adaptadas pelo próprio código foram hardcoded, já que só se aplicavam ao idioma português.

> O capítulo 5 é jogável de forma totalmente traduzida até a entrada do *Castelo das Flores*, após a batalha em dupla de *Seth e Turquesa* (*Aqua*).

### [ALTERAÇÕES NO CÓDIGO]

- O código da batalha com **Nubert**, **Bolinha** e **Floradino** foi adaptado para usar o masculino ou feminino dependendo de qual gênero for escolhido na frase *"Can you get me a hot gamer girlfriend."* (*Me arranja um/uma namorado(a) gamer sexy?*)

| Masculino | Feminino |
|---|---|
| <img width="320" height="240" alt="image" src="https://github-production-user-asset-6210df.s3.amazonaws.com/103546534/641639186-7abf183d-9b8f-437a-b78e-ed0052481177.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20260826%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260826T143844Z&X-Amz-Expires=300&X-Amz-Signature=5340a212429d5a70d496dd3c2675869de6d316b4dc1d7f2913661a6543463df0&X-Amz-SignedHeaders=host&response-content-type=image%2Fpng"/> | <img width="320" height="240" alt="image" src="https://github-production-user-asset-6210df.s3.amazonaws.com/103546534/641636443-ea7d7fe6-d5bf-4b98-b085-9745a93faa19.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20260826%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260826T143417Z&X-Amz-Expires=300&X-Amz-Signature=d0fbb33072636f7ffd0c09a61b1f10f3d8348e5afa573ab2fb93151abdea7c93&X-Amz-SignedHeaders=host&response-content-type=image%2Fpng"/> |

- O layout da loja da Pink foi adaptado para o mesmo layout da lanchonete, além de finalmente termos adaptado a *Lâmina de Madeira 2* para não atravessar o texto do preço e estar proporcional.

### [REPOSITÓRIO]

- Adicionada a pasta `/sem-herança` para facilitar a tradução, removendo linhas da lang dos capítulos anteriores.
- Adicionada a lang capítulo 4 para comparação.
- `hash-generator.yml` foi corrigido e gera as hashes corretamente.
- Algumas mudanças menores na estrutura do repositório.

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

<img width="320" height="240" alt="image" src="https://github.com/user-attachments/assets/4094bcf9-87ac-46cb-bd3a-10d97ca90985" />

<img width="320" height="240" alt="image" src="https://github.com/user-attachments/assets/4c98052a-3840-4418-8a64-239d52535820" />


<br></br>

- Um pequeno aperfeiçoamento foi feito no menu em o nome do capítulo está traduzido e as mensagens em cima dos arquivos são agora centralizadas, semelhante a versão japonesa.

<img width="320" height="240" alt="image" src="https://github.com/user-attachments/assets/4162947d-cc3d-4b15-9750-fbdd99c264c4" />


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
