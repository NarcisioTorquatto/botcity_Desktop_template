## BotCity Desktop Automation - Template

Este repositório contém um template para automação de bots utilizando **BotCity**, uma poderosa ferramenta de automação desktop e web.

## 📌 Requisitos

Antes de começar, certifique-se de que possui os seguintes requisitos instalados:

- Python 3.7+
- BotCity Framework (`botcity-core`, `botcity-maestro-sdk`)
- Navegador compatível (Chrome, Firefox, etc.)

Para instalar as dependências, execute:

```sh
pip install botcity-core botcity-maestro-sdk
```

---

## 🚀 Como Usar

O código contém um bot simples que:

1. Se conecta ao **BotMaestro**
2. Registra a execução da automação
3. Abre um site no navegador (`http://www.botcity.dev`)

### **Executando o Bot**
Para rodar o bot localmente, use:

```sh
python bot.py
```

Caso o bot esteja integrado ao **BotCity Maestro**, ele será acionado automaticamente pelo sistema.

---

## 🛠 Estrutura do Código

### Classe `MyBot`

- `alerts()`: Registra e finaliza a execução no **BotMaestro**.
- `open_site()`: Abre o site no navegador.
- `run()`: Método opcional para executar todas as etapas automaticamente.

### Função `main()`

- Instancia e executa o bot com tratamento de exceções.

---

## ⚠ Tratamento de Erros

Se ocorrer um erro durante a execução, o bot capturará uma **screenshot** da tela atual e registrará no log. O tempo de espera antes do encerramento é de **5 segundos**.

---

## 📝 Licença

Este projeto é open-source e pode ser usado livremente para fins educacionais e comerciais.

---

📌 **Dica**: Customize este código conforme suas necessidades, adicionando mais funcionalidades como interações com sistemas desktop, OCR e automações avançadas!

---

