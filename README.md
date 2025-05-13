# 📊 Pokémon Team Builder (Analisador de Status por Geração)

Este projeto é uma aplicação interativa feita com **Streamlit** que auxilia na **análise de status de Pokémon** ao longo das gerações. Ele é especialmente útil para quem deseja montar **times estratégicos**, comparando atributos como HP, ataque, defesa e velocidade, além de tipos mais comuns por geração.

---

## 🎯 Objetivo

Oferecer uma interface visual simples para explorar os dados dos Pokémon de diferentes gerações e ajudar jogadores, estrategistas e fãs a tomar decisões mais informadas ao montar seus times.

---

## 🖼️ Funcionalidades

* Visualização da **média de status por geração** (gráficos de linha, dispersão e colunas).
* Análise detalhada dos **top 10 Pokémon** de cada geração com base em atributos individuais:

  * HP
  * Speed
  * Attack
  * Special Attack
  * Defense
  * Special Defense
* Gráficos de **pizza** mostrando os **tipos primários e secundários mais comuns** em cada geração.
* Filtros laterais para seleção da geração.

---

## 🧠 Tecnologias Utilizadas

* [Python](https://www.python.org/)
* [Streamlit](https://streamlit.io/)
* [Pandas](https://pandas.pydata.org/)
* [Matplotlib](https://matplotlib.org/)
* [NumPy](https://numpy.org/)

---

## 🗂️ Estrutura Esperada do Dataset

O aplicativo espera um arquivo chamado `pokemon.csv` com as seguintes colunas:

* `name`
* `generation`
* `type1`
* `type2`
* `total`
* `hp`
* `attack`
* `defense`
* `sp_attack`
* `sp_defense`
* `speed`

> Certifique-se de que o arquivo CSV esteja no mesmo diretório do arquivo principal `.py`.

---

## 🚀 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/pokemon-team-builder.git
cd pokemon-team-builder
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute a aplicação com o Streamlit:

```bash
streamlit run nome_do_arquivo.py
```

---

## 📌 Observações

* O sistema atualmente suporta visualização até a geração 8.
* O código pode ser facilmente estendido para incluir outras gerações ou mais análises específicas.

---

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir *issues*, sugerir melhorias ou enviar *pull requests*.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---
