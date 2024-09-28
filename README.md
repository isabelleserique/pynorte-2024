Aqui está o formato em `.md` com emojis e uma estrutura mais atrativa:

# 🐍 Python Norte 2024 - Data Science 🌐

Olá! Se você está aqui é porque gostou do conteúdo apresentado na **PyNorte** sobre **Data Science** ou está pronto para desenvolver seu próprio projeto de integração **API-to-GCP**. 🚀

## 🎯 Primeiros Passos

1. Crie um ambiente virtual Python e instale as bibliotecas necessárias:

```bash
sudo apt install python3.8-venv
python3 -m venv nomedavenv
source nomedavenv/bin/activate
pip install pandas
pip install requests
pip install gspread google-auth google-auth-oauthlib
```

---

## ☁️ Integração com o Google Cloud Platform (GCP)

Se você tentar rodar o script `sheets.py` sem realizar a autenticação com o Google Cloud, vai encontrar erros. 😅 Não se preocupe! Aqui estão os passos para conectar seu script Python com o **GCP**:

### 1️⃣ Acesse o [Console do Google Cloud](https://console.cloud.google.com/)

### 2️⃣ Crie um novo projeto

### 3️⃣ Configure as APIs e credenciais:
   - No menu à esquerda, vá para **APIs & Services**:
      1. **Credentials**: crie as seguintes credenciais:
         - 🔑 **API Keys**
         - 🔐 **OAuth 2.0 Client IDs**
         - 👨‍💻 **Service Accounts**
      2. **Enabled APIs & Services**: clique em **+ ENABLE APIS AND SERVICES**
      3. **Ative as seguintes APIs**:
         - 📄 Google Sheets API
         - 📊 BigQuery API
         - 🔄 BigQuery Data Transfer API

### 4️⃣ Gerencie contas de serviço:
   - No menu à esquerda, vá para **IAM & Admin**:
      1. Clique em **Service Accounts**. Se não tiver uma, crie uma nova.
      2. Clique nos três pontinhos ao lado da conta e selecione **Manage keys**.
      3. Se não houver nenhuma chave, crie uma nova e baixe no formato JSON.

### 5️⃣ Faça a ponte entre o GCP e o seu script:
   - Coloque o arquivo JSON baixado no diretório do seu projeto e renomeie para `credentials.json`.
   - **Compartilhe** o e-mail da sua **Service Account** com a planilha que você está integrando.

---

🎉 Agora está tudo pronto para rodar o script `sheets.py` com sucesso!
